import telebot
import datetime
from telebot import types
bot = telebot.TeleBot('5501621331:AAFCpjPj8cC7Pr1KP-L2uebtasBlvRgaDn4')
nowTime = datetime.datetime.now().strftime("%H.%M")
day = datetime.datetime.now().strftime('%A')
@bot.message_handler(content_types=['text'])
def getPed(message):
    global nowTime
    if message.text == 'все команды' or message.text == 'вк':
        bot.send_message(message.chat.id, 'All our commands!\n'
                                          '1. Расписания(Р)\n'
                                          '2. Сабақ басталу уақыты(Сб)\n'
                                          '3. Сабақ аяталу уақыты(Са)\n')
        bot.register_next_step_handler(message, getPed)
    elif message.text == 'Р':
        message.text = day
        getSchedule(message)

    elif message.text == 'Расписания':
        getScheduleButtle(message)
    elif message.text == 'Сабақ нешеде басталады' or message.text == 'Сб' or message.text == '2':
        if nowTime[0:1] == '0':
            nowTime = nowTime[1:5]
        message.text = nowTime
        getTimeStart(message)
    elif message.text == 'Сабақ нешеде аяқталады' or message.text == 'Са' or message.text == '3':
        if nowTime[0:1] == '0':
            nowTime = nowTime[1:5]
        message.text = nowTime
        getTimeFinish(message)


def getSchedule(message):
    if message.text == 'Monday':
        bot.send_message(message.chat.id, 'Есеп арн.диск құр(пр) 11.40-12.30 \n'
                                          'Есеп арн.диск құр(пр) 12.40-13.30\n'
                                          'Ықтималдылық теория(д) 13.40-14.30\n'
                                          'Физика(пр) 15.50-16.40\n'
                                          'Физика(пр) 16.50 - 17.40')

    elif message.text == 'Tuesday':
        bot.send_message(message.chat.id,'Физика(д) 14.40-15.30\n'
                                          'Дене шынықтыру(пр) 15.50-16.40\n'
                                          'Дене шынықтыру(пр) 16.50 - 17.40')


    elif message.text == 'Wednesday':
        bot.send_message(message.chat.id,'Кәсіпкерлік(д) 13.40-14.30\n'
                                         'Кәсіпкерлік(д) 14.40-15.30\n'
                                          'ООП(пр) 15.50-16.40\n'
                                          'ООП(д) 16.50 - 17.40')

    elif message.text == 'Thursday':
        bot.send_message(message.chat.id,'Академиялық жазу(д) 12.40-13.30\n'
                                          'Окошка 13.40-14.30\n'
                                          'Академиялық жазу(пр) 15.50-16.40\n')

    elif message.text == 'Friday':
        bot.send_message(message.chat.id,'Есептеуге арн.диск(д) 13.40-14.30\n'
                                         'Ықтималдылық т(пр) 14.40-15.30\n'
                                          'ООП(д) 15.50-16.40\n'
                                          'Окошка 16.50 - 17.40\n'
                                         'Кәсіпкерлік(пр) 17.50-18.40')
    bot.register_next_step_handler(message, getPed)

def getScheduleButtle(message):
    keyboard = types.InlineKeyboardMarkup()
    keyMonday = types.InlineKeyboardButton('Дүйсенбі', callback_data='monday')
    keyTuesday = types.InlineKeyboardButton('Сейсенбі', callback_data='tuesday')
    keyWednesday = types.InlineKeyboardButton('Сәрсенбі', callback_data='wednesday')
    keyThursday = types.InlineKeyboardButton('Бейсенбі', callback_data='thursday')
    keyFriday = types.InlineKeyboardButton('Жұма', callback_data='friday')
    keyboard.add(keyMonday,keyTuesday, keyWednesday, keyThursday, keyFriday)
    bot.send_message(message.chat.id, 'Қай күннің сабақ кестесі керек?', reply_markup=keyboard)
    if message.text == '1':
        bot.send_message(message.chat.id, 'Есеп арн.диск құр(пр) 11.40-12.30 \n'
                                          'Есеп арн.диск құр(пр) 12.40-13.30\n'
                                          'Ықтималдылық теория(д) 13.40-14.30\n'
                                          'Физика(пр) 15.50-16.40\n'
                                          'Физика(пр) 16.50 - 17.40')

    elif message.text == '2':
        bot.send_message(message.chat.id,'Физика(д) 14.40-15.30\n'
                                          'Дене шынықтыру(пр) 15.50-16.40\n'
                                          'Дене шынықтыру(пр) 16.50 - 17.40')


    elif message.text == '3':
        bot.send_message(message.chat.id,'Кәсіпкерлік(д) 13.40-14.30\n'
                                         'Кәсіпкерлік(д) 14.40-15.30\n'
                                          'ООП(пр) 15.50-16.40\n'
                                          'ООП(д) 16.50 - 17.40')

    elif message.text == '4':
        bot.send_message(message.chat.id,'Академиялық жазу(д) 12.40-13.30\n'
                                          'Окошка 13.40-14.30\n'
                                          'Академиялық жазу(пр) 15.50-16.40\n')

    elif message.text == '5':
        bot.send_message(message.chat.id,'Есептеуге арн.диск(д) 13.40-14.30\n'
                                         'Ықтималдылық т(пр) 14.40-15.30\n'
                                          'ООП(д) 15.50-16.40\n'
                                          'Окошка 16.50 - 17.40\n'
                                         'Кәсіпкерлік(пр) 17.50-18.40')
    bot.register_next_step_handler(message, getPed)
