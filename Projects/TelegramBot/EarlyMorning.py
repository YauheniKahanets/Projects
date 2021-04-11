#import telebot
with open('.git/token.txt', 'r') as file:
    for line in file:
        token = line.strip()
#bot = telebot.TeleBot(token)
print(token)