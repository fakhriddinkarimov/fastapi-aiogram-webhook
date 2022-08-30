from fastapi import FastAPI
from aiogram import types
from bot.start import dp, bot,Token

app = FastAPI()

webhook_path = f"/bot/{Token}"
webhook_url = ""


@app.on_event("startup")
async def on_bot():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != webhook_url:
        await bot.set_webhook(url=webhook_url)

@app.post(webhook_path)
async def bot_webhook(update: dict):
    updater = types.Update(**update)
    await dp.process_update(updater)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()