import telebot
import datetime
from telebot.types import Message
from telebot import types

bot  =  telebot.TeleBot('1030274384:AAGleQhVCCfv0y1xU5hVpRUugl4PZg8XDKI')

now = datetime.datetime.now()
now2 = now.strftime("%d-%m-%Y")
swearing = {}
if now2 not in swearing:
    swearing[now2] = 0

phrases = ['сука', 'лол', 'хуй', 'пизд']

@bot.message_handler(func=lambda m: True)
def echo(message: Message):
	for phrase in phrases:
		if phrase in message.text.lower():
			bot.send_message(-303816860, 'Это слово есть в списке фраз, в скором времени я научусь реагировать на него')

	if 'бля' in message.text.lower():
		bot.reply_to(message, 'не матерись -_-')
		swearing[now2] += 1
	elif 'писос' in message.text.lower():
		bot.reply_to(message, 'мягко, но все равно мало приятного')
		swearing[now2] += 1
	elif 'не матерись' in message.text.lower():
		bot.reply_to(message, 'Не забирай мою работу!')
	elif 'привет' in message.text.lower():
		bot.reply_to(message, 'Привет! Как твои дела?)')
		#bot.send_message(-303816860, 'Снова опаздываешь...')
	elif 'сколько матов' in message.text.lower():
		bot.reply_to(message, 'На данный момент матов - ' + str(swearing[now2]))

@bot.message_handler(content_types=['new_chat_members'])		
def handler_new_member(message):
    user_name = message.new_chat_member.username
    bot.send_message(-303816860, 'Добро пожаловать, @' + user_name + ' !')
		
bot.polling(none_stop = True)