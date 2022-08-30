from aiogram.dispatcher.dispatcher import Dispatcher
from fastapi import FastAPI
from aiogram import types, Dispatcher, Bot
from bot.start import dp, bot

app = FastAPI()

webhook_path = f"/bot/{bot}"
webhook_url = "" + webhook_path


@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != webhook_url:
        await bot.set_webhook(
            url=webhook_url
        )


@app.post(webhook_path)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.on_event("shutdown")
async def on_shutdown():
    pass

