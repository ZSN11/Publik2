import telebot

TOKEN = "5859319186:AAEd0vrcCMbmZ0OVJd6APkxjivOHYa9zHb0 "

bot = telebot.TeleBot(TOKEN)

@bot.message.handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hello')