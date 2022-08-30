from aiogram import Dispatcher, Bot, types
bot = Bot(token="")
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Hi")