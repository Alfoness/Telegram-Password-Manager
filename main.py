import sys
import telebot
from telebot import TeleBot
from client import start, help, createVault, addNote

def initToken():
	params = sys.argv
	print(params)

	try:
		from config import TOKEN
		return TOKEN
	except Exception as e:
		raise

def reg_handlers(bot: TeleBot) -> None:
    bot.register_message_handler(callback=start, commands=['start'], pass_bot=True)
    bot.register_message_handler(callback=help, commands=['help'], pass_bot=True)
    bot.register_message_handler(callback=createVault, commands=['newvault'], pass_bot=True)
    bot.register_callback_query_handler(callback=addNote, func=lambda call: call.data.startswith('add'), pass_bot=True)
 
if __name__ == '__main__':
	bot = TeleBot(initToken())
	reg_handlers(bot=bot)
	bot.polling()