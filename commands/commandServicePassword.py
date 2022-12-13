import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'забыли пароль'

async def commandServicePassword(event):
    chat = event.chat_id
    
    markup = event.client.build_reply_markup(
        [[Button.text(x, resize=True)] if type(x) != list else [Button.text(y, resize=True) for y in x] for x in MENU_BUTTONS["Сервис"]["Забыли пароль"]]
        )
    
    await event.respond(SERVICEPASSWORD, buttons=markup)

    return True