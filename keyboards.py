from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

add_product_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Mahsulot qo'shish", callback_data="/add_product")],
], resize_keyboard=True)

register_inl_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Ro'yxatdan o'tish", callback_data="/register")]
])

get_phone_btn = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="telefon raqamni jo'natish", request_contact=True),
    ]
], resize_keyboard=True)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Button"),
        KeyboardButton(text="Yordam"),
        KeyboardButton(text="Button3"),
    ],
    [
        KeyboardButton(text="Button4"),
        KeyboardButton(text="Button5"),
        KeyboardButton(text="Button6"),
    ]
])

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Inline Keyboard", callback_data="Yordam"),
         InlineKeyboardButton(text="Inline Keyboard2", callback_data="Test2", url="https://telegram.org")]
    ]
)