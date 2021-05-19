import telebot
from telebot import types
import config

token = config.token
TOKEN = token
bot = telebot.TeleBot(TOKEN)



import json




@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Я студент', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Я лаборант', callback_data=2))

    bot.send_message(message.chat.id, text="Здравствуйте. Добро пожаловать в лабораторию. Авторизуйтесь в системе:", reply_markup=markup)




@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Авторизация...')
    if call.data == '1':
        answer = 'Добро пожаловать,студент. У вас есть доступ к базовому набору реактивов. Введите "взять реактивы", чтобы получить список доступных'
        image = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fexpert-stroypro.ru%2Fwp-content%2Fuploads%2F2020%2F03%2Fstroitelnaya-laboratoriya.jpg&f=1&nofb=1'
        bot.send_photo(call.message.chat.id, image)

    elif call.data == '2':
        answer = 'Вы зашли как лаборант. У вас есть доступ к складу реактивов. Введите "добавить реактивы", чтобы пополнить запасы лаборатории'
        image = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fchemistry-chemists.com%2FN6_2011%2FU7%2FLaboratory-31.jpg&f=1&nofb=1'
        bot.send_photo(call.message.chat.id, image)

    elif call.data == '3':
        with open('strings.json') as fp:
            d = json.load(fp)
        if d['H2SO4'] > 0:
            answer = 'Вы взяли 1 эквивалент H2SO4'
            
            d['H2SO4'] -= 1 
            with open('strings.json', 'w') as fp:
                json.dump(d, fp)
        else:
            answer = 'Это вещество закончилось'
    
    elif call.data == '4':
        with open('strings.json') as fp:
            d = json.load(fp)
        if d['HCl'] > 0:
            answer = 'Вы взяли 1 эквивалент HCl'
            d['HCl'] -= 1 
            with open('strings.json', 'w') as fp:
                json.dump(d, fp)
        else:
            answer = 'Это вещество закончилось'
    
    elif call.data == '5':
        with open('strings.json') as fp:
            d = json.load(fp)
        if d['KOH'] > 0:
            answer = 'Вы взяли 1 эквивалент KOH'
            d['KOH'] -= 1 
            with open('strings.json', 'w') as fp:
                json.dump(d, fp)
        else:
            answer = 'Это вещество закончилось'
        
    
    elif call.data == '6':
        with open('strings.json') as fp:
            d = json.load(fp)
        if d['NaCl'] > 0:
            answer = 'Вы взяли 1 эквивалент NaCl'
            d['NaCl'] -= 1 
            with open('strings.json', 'w') as fp:
                json.dump(d, fp)
        else:
            answer = 'Это вещество закончилось'

    elif call.data == '7':
        answer = 'Вы добавили 1 эквивалент H2SO4'
        with open('strings.json') as fp:
            d = json.load(fp)
        d['H2SO4'] += 1 
        with open('strings.json', 'w') as fp:
            json.dump(d, fp)
    
    elif call.data == '8':
        answer = 'Вы добавили 1 эквивалент HСl'
        with open('strings.json') as fp:
            d = json.load(fp)
        d['HCl'] += 1 
        with open('strings.json', 'w') as fp:
            json.dump(d, fp)

    elif call.data == '9':
        answer = 'Вы добавили 1 эквивалент KOH'
        with open('strings.json') as fp:
            d = json.load(fp)
        d['KOH'] += 1 
        with open('strings.json', 'w') as fp:
            json.dump(d, fp)

    elif call.data == '10':
        answer = 'Вы добавили 1 эквивалент NaСl'
        with open('strings.json') as fp:
            d = json.load(fp)
        d['NaCl'] += 1 
        with open('strings.json', 'w') as fp:
            json.dump(d, fp)

    
    
    

    bot.send_message(call.message.chat.id, answer)
    
    
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)






@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'взять реактивы':
        with open('strings.json') as fp:
            d = json.load(fp)
        
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='H2SO4 ' + str(d["H2SO4"]), callback_data=3))
        markup.add(telebot.types.InlineKeyboardButton(text='HCl ' + str(d["HCl"]), callback_data=4))
        markup.add(telebot.types.InlineKeyboardButton(text='KOH ' + str(d["KOH"]), callback_data=5))
        markup.add(telebot.types.InlineKeyboardButton(text='NaCl ' + str(d["NaCl"]), callback_data=6))
        bot.send_message(message.chat.id, text="Выберете реактив, который хотите взять", reply_markup=markup)
    
    if message.text.lower() == 'добавить реактивы':
        with open('strings.json') as fp:
            d = json.load(fp)
        
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='+H2SO4 ' + str(d["H2SO4"]), callback_data=7))
        markup.add(telebot.types.InlineKeyboardButton(text='+HCl ' + str(d["HCl"]), callback_data=8))
        markup.add(telebot.types.InlineKeyboardButton(text='+KOH ' + str(d["KOH"]), callback_data=9))
        markup.add(telebot.types.InlineKeyboardButton(text='+NaCl ' + str(d["NaCl"]), callback_data=10))
        bot.send_message(message.chat.id, text="Выберете реактив, который хотите добавить", reply_markup=markup)

    else:
        if (message.text.lower() != 'взять реактивы') and (message.text.lower() != 'добавить реактивы'): 
            bot.send_message(message.chat.id, text= "У меня есть команды /start, взять реактивы и добавить реактивы")


            






bot.polling()