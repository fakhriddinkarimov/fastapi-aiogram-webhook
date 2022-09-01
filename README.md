# fastapi-aiogram-webhook

**FastAPI** dan foydalanib **aiogram** telegram botlarni webhook qilish uchun template.

## Dastlabki sozlash ishlari:

### Python kutubxonlarini o'rnatib oling:
```bash
$ pip install -r requirements.txt
```

### Enviroment variables
Namunadagi `.env.dist` faylidan nusxa `.env` fayl yaratib undagi __ADMINS__, __BOT_TOKEN__, __WEB_DOMAIN__, __PRETTY_LOGGER__ o'zgaruvchilarini kiriting:

```bash
$ cp .env.dist .env
$ nano .env
```

## Ishga tushirish
Ishga tushirish oddiygina `uvicorn` yordamida bo'ladi.

```bash
$ uvicorn main:app --port 8000 --reload
```

