import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'комиссия'

async def commandShopCommission(event):
    chat = event.chat_id

    buttons = [[Button.inline("Iphone", b"com_iphone"), Button.inline("Apple Watch", b"com_watch")]]

    await event.respond(SHOPCOMMISSION, buttons=buttons)