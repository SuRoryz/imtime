import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'проблема с подключением акксесуаров'

async def commandServiceSettingDevice(event):
    chat = event.chat_id
    
    await event.respond(SERVICESETTINGTROUBLENOTDEVICE)