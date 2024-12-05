import os
import pandas
import telebot
from dotenv import load_dotenv, dotenv_values

load_dotenv()
API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)

def post_articles():
    url_list = pandas.read_csv('article_urls', header=None, index_col=False)

    
# TODO: fix :(

'''
        for i in post_list:
            bot.send_message(post_list[i]);
            print("\nposting: " + post_list[i]);
'''
def start_scrape():
    print("starting scrape")
    #os.system("python aggregator.py")

    # debugging:
    with open("article_urls") as file:
        while line


    post_articles()

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "The bot scrapes for new articles once a day.\n enter \"/scrapenow\" to check for new content now (will probably post duplicate articles).")

@bot.message_handler(commands=['scrapenow'])
def scrapenow(message):
    bot.reply_to(message, "scraping now...")
    start_scrape()

bot.infinity_polling()
