import telebot
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "7975251424:AAFs3S9tSritY3nnsw4zv43E9bTeBV2-aFg"
WEBAPP_URL = "https://harshad444.github.io/hamster-game-bot/"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("▶️ Play Hamster Game", web_app=WebAppInfo(url=WEBAPP_URL)))
    bot.send_message(message.chat.id, "Welcome to Hamster Game!", reply_markup=markup)

bot.polling()
