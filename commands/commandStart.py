import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = ('меню', "начать", "старт", "/start")

async def commandStart(event):
    chat = event.chat_id

    markup = event.client.build_reply_markup(
        [Button.text(x, resize=True) for x in MENU_BUTTONS]
        )
    
    await event.respond(MENU, buttons=markup)

    return True