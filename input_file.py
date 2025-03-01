from aiogram.fsm.state import StatesGroup, State


class UserRegisterState(StatesGroup):
    full_name = State()
    phone_number = State()