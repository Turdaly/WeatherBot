import telebot

bot = telebot.TeleBot('5772354431:AAEUpfbDMA9OLua120Ie2INJ3vurL3vst1I')

@bot.message_handler(commands=['start'])
def startBot(message):
    bot.send_message(message.chata.id, 'Hello this is weather bot. \n'
                                       'you can use command /current'
                                       'to takecurrent weather.')

@bot.message_handler(commands=['current'])
def currentWeather(message):
    bot.send_message(message.chata.id, 'what is your city?:')


def getCurentWeather(message):
    city = message.text


def futureWeather(message):
    pass


bot.polling(non_stop=True, interval=0)
