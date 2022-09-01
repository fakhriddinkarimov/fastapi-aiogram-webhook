import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from aiogram import types, Dispatcher, Bot
from app import dp, bot, on_startup, on_shutdown
from data.config import WEBHOOK_PATH, PRETTY_LOGGER
from typing import Dict
from logger import CustomizeLogger


webhook_path = f"/bot/{bot}"
webhook_url = "" + webhook_path




app = FastAPI(title="Main", docs_url=None, redoc_url=None, debug=False)
if PRETTY_LOGGER:
    logger = CustomizeLogger.make_logger()
    app.logger = logger


@app.on_event("startup")
async def on_startup_app():
    await on_startup(dp)


@app.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse(content="<p>Hello world</p>")


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: Dict):
    updater = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    try:
        await dp.process_update(updater)
        return {"ok": True}
    except Exception as e:
        if PRETTY_LOGGER:
            app.logger.error(e)
        return {"ok": False}
        
    

@app.on_event("shutdown")
async def on_shutdown_app():
    await on_shutdown(dp)
    
    
if __name__ == '__main__':
    uvicorn.run(app)
