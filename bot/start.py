from aiogram import Dispatcher,Bot, types
Token = ""
bot = Bot(token=Token)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(f"Hi, {message.from_user.full_name}")