import telebot
import requests
from pycoingecko import CoinGeckoAPI

with open('.git/token', 'r') as file:
    tokens = list(file)
cg = CoinGeckoAPI()
bot_token = tokens[0].strip()
weather_token = tokens[1].strip()
bot = telebot.TeleBot(bot_token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).add('Погода', 'Курсы криптовалют')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Доступные функции: \n\t• прогноз погоды в Светлогорске '
                                      '\n\t• информация о стоимости BTT,\n\t Cardano, Tron',
                     reply_markup=keyboard1)


@bot.message_handler(content_types=["text"])
def output_message(message):
    if message.text == 'Погода':
        try:
            res = requests.get(
                f"http://api.openweathermap.org/data/2.5/find?q=Svyetlahorsk&type=like&APPID={weather_token}",
                params={'units': 'metric', 'lang': 'ru'})
            data = res.json()
            weather_message= f"{data['list'][0]['weather'][0]['description'].capitalize()} " \
                             f"\nТемпература: {data['list'][0]['main']['temp']}° " \
                             f"\nОщущается как: {data['list'][0]['main']['feels_like']}° " \
                             f"\nВлажность: {data['list'][0]['main']['humidity']}%" \
                             f"\nСкорость ветра: {data['list'][0]['wind']['speed']}м/с" \
                             f"\nОблачность: {data['list'][0]['clouds']['all']}% "
            bot.send_message(message.chat.id, weather_message)
            if data['list'][0]['rain'] != 'null':
                bot.send_message(message.chat.id, data['list'][0]['rain'])
            if data['list'][0]['snow'] != 'null':
                bot.send_message(message.chat.id, data['list'][0]['snow'])
        except Exception:
            pass
    elif message.text == 'Курсы криптовалют':

        currency = cg.get_price(ids='bittorrent-2,cardano,tron', vs_currencies='usd', include_24hr_change='true')
        currency_message = \
            f"BTT: {currency['bittorrent-2']['usd']} $  || {round(currency['bittorrent-2']['usd_24h_change'], 3)} %" \
            f"\nCardano: {currency['cardano']['usd']} $  || {round(currency['cardano']['usd_24h_change'], 3)} %" \
            f"\nTron: {currency['tron']['usd']} $  || {round(currency['tron']['usd_24h_change'], 3)} %"
        bot.send_message(message.chat.id, currency_message)
    else:
        bot.send_message(message.chat.id, "Sorry! I can't do this.")


bot.polling(none_stop=True, interval=0)
