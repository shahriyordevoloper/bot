import telebot
from telebot import TeleBot
from telebot import types
import requests
from bs4 import BeautifulSoup
API_TOKEN = '6192191641:AAGfWZQF5A6MiSJluYLSvarDKbm-s8rhyX4'

bot = telebot.TeleBot(API_TOKEN)



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    
    url =  f'https://obhavo.uz/{message.text}'
    data = requests.get(url)
    content = BeautifulSoup(data.content,'html.parser')

    today = content.find('div',class_='current-forecast')
    # today = today.strong.text

    day1 = content.select_one(selector='body > div.container > div.grid-2.cont-block > table > tbody > tr:nth-child(2) > td.weather-row-forecast > span.forecast-day')
    day2 = content.select_one(selector='body > div.container > div.grid-2.cont-block > table > tbody > tr:nth-child(3) > td.weather-row-forecast > span.forecast-day')
    day3 = content.select_one(selector='body > div.container > div.grid-2.cont-block > table > tbody > tr:nth-child(4) > td.weather-row-forecast > span.forecast-day')
    day4 = content.select_one(selector='body > div.container > div.grid-2.cont-block > table > tbody > tr:nth-child(5) > td.weather-row-forecast > span.forecast-day')
    day5 = content.select_one(selector='body > div.container > div.grid-2.cont-block > table > tbody > tr:nth-child(6) > td.weather-row-forecast > span.forecast-day')
    day6 = content.select_one(selector='body > div.container > div.grid-2.cont-block > table > tbody > tr:nth-child(7) > td.weather-row-forecast > span.forecast-day')
    day7 = content.select_one(selector='body > div.container > div.grid-2.cont-block > table > tbody > tr:nth-child(8) > td.weather-row-forecast > span.forecast-day')


    # for x in table:
    #     print(x.findChildren('th')[0] )




    bot.reply_to(message,f'{day1}\n{day2}\n{day3}\n{day4}\n{day5}\n{day6}\n{day7}')


bot.infinity_polling()
