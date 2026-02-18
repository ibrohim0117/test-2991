from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔎Ijaraga olaman"),
            KeyboardButton(text="🔑Ijaraga beraman")
        ],
        [
            KeyboardButton(text="🌐Tilni ozgartirish"),
            KeyboardButton(text="❓ Qanday ishlaydi")
        ],
        [
            KeyboardButton(text="Mening elonlarim")
        ]
    ],
    resize_keyboard=True
)


ijara_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kvartira"),
            KeyboardButton(text="Uy hovli")
        ],
        [
            KeyboardButton(text="Dacha"),
            KeyboardButton(text="Ofis")
        ],
        [
            KeyboardButton(text="🏠 Bosh sahifa")
        ]
    ],
    resize_keyboard=True 
)


muddat_ijara = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Uzoq muddatga"),
        ],
        [
            KeyboardButton(text="Kunlik"),
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
            KeyboardButton(text="🏠 Bosh sahifa")
        ]
    ],
    resize_keyboard=True
)

reg = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌐 Boshqa viloyatni tanlash")
        ],
        [
            KeyboardButton(text="Yakkasaroy"),
            KeyboardButton(text="Yashnobod")
        ],
        [
            KeyboardButton(text="Shayhontohur"),
            KeyboardButton(text="Chilonzor"),
        ],
        [
            KeyboardButton(text="Bektemir"),
            KeyboardButton(text="Olmazor")
        ],
        [
            KeyboardButton(text="Mirobod"),
            KeyboardButton(text="Mirzo-Ulug'bek")
        ],
        [
            KeyboardButton(text="Uchtepa"),
            KeyboardButton(text="Yunusobod")
        ],
        [
            KeyboardButton(text="Sergeli"),
            KeyboardButton(text="Yangihayot")
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
            KeyboardButton(text="🏠 Bosh sahifa")
        ]
    ]
)


humans_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Talabalarga"),
            KeyboardButton(text="Ishchilarga")
        ],
        [
            KeyboardButton(text="Sayyohlarga"),
            KeyboardButton(text="Oilaga")
        ],
        [
            KeyboardButton(text="Sheriklikka"),
            KeyboardButton(text="Barchaga")
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
            KeyboardButton(text="🏠 Bosh sahifa")
        ],
    ],
    resize_keyboard=True
)


xona_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "1 xona"),
            KeyboardButton(text = "2 xona"),
            KeyboardButton(text = "3 xona"),
            KeyboardButton(text = "4 xona"),
        ],
        [
            KeyboardButton(text = "5 xona"),
            KeyboardButton(text = "6 xona"),
            KeyboardButton(text = "7 xona"),
            KeyboardButton(text = "8 xona"),
        ],
        [
            KeyboardButton(text = "9 xona"),
            KeyboardButton(text = "10 xona"),
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
            KeyboardButton(text="🏠 Bosh sahifa")
        ]
    ]
)


sotix_button = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text = "20 m²"),
            KeyboardButton(text = "22 m²"),
            KeyboardButton(text = "25 m²"),
            KeyboardButton(text = "28 m²"),
        ],
        [
            KeyboardButton(text = "30 m²"),
            KeyboardButton(text = "32 m²"),
            KeyboardButton(text = "35 m²"),
            KeyboardButton(text = "38 m²"),
        ],
        [
            KeyboardButton(text = "40 m²"),
            KeyboardButton(text = "42 m²"),
            KeyboardButton(text = "45 m²"),
            KeyboardButton(text = "48 m²"),
        ],
        [
            KeyboardButton(text = "50 m²"),
            KeyboardButton(text = "52 m²"),
            KeyboardButton(text = "55 m²"),
            KeyboardButton(text = "58 m²"),
        ],
        [
            KeyboardButton(text = "60 m²"),
            KeyboardButton(text = "62 m²"),
            KeyboardButton(text = "65 m²"),
            KeyboardButton(text = "68 m²"),
        ],
        [
            KeyboardButton(text = "70 m²"),
            KeyboardButton(text = "72 m²"),
            KeyboardButton(text = "75 m²"),
            KeyboardButton(text = "78 m²"),
        ],
        [
            KeyboardButton(text = "80 m²"),
            KeyboardButton(text = "82 m²"),
            KeyboardButton(text = "85 m²"),
            KeyboardButton(text = "88 m²"),
        ],
        [
            KeyboardButton(text = "90 m²"),
            KeyboardButton(text = "92 m²"),
            KeyboardButton(text = "95 m²"),
            KeyboardButton(text = "98 m²"),
        ],
        [
           KeyboardButton(text = "100 m²"),
           KeyboardButton(text = "105 m²"),
           KeyboardButton(text = "110 m²"),
           KeyboardButton(text = "115 m²"),
        ],
        [
           KeyboardButton(text = "120 m²"),
           KeyboardButton(text = "125 m²"), 
           KeyboardButton(text = "130 m²"),
           KeyboardButton(text = "135 m²"),
        ],
        [
              KeyboardButton(text = "140 m²"),
              KeyboardButton(text = "145 m²"), 
              KeyboardButton(text = "150 m²"),
              KeyboardButton(text = "155 m²"),
        ],
        [
              KeyboardButton(text = "160 m²"),
              KeyboardButton(text = "165 m²"), 
              KeyboardButton(text = "170 m²"),
              KeyboardButton(text = "175 m²"),
        ],
        [
              KeyboardButton(text = "180 m²"),
              KeyboardButton(text = "185 m²"), 
              KeyboardButton(text = "190 m²"),
              KeyboardButton(text = "195 m²"),
        ]
    ],
    resize_keyboard=True
)   



res= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yevro ta'mir"),
            KeyboardButton(text="Ta'mirsiz"),
        ],
        [
            KeyboardButton(text="O'rtacha ta'mir"),
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
            KeyboardButton(text="🏠 Bosh sahifa"),
        ],
    ],
    resize_keyboard=True
)


def get_uy_keyboard() -> ReplyKeyboardMarkup:
    uy_buttons = [
        "Internet", "Telefon tarmog'i", "Sun'iy yo'ldosh/kabel TV",
        "Videokuzatuv", "Gaz ta'minoti", "Suv ta'minoti",
        "Kanalizatsiya", "Qo'riqlash", "Bolalar maydonchasi",
        "Mebel", "Televizor", "Hammom",
        "Konditsioner", "Kir yuvish mashinasi", "Mikroto'lqinli pech",
        "Muzlatgich", "Lift", "Avtoturargox"
    ]
    
    builder = ReplyKeyboardBuilder()
    
    for button in uy_buttons:
        builder.button(text=button)
    
    # Tugmalarni 2 tadan qatorga teradi
    builder.adjust(2)
    
    return builder.as_markup(resize_keyboard=True)

def create_price_keyboard(start=10, end=20000, step=10, buttons_per_row=2):
    keyboard = []
    row = []

    for i in range(start, end + 1, step):
        row.append(KeyboardButton(text=f"{i} y.e"))

        if len(row) == buttons_per_row:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
)


vosita_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Yo'q")
        ],
        [
            KeyboardButton(text = "50 %"),
            KeyboardButton(text = "40 %")
        ],
        [
            KeyboardButton(text = "30 %"),
            KeyboardButton(text = "25 %")
        ],
        [
            KeyboardButton(text = "20 %"),
            KeyboardButton(text = "15 %")
        ],
        [
            KeyboardButton(text = "10 %"),
            KeyboardButton(text = "5 %")
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
            KeyboardButton(text="🏠 Bosh sahifa")
        ]
    ]
)

number_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Contactni yuborish", request_contact=True)
        ]
    ]
)


print("botlar")