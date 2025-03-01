import asyncio
import os

from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, CallbackQuery
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from keyboards import register_inl_btn, get_phone_btn, add_product_btn
from states import UserRegisterState
from database import db

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    user = db.get_telegram_user_from_db(message.from_user.id)
    if user:
        await message.answer("Do'konimizga xush kelibsiz!\n"
                             "Ro'yxatdan o'ting!", reply_markup=register_inl_btn)
        if user.get("is_seller"):
            await message.answer("Mahsulot qo'shishingiz mumkin:",
                                 reply_markup=add_product_btn)
    else:
        await message.answer("Do'konimizga xush kelibsiz!\n"
                             "Ro'yxatdan o'ting!", reply_markup=register_inl_btn)


@dp.message(Command("help"))
async def _help(message: types.Message):
    await message.answer("Help")


@dp.message(Command("images"))
async def get_image(msg: types.Message):
    img = FSInputFile("images/img.png")
    await msg.answer_photo(img, caption="Bu screenshot")


@dp.message(Command("videos"))
async def get_video(msg: types.Message):
    video = FSInputFile("videos/20250218-0428-29.7812879.mp4")
    await msg.answer_video(video, caption="Bu screenrecorder")


@dp.message(F.video)
async def get_video(msg: types.Message):
    await msg.answer("Video uchun rahmat")


@dp.callback_query(F.data == "/register")
async def user_register(call: CallbackQuery, state: FSMContext):
    await state.set_state(UserRegisterState.full_name)
    await call.message.answer("Ismingizni kiriting:")


@dp.message(UserRegisterState.full_name)
async def get_full_name(msg: types.Message, state: FSMContext):
    await state.update_data(full_name=msg.text)
    await state.set_state(UserRegisterState.phone_number)
    await msg.answer("Telefon raqamingizni kiriting: ", reply_markup=get_phone_btn)


@dp.message(UserRegisterState.phone_number)
async def get_phone_number(msg: types.Message, state: FSMContext):
    if msg.text:
        await state.update_data(phone_number=msg.text)
    elif msg.contact.phone_number:
        await state.update_data(phone_number=msg.contact.phone_number)
    await state.set_state(UserRegisterState.age)
    await msg.answer("Yoshingizni kiriting:")


@dp.message(UserRegisterState.age)
async def get_age(msg: types.Message, state: FSMContext):
    await state.update_data(age=msg.text)
    await state.set_state(UserRegisterState.address)
    await msg.answer("Addresingizni kiriting:")


@dp.message(UserRegisterState.address)
async def get_address(msg: types.Message, state: FSMContext):
    await state.update_data(address=msg.text)
    data = await state.get_data()
    await msg.answer(f"Ism: {data['full_name']}\n"
                     f"Telefon: {data['phone_number']}\n"
                     f"age: {data['age']}\n"
                     f"address: {data['address']}")


async def main():
    print("Starting...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
