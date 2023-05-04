import telebot
from extensions import  APIException, CryptoConverter, keys

TOKEN = "5859319186:AAEd0vrcCMbmZ0OVJd6APkxjivOHYa9zHb0"


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты>\
<в какую валюту перевести>\
<колличество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
     text = 'Доступные валюты:'
     for key in keys.keys():
         text = '\n'.join((text, key,))  # каждая новая валюта переносится на строчку в низ
     bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        price = message.text.split(" ")
        if len(price) != 3:
            raise APIException('Слишком много параметров')
        quote, base, amount = price
        total_base = CryptoConverter.convert(quote,base,amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Неудалось обработать команду\n{e}')
    else:
        text = f'{amount} {quote} - {total_base * float(amount)} {base}'
        bot.send_message(message.chat.id, text)


bot.polling()



