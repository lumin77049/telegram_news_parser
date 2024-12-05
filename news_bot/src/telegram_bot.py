import os
import pandas
import telebot
from dotenv import load_dotenv, dotenv_values

load_dotenv()
API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)

def post_articles(message):
    print("posting articles")
    url_list = pandas.read_csv('article_urls.csv', header=None, index_col=False)

    for i in url_list:
        bot.send_message(message.chat.id, url_list[i]);
        print("\nposting: " + url_list[i]);

def start_scrape(message):
    print("starting scrape")
    os.system("python aggregator.py")
    post_articles(message)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "The bot scrapes for new articles once a day.\n enter \"/scrapenow\" to check for new content now (will probably post duplicate articles).")

@bot.message_handler(commands=['scrapenow'])
def scrapenow(message):
    bot.reply_to(message, "scraping now...")
    start_scrape(message)

bot.infinity_polling()
