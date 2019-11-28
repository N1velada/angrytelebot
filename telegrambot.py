import telebot
from telebot.types import Message
from telebot import types

bot  =  telebot.TeleBot('1030274384:AAGleQhVCCfv0y1xU5hVpRUugl4PZg8XDKI')

current_number = 0

def increase(current_number, a):
	current_number += 1

@bot.message_handler(func=lambda m: True)
def echo_all_2(message: Message):
	if 'пиздец' in message.text:
		bot.reply_to(message, 'ты серьезно?')
		increase(current_number, 1)
	elif 'блять' in message.text:
		bot.reply_to(message, 'не матерись -_-')
		increase(current_number, 1)
	elif 'сколько матов уже' in message.text:
		bot.reply_to(message, str(current_number) + '. Живи пока.')
		
bot.polling(none_stop = True)