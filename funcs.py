import sqlite3
from telebot import TeleBot
import telebot
from telebot.types import Message
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

database = sqlite3.connect('database.db', check_same_thread=False)
c = database.cursor()

def checkVault(name) -> bool:
    if c.execute("SELECT name FROM vaults WHERE name = ?", (name, )).fetchone() is None: return True
    else: False

def createVault(name) -> None:
    if checkVault(str(name)):
        c.execute("INSERT INTO vault (name) VALUES (?)", (str(name), ))
        database.commit()
    else: raise Exception('NameUsed')