import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from aiogram.fsm.storage.memory import MemoryStorage
from keyboard import (
    main_menu, ijara_menu, muddat_ijara, reg,
    humans_menu, xona_button, sotix_button,
    res, get_uy_keyboard, create_price_keyboard,
    vosita_button, number_button
)

from aiogram.client.session.aiohttp import AiohttpSession


PROXY_URL = 'http://proxy.server:3128'
session = AiohttpSession(proxy=PROXY_URL)


from states import KvState

TOKEN = "8572413186:AAEOX4uYKixrivLYO-dsrjtnNK-rwn_YkZY"


dp = Dispatcher(storage=MemoryStorage())
bot = Bot(token=TOKEN, session=session)

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer("""
Ijara bot ga xush kelibsiz!

Kerakli bo‘limni tanlang. 👇
""", reply_markup=main_menu)
    

@dp.message(F.text == "🔑Ijaraga beraman")
async def i_b(message: types.Message):
    await message.answer("""
Qanday turdagi binoni ijaraga berasiz?

Tugmalardan birini tanlang 👇
""", reply_markup=ijara_menu)
    

# --- kvartira bo'limi ---- 
@dp.message(F.text == "Kvartira")
async def k_b(message: types.Message, state: FSMContext):
    await message.answer("""
Qancha muddatga ijaraga berasiz?

Tugmalardan birini tanlang 👇
""", reply_markup=muddat_ijara)
    await state.set_state(KvState.muddat)


@dp.message(KvState.muddat)
async def kv_m(message: types.Message, state: FSMContext):
    await state.update_data(muddat=message.text)
    await message.answer("""
Qaysi tumanda?

Tugmalardan birini tanlang 👇
""", reply_markup=reg)
    await state.set_state(KvState.tuman)


@dp.message(KvState.tuman)
async def kv_t(message: types.Message, state: FSMContext):
    await state.update_data(tuman=message.text)
    await message.answer("""
Kimlarga ijaraga bermoqchisiz?

Tugmalardan birini tanlang 👇
""", reply_markup=humans_menu)
    await state.set_state(KvState.kimga)


@dp.message(KvState.kimga)
async def kv_k(message: types.Message, state: FSMContext):
    await state.update_data(kimga=message.text)
    await message.answer("""
Necha xona

Tugmalardan birini tanlang 👇
""", reply_markup=xona_button)
    await state.set_state(KvState.xona_s)


@dp.message(KvState.xona_s)
async def kv_s(message: types.Message, state: FSMContext):
    await state.update_data(xona_s=message.text)
    await message.answer("""
Maydoni necha kvadrat bo'lsin? (m²)

Tugmalardan birini tanlang 👇
""", reply_markup=sotix_button)
    await state.set_state(KvState.maydoni)


@dp.message(KvState.xona_s)
async def kv_s(message: types.Message, state: FSMContext):
    await state.update_data(xona_s=message.text)
    await message.answer("""
Maydoni necha kvadrat bo'lsin? (m²)

Tugmalardan birini tanlang 👇
""", reply_markup=sotix_button)
    await state.set_state(KvState.maydoni)


@dp.message(KvState.maydoni)
async def kv_m(message: types.Message, state: FSMContext):
    await state.update_data(maydoni=message.text)
    await message.answer("""
Ta'miri qanday?

Tugmalardan birini tanlang 👇
""", reply_markup=res)
    await state.set_state(KvState.tamir)


@dp.message(KvState.tamir)
async def kv_t(message: types.Message, state: FSMContext):
    await state.update_data(tamir=message.text)
    await message.answer("""
Yevro ta'mir

Binoda bor qo'shimcha jihozlarni quyidagi tugmalar yordamida tanlang 👇
""", reply_markup=get_uy_keyboard())
    await state.set_state(KvState.jihoz)


@dp.message(KvState.jihoz)
async def kv_jj(message: types.Message, state: FSMContext):
    await state.update_data(jihoz=message.text)
    await message.answer("""
📎 Shu belgini bosib rasmlarni yuklang.

❗️Rasmlar soni 10 tadan oshmasin.
""", reply_markup=ReplyKeyboardRemove())
    await state.set_state(KvState.rasm)


@dp.message(KvState.rasm, F.photo)
async def kv_ra(message: types.Message, state: FSMContext):
    await state.update_data(rasm=message.photo[-1].file_id)
    await message.answer("""
Narxi qancha? (1 oy uchun)

Tugmalardan birini tanlang 👇
""", reply_markup=create_price_keyboard())
    await state.set_state(KvState.narx)


@dp.message(KvState.narx)
async def kv_narx(message: types.Message, state: FSMContext):
    await state.update_data(narx=message.text)
    await message.answer("""
Vositachilik haqi bormi?

Agar bo'lsa, necha foiz?

Vositachilik haqi yo'q bo'lsa YO'Q tugmasini bosing 👇
""", reply_markup=vosita_button)
    await state.set_state(KvState.makler)


@dp.message(KvState.makler)
async def kv_ds(message: types.Message, state: FSMContext):
    await state.update_data(makler=message.text)
    await message.answer("""
Telefon raqamni yuborish tugmasini bosing,

yoki boshqa raqamingizni shu ko‘rinishda yozing!

👉 +998901234567
""", reply_markup=number_button)
    await state.set_state(KvState.nomer)


@dp.message(KvState.nomer, F.contact)
async def kv_mak(message: types.Message, state: FSMContext):
    await state.update_data(nomer=message.contact.phone_number)
    await message.answer("""
Qo'shimcha ma'lumot bo'lsa yozing. Yoki,

Davom etish ➡️ tugmasini bosing.
""")
    await state.set_state(KvState.qushimcha)


@dp.message(KvState.qushimcha)
async def kv_qushimcha(message: types.Message, state: FSMContext):
    await state.update_data(qushimcha=message.text)
    data = await state.get_data()
    text = f"""
🌟IJARA-CHI | KVARTIRA, {data.get('muddat')}

📍 Manzil: Toshkent, {data.get('manzil')}
🛠️ Ta'mir: {data.get('tamir')}
👥 Kimlarga: {data.get('kimga')}
🚪 Necha xona: {data.get('xona_s')}
📐 Maydoni: {data.get('maydoni')} m²
💵 Narxi: {data.get('narx')} y.e
🤝 Vositachilik haqi: {data.get('makler')} %
🔌 Jihozlar: {data.get('jihoz')}

✏️ @{message.from_user.username}
📱 {data.get('nomer')}


📣 KANAL    📝 OLX
👥 GURUH   📷 INSTAGRAM

"""
    await state.clear()
    await message.answer_photo(photo=data.get('rasm'), caption=text, reply_markup=main_menu)


# ----dacha-----


    








async def main() -> None:
    # bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())