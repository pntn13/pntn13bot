# -*- coding: utf-8 -*-

import config
import telebot
import time

bot = telebot.TeleBot(config.token)

def append_to_log(message):
    with open("messages.log", "a", encoding="utf-8") as logs:
        logs.write(message)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "who da fuck do you think i is?")
    
@bot.message_handler(commands=["happy_days"])
def happy_days(message):
    mytime = time.localtime(message.date)
    starttime = time.strptime("5 Nov 16", "%d %b %y")
    number = time.mktime(mytime) - time.mktime(starttime)
    number /= 24*60*60
    number = round(number)
    bot.reply_to(message, str(number))
    printed_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(message.date))
    append_to_log("{} | {} {} : {} :: {}\n".format(printed_time, 
                                        message.from_user.first_name, 
                                        message.from_user.last_name, 
                                        message.text, 
                                        str(number)))

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)
    #print(message)
    #print(time.localtime(message.date))
    printed_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(message.date))
    append_to_log("{} | {} {} : {}\n".format(printed_time, 
                                        message.from_user.first_name, 
                                        message.from_user.last_name, 
                                        message.text))
    

if __name__ == "__main__":
    bot.polling(none_stop=True)
     
