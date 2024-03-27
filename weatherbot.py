import requests
import telebot
import json

bot = telebot.TeleBot('YOUR_TOKEN')
API = 'YOUR_API'  # Ключ API OPENWEATHER

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привіт, я бот для відправки погоди! Радий буду тобі допомогти! Введи назву свого міста!')

@bot.message_handler(content_types=['text'])  # Тип, який відстежує, що відправив користувач
def text(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')# USING https://openweathermap.org/api/one-call-3
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
