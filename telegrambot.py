import telebot
from telebot.types import Message
from telebot import types
from inc import increase

bot  =  telebot.TeleBot('1030274384:AAGleQhVCCfv0y1xU5hVpRUugl4PZg8XDKI')

phrases = ['сука', 'лол']
swearing = {'count': 0}

@bot.message_handler(func=lambda m: True)
def echo(message: Message):
	for phrase in phrases:
		if phrase in message.text.lower():
			bot.send_message(-303816860, 'Это слово есть в списке фраз')

	if 'пиздец' in message.text.lower():
		bot.reply_to(message, 'как это грубо.')
		swearing['count'] += 1
	elif 'блять' in message.text.lower():
		bot.reply_to(message, 'не матерись -_-')
		swearing['count'] += 1
	elif 'писос' in message.text.lower():
		bot.reply_to(message, 'мягко, но все равно мало приятного')
		swearing['count'] += 1
	elif 'привет' in message.text.lower():
		bot.reply_to(message, 'Привет! Как твои дела?)')
		bot.send_message(-303816860, 'Снова опаздываешь...')
	elif 'сколько матов' in message.text.lower():
		bot.reply_to(message, 'На данный момент матов - ' + str(swearing['count']))

@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.reply_to(message, text='Hey =)')
		
bot.polling(none_stop = True)