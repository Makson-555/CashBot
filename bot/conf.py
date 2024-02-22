from time import sleep

import telebot
from django.conf import settings

TOKEN = '6859339625:AAG9BFVy-MDEYYPZATXQx4q-FYJyNrCXR34'

# Ініціалізуємо телеграм-бота
bot = telebot.TeleBot(TOKEN)


# Встановлюємо вебхук
bot.remove_webhook()
bot.set_webhook(url=settings.WEBHOOK_URL)