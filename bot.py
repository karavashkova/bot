import telegram
from telegram import keyboardbutton
import config

token = config.token
bot = telegram.Bot(token)


markup = telegram.ReplyKeyboardMarkup(
    keyboard=[['Зарегистрироваться']]
)



def registration():
    global s
    with open(s, 'a+') as file:
        file.write('1 \n')

recognize = {
    'Зарегистрироваться': [bot.sendMessage, 'Введите свой курс'],
    '1': registration,
    'f': [bot.sendMessage, 'fff']
}
 



def get_last_update_id(updates):
    id_list = list() # пустой список ID апдейтов
    for update in updates: # для каждого апдейта 
        id_list.append(update["update_id"]) # заносим в список его ID
    return(max(id_list)) # возвращаем последний


def main():
    last_update_id = None
    while True:
        updates = bot.getUpdates(last_update_id, timeout=100)
        if len(updates) > 0:
            last_update_id = get_last_update_id(updates) + 1
            for update in updates: # сообщения могут приходить быстро, быстрее, чем работает код
                last_message = update["message"] # взяли из него сообщение
                last_message_text = last_message['text'] # из сообщения - текст
                last_chat_id =  last_message['chat']['id']
                s = str(last_chat_id)+'.txt'
                with open(s, 'a+') as file:
                    file.seek(0, 2)
                    file.write(str(last_message_text) + "\n")
                if  recognize.get(last_message_text):
                    function = recognize[last_message_text][0]
                    arg = recognize[last_message_text][1]
                    function(last_chat_id, arg)
                else:
                    bot.sendMessage(last_chat_id, # написавшему
                                    "zdarova broo!") # включаем кнопки

if __name__ == '__main__':
    main()

