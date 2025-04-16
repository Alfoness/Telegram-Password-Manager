import telebot
from telebot import TeleBot
from telebot.types import Message, CallbackQuery
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ID as id
from config import lang

if lang == 'ru':
    import ru_RU as text

def start(message: Message, bot: TeleBot):
    bot.send_message(
        chat_id=id,
        parse_mode="Markdown",
        text=text.start.format(message.from_user.first_name),
        disable_web_page_preview=True)
    bot.send_message(
        chat_id=id,
        text=text.commands)    

def help(message: Message, bot: TeleBot):
    bot.send_message(
        chat_id=id,
        text=text.commands)

def createVault(message: Message, bot: TeleBot):
    ...
    
def createVault_getName(message: Message, bot: TeleBot):
    ...