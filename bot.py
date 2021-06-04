# TODO: Бот для получения фильма с HDrezka
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
import parsing
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"""
    Хелоу 🙈 \nНапиши название фильма/сериала и я найду его 🔍 \n- Например: 'кто я' 🙌\nЕще могу так 💁
/top_series - Получить топ сериалов 🍓
/top_films - Получить топ фильмов 🍇
""")


# Топ 10 популярных фильмов 🙈
@bot.message_handler(commands=['top_films'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Топ 10 популярных фильмов 🙈")
    chat_id = message.chat.id
    result = parsing.get_popular_film()
    i = 0
    for res in result:
        if i > 9:
            break
        # bot.send_message(chat_id, f"{res['title']}. \n {res['year']}. \n",
        #                  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Смотреть фильм', url=res['URL'])]]))
        bot.send_photo(chat_id, res['img'],
                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Смотреть фильм', url=res['URL'])]]))
        i += 1


# Топ 10 популярных сериалов 🧞‍♂️
@bot.message_handler(commands=['top_series'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Топ 10 популярных сериалов 🧞‍♂️")
    chat_id = message.chat.id
    result = parsing.get_popular_series()
    i = 0
    for res in result:
        if i > 9:
            break
        # bot.send_message(chat_id, f"{res['title']}. \n {res['year']}. \n",
        #                  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Смотреть фильм', url=res['URL'])]]))
        bot.send_photo(chat_id, res['img'],
                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Смотреть сериал', url=res['URL'])]]))
        i += 1


# Ищет фильм по названию
@bot.message_handler(content_types=["text"])
def send_anytext(message):
    chat_id = message.chat.id
    result = parsing.get_film(message.text)
    bot.send_message(chat_id, f"По запросу: ' {message.text} ' найдено {int(len(result))} фильмов/сериалов 🙌")
    i = 0
    for res in result:
        if i == len(result):
            break
        # bot.send_message(chat_id, f"{res['title']}. \n {res['year']}. \n",
        #                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Смотреть фильм', url=res['URL'])]]))
        bot.send_photo(chat_id, res['img'],
                         reply_markup=InlineKeyboardMarkup([
                             [InlineKeyboardButton(text='Смотреть трейлер 🧞‍♂️', url=f'https://www.youtube.com/results?search_query={message.text} трейлер')],
                             [InlineKeyboardButton(text='Смотреть фильм 👀', url=res['URL'])]
                         ]))
        i += 1


@bot.callback_query_handler(func=lambda message: True)
def ans(message):
    chat_id = message.message.chat.id


bot.polling()

