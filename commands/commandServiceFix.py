import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'нужен ремонт'

async def commandServiceFix(event):
    chat = event.chat_id
    
    markup = event.client.build_reply_markup(
        [[Button.text(x, resize=True)] for x in MENU_BUTTONS["Сервис"]["Нужен ремонт"]]
        )
    
    await event.respond(SERVICEFIX, buttons=markup)

    return True