import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'выкуп'

async def commandShopRebuy(event):
    chat = event.chat_id
    
    buttons = [[Button.inline("Iphone", b"rebuy_iphone"), Button.inline("Apple Watch", b"rebuy_watch")]]

    await event.respond(SHOPREBUY, buttons=buttons)