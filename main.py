import telebot
from telebot import types
import time

# Main tokens here -->
bot = telebot.TeleBot('1870221472:AAEwNPg5pOyz35B75hQ17eLundIYB0mAf0U')

# Метод для получения текстовых сообщений
@bot.message_handler(content_types=['text']) # https://github.com/eternnoir/pyTelegramBotAPI
def get_text_messages(message):
    if message.text == "/start":
        # STICKER
        stic = open('tmp/Stickers/file_48037426.webp', 'rb')
        bot.send_sticker(message.from_user.id, stic)
        time.sleep(1)

        bot.send_message(message.from_user.id, "Вас приветствует бот автосервиса ИП \"Деминов А.М.\"!✋🏼")
        time.sleep(0.5)
        bot.send_message(message.from_user.id, "Хотели бы вы посмотреть наш список услуг? Введите /service")
        bot.register_next_step_handler(message, get_job) #следующий шаг – функция get_job
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")


def get_job(message):
    if message.text == "/service":
        # STICKER
        stic = open('tmp/Stickers/file_48037431.webp', 'rb')
        bot.send_sticker(message.from_user.id, stic)

        bot.send_message(message.from_user.id, "Основные виды деятельности ИП \"Деминов А.М.\": \n ☑️ Техническое обслуживание и ремонт автотранспортных средств;\n ☑️ Торговля автомобильными деталями, узлами и принадлежностями.")
        time.sleep(2)
        keyboard = types.InlineKeyboardMarkup() # наша клавиатура
        key_ServiceJob = types.InlineKeyboardButton(text='🔧Тех. обслуживание и ремонт ТС', callback_data='ServiceJob')
        keyboard.add(key_ServiceJob)
        key_Market = types.InlineKeyboardButton(text='🚗Торговля автомобильными деталями, узлами и принадлежностями', callback_data='Market')
        keyboard.add(key_Market)

        question = 'Что именно вас интересует?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

def service(call):
    if call.data == 'ServiceJob':
        keyboard = types.InlineKeyboardMarkup() # клавиатура основных опций
        key_BodyWork = types.InlineKeyboardButton(text='Кузовной цех.', callback_data='BodyWork')
        key_Wash = types.InlineKeyboardButton(text='Мойка и химчисика.', callback_data='Wash')
        key_Repair = types.InlineKeyboardButton(text='Цех ТО и ремонта авто.', callback_data='Repair')
        key_TireService = types.InlineKeyboardButton(text='Шиномонтаж и ремонт колес.', callback_data='TireService')
        key_Electician = types.InlineKeyboardButton(text='Ремонт электрики', callback_data='Electrician')
        keyboard.add(key_BodyWork)
        keyboard.add(key_Wash)
        keyboard.add(key_Repair)
        keyboard.add(key_TireService)
        keyboard.add(key_Electician)

        bot.send_message(call.message.chat.id, 'Выберите пожалуйста область услуги 🔧', reply_markup=keyboard)
    
    

# Обработка событий кастомной клавиатуры
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "ServiceJob": #call.data это callback_data, которую мы указали при объявлении кнопки
        #код сохранения данных, или их обработки
        

        # keyboard = types.InlineKeyboardMarkup() # клавиатура основных опций
        # key_BodyWork = types.InlineKeyboardButton(text='Кузовной цех.', callback_data='BodyWork')
        # key_Wash = types.InlineKeyboardButton(text='Мойка и химчисика.', callback_data='Wash')
        # key_Repair = types.InlineKeyboardButton(text='Цех ТО и ремонта авто.', callback_data='Repair')
        # key_TireService = types.InlineKeyboardButton(text='Шиномонтаж и ремонт колес.', callback_data='TireService')
        # key_Electician = types.InlineKeyboardButton(text='Ремонт электрики', callback_data='Electrician')
        # keyboard.add(key_BodyWork)
        # keyboard.add(key_Wash)
        # keyboard.add(key_Repair)
        # keyboard.add(key_TireService)
        # keyboard.add(key_Electician)

        bot.send_message(call.message.chat.id, 'Отлично! Вы выбрали тех.обслуживание')
        time.sleep(1)
        service(call)

    if call.data == "BodyWork":
        photo = open('tmp/Sales.PNG', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        file_id = 'sales1'
        bot.send_photo(call.message.chat.id, file_id)

    elif call.data == "Market":
        bot.send_message(call.message.chat.id, 'Отлично! Вы выбрали наш магазин деталей!')





# Теперь наш бот будет постоянно спрашивать у сервера Телеграмма «Мне кто-нибудь написал?»
bot.polling(none_stop=True, interval=0)
