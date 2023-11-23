import telebot
from telebot import types
TOKEN="6654749511:AAHL0CGXOhrqTWGrubwAXHsY80XGtRGssv4"

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)     #главное меню
    item1 = types.KeyboardButton('Информация')
    item2 = types.KeyboardButton('Работа у нас')
    item3 = types.KeyboardButton('Каталог товаров')
    item4 = types.KeyboardButton('Профиль')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user)+" Рады приветствовать вас в маркете Bimshot! Выберите кнопку в главном меню", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type=='private':
        if message.text=='Информация':
            bot.send_message(message.chat.id, '...') #текст инфо
        
        elif message.text=='Работа у нас':
            bot.send_message(message.chat.id, '...') #инфо о работе
        
        elif message.text=='Каталог товаров':     #создание каталога товаров
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton('рыба')
            item2=types.KeyboardButton('Мясо')
            item3=types.KeyboardButton('яйца')
            item4=types.KeyboardButton('яблоки')
            item5=types.KeyboardButton('бананы')
            item6=types.KeyboardButton('мандарины')
            item7=types.KeyboardButton('Назад') #кнопка назад
            markup.add(item1,item2,item3,item4,item5,item6,item7)
            bot.send_message(message.chat.id, 'У нас следующий каталог товаров (кнопки снизу). Выберите продукт, чтобы узнать цену, описание и информацию о нем') #и другие товары

            
            
bot.polling(non_stop=True)    
