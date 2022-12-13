import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'магазин'

async def commandShop(event):
    chat = event.chat_id

    buttons = []
    row = []

    for index, item in enumerate(MENU_BUTTONS["Магазин"].keys()):

        row.append(Button.text(item, resize=True))

        if index % 2 != 0 or item == "Назад":
            buttons.append(row)
            row = []
    
    await event.respond(SHOP, buttons=buttons)

    return True