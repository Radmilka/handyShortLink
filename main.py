from telebot import TeleBot, types
from config import Config

bot = TeleBot(Config.TOKEN.value, parse_mode='html')


main_menu_reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# первый ряд кнопок
main_menu_reply_markup.row(
    types.KeyboardButton(text="1️⃣"), types.KeyboardButton(text="2️⃣")
)
# второй ряд кнопок
main_menu_reply_markup.row(
    types.KeyboardButton(text="5️⃣"), types.KeyboardButton(text="🔟")
)


# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_message_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    # не забываем прикрепить объект клавиатуры к сообщению
    bot.send_message(
        chat_id=message.chat.id,
        text="Привет!\nЭто бот для генерации тестовых пользователей. " \
             "Выбери сколько пользователей тебе нужно 👇🏻",
        reply_markup=main_menu_reply_markup
    )


# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # определяем количество тестовых пользователей
    # или отправляем ошибку
    payload_len = 0
    if message.text == "1️⃣":
        payload_len = 1
    elif message.text == "2️⃣":
        payload_len = 2
    elif message.text == "5️⃣":
        payload_len = 5
    elif message.text == "🔟":
        payload_len = 10
    else:
        bot.send_message(chat_id=message.chat.id, text="Не понимаю тебя :(")
        return

    # сериализуем данные в строку

    # отправляем результат
    bot.send_message(
        chat_id=message.chat.id,
        text=f"Данные {payload_len} тестовых пользователей:\n<code>" \
             f"{None}</code>"
    )
    bot.send_message(
        chat_id=message.chat.id,
        text="Если нужны еще данные, можешь выбрать еще раз 👇🏻",
        reply_markup=main_menu_reply_markup
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()