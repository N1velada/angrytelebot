import telebot
import datetime
import sqlite3
import datetime
from telebot.types import Message
from telebot import types

bot  =  telebot.TeleBot('1030274384:AAGleQhVCCfv0y1xU5hVpRUugl4PZg8XDKI')
conn = sqlite3.connect('BotSwearing.db')
cursor = conn.cursor()

phrases = ['сука', 'лол', 'хуй', 'пизд']

@bot.message_handler(func=lambda m: True)
def echo(message: Message):
	for phrase in phrases:
		if phrase in message.text.lower():
			bot.reply_to(message, 'Это слово есть в списке фраз, в скором времени ',
						'я научусь реагировать на него')

	if 'бля' in message.text.lower():
		bot.reply_to(message, 'не матерись -_-')
		date = datetime.datetime.today()
		date2 = date.strftime("%Y.%m.%d")
		cursor.execute("SELECT * FROM Swearings")
		results = cursor.fetchall()
		for result in results:
		    if result[1] == date2:
		        number = result[0]
		        number2 = result[2] + 1
		        cursor.execute("UPDATE Swearings SET Count = " + str(number2) + " WHERE ID = " + str(number))
		        conn.commit()
	elif 'бот запомни слово' in message.text.lower():
		bot.reply_to(message, 'окич )')
		phrases.append(message.text[18:])
	elif 'писос' in message.text.lower():
		bot.reply_to(message, 'мягко, но все равно мало приятного')
	elif 'не матерись' in message.text.lower():
		bot.reply_to(message, 'Не забирай мою работу!')
	elif 'привет' in message.text.lower():
		bot.reply_to(message, 'Привет! Как твои дела?)')
		#bot.send_message(-303816860, 'Снова опаздываешь...')
	#elif 'сколько матов' in message.text.lower():
		#bot.reply_to(message, 'На данный момент матов - ' + str(swearing[now2]))

@bot.message_handler(content_types=['new_chat_members'])		
def handler_new_member(message):
    user_name = message.new_chat_member.username
    bot.send_message(-303816860, 'Добро пожаловать, @' + user_name + ' !')
		
bot.polling(none_stop = True)