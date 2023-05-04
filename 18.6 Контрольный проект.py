import telebot

TOKEN = "5859319186:AAEd0vrcCMbmZ0OVJd6APkxjivOHYa9zHb0"

bot = telebot.TeleBot(TOKEN)

@bot.message_handker()
def echo_test(message: telebot.tupe.Message):
    bot.send_message(message.chat.id, "Hello")