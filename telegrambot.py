import telebot
from telebot.types import Message
from telebot import types
from inc import increase

bot  =  telebot.TeleBot('1030274384:AAGleQhVCCfv0y1xU5hVpRUugl4PZg8XDKI')

#current_number = 0

@bot.message_handler(func=lambda m: True)
def echo(message: Message):
	if 'пиздец' in message.text.lower():
		bot.reply_to(message, 'ты серьезно?')
#		curent_number = increase(curent_number)
	elif 'блять' in message.text.lower():
		bot.reply_to(message, 'не матерись -_-')
	elif 'привет' in message.text.lower():
		bot.reply_to(message, 'Привет! Как твои дела?)')
		bot.send_message(-303816860, 'Снова опаздываешь...')
#		curent_number = increase(curent_number)
#	elif 'сколько матов уже' in message.text:
#		bot.reply_to(message, str(current_number) + '. Живи пока.')

@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.reply_to(message, text='Hey =)')
		
bot.polling(none_stop = True)