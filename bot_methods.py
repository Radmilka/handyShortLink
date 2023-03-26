import logging

from telebot import TeleBot, types
from config import Config
from clck_api import shorten_url
from validators import is_link_ok

bot = TeleBot(Config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Напишите мне URL-ссылку:) В ответ я пришлю ее удобную короткую версию. Пример ссылки для меня: \nhttps://www.google.com/?hl=ru "
    )


@bot.message_handler()
def message_handler(message: types.Message):
    logging.log(
        level=logging.INFO,
        msg=f"Пользователь c uid '{message.chat.id}' прислал сообщение: '{message.text}' messageId: '{message.message_id}'"
    )

    if message.text and is_link_ok(message.text):
        text = shorten_url(message.text)
    else:
        text = "Источник ссылки не найден. Проверьте, правильно ли вы вводите данные:)"

    bot.send_message(chat_id=message.chat.id, text=text)


def start():
    bot.infinity_polling()
