import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql
from commands.commandShopBuyTehDeviceBuy import commandShopBuyTehDeviceBuy

key = 'технику и аксессуары'

async def commandShopBuyTehDevice(event):
    chat = event.chat_id
    
    msg, buttons = commandShopBuyTehDeviceBuy(event, 1)

    await event.respond(msg, buttons=buttons, link_preview=False)