import telebot
import requests
from pycoingecko import CoinGeckoAPI
import urllib.request
from pprint import pprint
from html_table_parser.parser import HTMLTableParser

with open('.git/token', 'r') as file:
    tokens = list(file)
cg = CoinGeckoAPI()
bot_token = tokens[0].strip()
weather_token = tokens[1].strip()
bot = telebot.TeleBot(bot_token)
currency = cg.get_price(ids='bittorrent-2,cardano,tron', vs_currencies='usd', include_24hr_change='true')
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).add('Погода', 'Курсы криптовалют',
                                                                        'Стоимость топлива')
keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).add('BitTorrent', 'Tron', 'Cardano')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Доступные функции: \n\t• прогноз погоды в Светлогорске '
                                      '\n\t• информация о стоимости криптовалют'
                                      '\n\t• стоимость топлива',
                     reply_markup=keyboard1)


@bot.message_handler(content_types=["text"])
def output_message(message):
    if message.text == 'Погода':
        try:
            res = requests.get(
                f"http://api.openweathermap.org/data/2.5/find?q=Svyetlahorsk&type=like&APPID={weather_token}",
                params={'units': 'metric', 'lang': 'ru'})
            data = res.json()
            weather_message = f"{data['list'][0]['weather'][0]['description'].capitalize()} " \
                              f"\nТемпература: {data['list'][0]['main']['temp']}° " \
                              f"\nОщущается как: {data['list'][0]['main']['feels_like']}° " \
                              f"\nВлажность: {data['list'][0]['main']['humidity']}%" \
                              f"\nСкорость ветра: {data['list'][0]['wind']['speed']}м/с" \
                              f"\nОблачность: {data['list'][0]['clouds']['all']}% "
            bot.send_message(message.chat.id, weather_message)
            if data['list'][0]['rain'] != 'null':
                rain = f"Вероятность дождя в ближайший час {round(data['list'][0]['rain']['1h'] * 100)}%"
                bot.send_message(message.chat.id, rain)
                bot.send_message(message.chat.id, "Возьмите зонт!")
            if data['list'][0]['snow'] != 'null':
                snow = f"Вероятность снега в ближайший час {round(data['list'][0]['snow']['1h'] * 100)}%"
                bot.send_message(message.chat.id, snow)
                bot.send_message(message.chat.id, "Лучше никуда не идти!")
        except Exception:
            pass
    elif message.text == 'Курсы криптовалют':
        bot.send_message(message.chat.id, 'Выберите криптовалюту!', reply_markup=keyboard2)
    elif message.text == 'BitTorrent':
        crypto = f"BTT: {currency['bittorrent-2']['usd']} $   {round(currency['bittorrent-2']['usd_24h_change'], 3)} %"
        bot.send_message(message.chat.id, crypto, reply_markup=keyboard1)
    elif message.text == 'Cardano':
        crypto = f"Cardano: {currency['cardano']['usd']} $   {round(currency['cardano']['usd_24h_change'], 3)} %"
        bot.send_message(message.chat.id, crypto, reply_markup=keyboard1)
    elif message.text == 'Tron':
        crypto = f"Tron: {currency['tron']['usd']} $   {round(currency['tron']['usd_24h_change'], 3)} %"
        bot.send_message(message.chat.id, crypto, reply_markup=keyboard1)
    elif message.text == 'Стоимость топлива':
        def url_get_contents():
            req = urllib.request.Request(url='https://azs.belorusneft.by/sitebeloil/ru/center/azs/center'
                                             '/fuelandService/price/')
            f = urllib.request.urlopen(req)
            return f.read()

        xhtml = url_get_contents().decode('utf-8')
        p = HTMLTableParser()
        p.feed(xhtml)
        prices = p.tables[0]
        fuel = list()
        price = list()
        fuel_price = ''
        for i in range(len(prices)):
            if i % 2 == 0:
                for j in range(len(prices[i])):
                    fuel.append(prices[i][j].strip(','))
            else:
                for j in range(len(prices[i])):
                    price.append(prices[i][j].strip(','))
        for i in range(len(fuel)):
            fuel_price += (fuel[i] + " : " + price[i] + '\n')
        bot.send_message(message.chat.id, fuel_price)
    else:
        bot.send_message(message.chat.id, "Sorry! I can't do this.")


bot.polling(none_stop=True, interval=0)