@bot.callback_query_handler(func=lambda call:True)
def callbackHandler(call):
    if call.data == 'monday':
        bot.send_message(call.message.chat.id, 'Есеп арн.диск құр(пр) 11.40-12.30 \n'
                                          'Есеп арн.диск құр(пр) 12.40-13.30\n'
                                          'Ықтималдылық теория(д) 13.40-14.30\n'
                                          'Физика(пр) 15.50-16.40\n'
                                          'Физика(пр) 16.50 - 17.40')

    elif call.data == 'tuesday':
        bot.send_message(call.message.chat.id, 'Физика(д) 14.40-15.30\n'
                                          'Дене шынықтыру(пр) 15.50-16.40\n'
                                          'Дене шынықтыру(пр) 16.50 - 17.40')

    elif call.data == 'wednesday':
        bot.send_message(call.message.chat.id, 'Кәсіпкерлік(д) 13.40-14.30\n'
                                         'Кәсіпкерлік(д) 14.40-15.30\n'
                                          'ООП(пр) 15.50-16.40\n'
                                          'ООП(д) 16.50 - 17.40')

    elif call.data == 'thursday':
        bot.send_message(call.message.chat.id, 'Академиялық жазу(д) 12.40-13.30\n'
                                          'Окошка 13.40-14.30\n'
                                          'Академиялық жазу(пр) 15.50-16.40\n')

    elif call.data == 'friday':
        bot.send_message(call.message.chat.id, 'Есептеуге арн.диск(д) 13.40-14.30\n'
                                         'Ықтималдылық т(пр) 14.40-15.30\n'
                                          'ООП(д) 15.50-16.40\n'
                                          'Окошка 16.50 - 17.40\n'
                                         'Кәсіпкерлік(пр) 17.50-18.40')

    bot.register_next_step_handler(call.message, getPed)



def getTimeFinish(message):
    global day
    if day == 'Monday':
        finishTime = [12.30, 13.30, 14.30, 16.40, 17.40]
        time = float(message.text)
        for i in finishTime:
            if time < i:
                bot.send_message(message.chat.id, str(i) + '0')
                break

    elif day == 'Tuesday':
        finishTime = [15.30, 16.40, 17.40]
        time = float(message.text)
        for i in finishTime:
            if time < i:
                bot.send_message(message.chat.id, str(i) + '0')
                break

    elif day == 'Wednesday':
        finishTime = [14.30, 15.30, 16.40, 17.40]
        time = float(message.text)
        for i in finishTime:
            if time < i:
                bot.send_message(message.chat.id, str(i) + '0')
                break

    elif day == 'Thursday':
        finishTime = [13.30, 14.30, 16.40,]
        time = float(message.text)
        for i in finishTime:
            if time < i:
                bot.send_message(message.chat.id, str(i) + '0')
                break

    elif day == 'Friday':
        finishTime = [14.30, 15.30, 16.40, 17.40, 18.40]
        time = float(message.text)
        for i in finishTime:
            if time < i:
                bot.send_message(message.chat.id, str(i) + '0')
                break
    bot.register_next_step_handler(message, getPed)

def getTimeStart(message):
    global day
    time = float(message.text)
    if day == 'Monday':
        startTime = [11.40, 12.40, 13.40, 15.50, 16.50]
        for i in startTime:
            if time < i:
                bot.send_message(message.chat.id, str(i) + '0')
                break

    elif day == 'Tuesday':
        startTime = [14.40, 15.50, 16.50]
        for i in startTime:
            if time < i:
                bot.send_message(message.chat.id, str(i) + '0')
                break

    elif day == 'Wednesday':
        startTime = [13.40, 14.40, 15.50, 16.50]
        for i in startTime:
            if time < i:
                bot.send_message(message.chat.id, str(i) + '0')
                break

    elif day == 'Thursday':
        startTime = [12.40, 13.40, 14.40, 15.50]
        for i in startTime:
            if time < i:
                bot.send_message(message.chat.id, str(i) + '0')
                break

    elif day == 'Friday':
        startTime = [13.40, 14.40, 15.50, 17.50]
        for i in startTime:
            if time < i:
                bot.send_message(message.chat.id, str(i) + '0')
                break
    bot.register_next_step_handler(message, getPed)


bot.polling(non_stop=True, interval=0)


