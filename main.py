from telebot import TeleBot, types
from config import Config
from clck_api import shorten_url

bot = TeleBot(Config.TOKEN.value, parse_mode='html')


# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_message_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    # не забываем прикрепить объект клавиатуры к сообщению
    bot.send_message(
        chat_id=message.chat.id,
        text="Привет!\nНапиши мне ссылку, и я верну тебе удобную короткую ссылку:) "
    )


# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    if message.text:
        text = shorten_url(message.text)
    else:
        text = "Не понимаю тебя :("

    bot.send_message(chat_id=message.chat.id, text=text)


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
