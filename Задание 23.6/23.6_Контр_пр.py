import telebot
from extensions import  APIException, CryptoConverter
from config import TOKEN, keys


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Привет! Я Бот-Конвертер валют и я могу:\n - Показать\
    список доступных валют через команду /values  \
    - Вывести конвертацию валюты через команду <имя \
    валюты> <в какую валюту перевести> <количество\
    переводимой валюты>'

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



