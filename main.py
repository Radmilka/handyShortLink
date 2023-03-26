import logging

from telebot import TeleBot, types
from config import Config
from clck_api import shorten_url
from validators import is_link_ok

bot = TeleBot(Config.TOKEN.value, parse_mode='html')


@bot.message_handler(commands=['start'])
def start_message_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Привет!\nНапиши мне ссылку, и я верну тебе удобную короткую ссылку:) "
    )


@bot.message_handler()
def message_handler(message: types.Message):
    logging.log(
        level=logging.DEBUG,
        msg=f"Пользователь c uid {message.id} прислал сообщение {message.text} {message.message_id}"
    )

    if message.text and is_link_ok(message.text):
        text = shorten_url(message.text)
    else:
        text = "Не понимаю тебя :("

    bot.send_message(chat_id=message.chat.id, text=text)


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    logging.basicConfig(level=Config.LOG_LEVEL.value)
    main()
