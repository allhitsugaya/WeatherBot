import requests
import telebot
import json

bot = telebot.TeleBot('6341780918:AAE01HZagc0GHHqSXu8zWh9hyUN2LfCnRVU')
API = 'd323085f7c89aa81472d0601634ca9bc'  # Ключ API OPENWEATHER

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привіт, я бот для відправки погоди! Радий буду тобі допомогти! Введи назву свого міста!')

@bot.message_handler(content_types=['text'])  # Тип, який відстежує, що відправив користувач
def text(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f"Зараз погода: {temp}°C")
        image = 'image.jpg' if temp > 5.0 else 'image1.jpg'
        with open(image, 'rb') as file:
            bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, "Місто вказано невірно")

bot.polling(none_stop=True)
