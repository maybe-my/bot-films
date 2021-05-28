# TODO: Бот для получения фильма с HDrezka
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import parsing
import pyowm
import telebot
from pyowm.utils.config import get_default_config
from telebot import types

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('d03f84421e1675a1a3fb23d575ebeb4b', config_dict)
bot = telebot.TeleBot("809214932:AAG2PCQzItdnGsOlmM8aq-nxQEA2vrikxpI", parse_mode=None)


# list_games
def list_games(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Блэджек", callback_data="game{0}"))
    keyboard.add(types.InlineKeyboardButton(text='⬅ Вернуться в главное меню', callback_data="wallet_return"))
    return keyboard


# Keyboard
def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    games = types.KeyboardButton('Games 🎲')
    weather = types.KeyboardButton('Weather ⛅️')
    markup.add(games, weather)
    return markup


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Хелоу ♥")


@bot.message_handler(content_types=["text"])
def send_anytext(message):
    chat_id = message.chat.id
    result = parsing.get_film(message.text)
    bot.send_message(chat_id, f"По запросу: '{message.text}' найдено {len(result)} фильмов/сериалов.")
    for res in result:
        bot.send_message(chat_id, f"{res['title']}. \n {res['year']}. \n",
                         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Смотреть фильм', url=res['URL'])]]))
        bot.send_photo(chat_id, res['img'])


@bot.callback_query_handler(func=lambda message: True)
def ans(message):
    chat_id = message.message.chat.id


bot.polling()

