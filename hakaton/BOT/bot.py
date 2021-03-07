import telebot

bot = telebot.TeleBot('1683245663:AAHAHcFkVT2B2JJ3rXAbQIhv_G20mRIPOsc')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling(none_stop=True, interval=0)
