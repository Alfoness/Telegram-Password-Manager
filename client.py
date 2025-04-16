import telebot
from telebot import TeleBot
from telebot.types import Message, CallbackQuery
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ID as id
from config import lang
import funcs

if lang == 'ru':
    import ru_RU as text

def check_user(func):
    def wrapper(context, bot: TeleBot):
        #if context.from_user.id == id: func(context, bot)
        #else: pass 
        func(context, bot)
    return wrapper

@check_user
def start(message: Message, bot: TeleBot):
    bot.send_message(
        chat_id=id,
        parse_mode="Markdown",
        text=text.start.format(message.from_user.first_name),
        disable_web_page_preview=True)
    bot.send_message(
        chat_id=id,
        parse_mode="Markdown",
        text=text.commands)    

@check_user
def help(message: Message, bot: TeleBot):
    bot.send_message(
        chat_id=id,
        parse_mode="Markdown",
        text=text.commands)

@check_user
def createVault(message: Message, bot: TeleBot):
    bot.send_message(
        chat_id=id,
        parse_mode="Markdown",
        text=text.vaultEnter_name)
    bot.register_next_step_handler(message=message, callback=createVault_getName, bot=bot)

@check_user
def createVault_getName(message: Message, bot: TeleBot):
    try:
        funcs.createVault(message.text)
        
        kb = InlineKeyboardMarkup(row_width=1)
        for i in text.types:
            kb.add(InlineKeyboardButton(text=text.types[i], callback_data=f'add {str(message.text)} {i}'))
        
        bot.send_message(
            chat_id=id,
            parse_mode="Markdown",
            text=text.vaultCreated,
            reply_markup=kb)
        
    except Exception as error:
        if error == 'NameUsed': bot.send_message(chat_id=id,
                                                 text=text.NameUsed)

def addNote(call: CallbackQuery, bot: TeleBot):
    call_data, vault, type = call.data.split()
    print(call_data, vault, type)