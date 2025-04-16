import sys
import telebot
from telebot import TeleBot

def initToken():
	params = sys.params
	print(params)

	try:
		from config import TOKEN
		return
	except Exception as e:
		raise

if __name__ == '__main__':
	initToken()