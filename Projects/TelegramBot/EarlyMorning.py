import telebot
import requests

with open('.git/token.txt', 'r') as file:
    for line in file:
        token = line.strip()
bot = telebot.TeleBot(token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).add('Погода', 'Курсы криптовалют')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Доступные функции: \n\t• прогноз погоды в Светлогорске '
                                      '\n\t• информация о стоимости BTT,\n\t Cardano, Tron',
                     reply_markup=keyboard1)


@bot.message_handler(content_types=["text"])
def weather_message(message):
    if message.text == 'Погода':
        try:
            res = requests.get(
                "http://api.openweathermap.org/data/2.5/find?q=Svyetlahorsk&type=like&APPID"
                "=34d0b12aa3eeabf3a7882862ce916b59",
                params={'units': 'metric', 'lang': 'ru'})
            data = res.json()
            weather = str("Сейчас " + str(data['list'][0]['weather'][0]['description']) +
                          "\nТемпература: " + str(data['list'][0]['main']['temp']) + "°\nОщущается как " +
                          str(data['list'][0]['main']['feels_like']) + "°" +
                          "\nВлажность: " + str(data['list'][0]['main']['humidity']) + "%"
                                                                                       "\nСкорость ветра: " + str(
                data['list'][0]['wind']['speed']) + "м/с")
            bot.send_message(message.chat.id, weather)
        except Exception as e:
            print("Exception (weather):", e)
            pass
    elif message.text == 'Курсы криптовалют':
        bot.send_message(message.chat.id, "Sorry! This feature is coming soon...")
    else:
        bot.send_message(message.chat.id, "Sorry! I can't do this.")
bot.polling(none_stop=True, interval=0)
