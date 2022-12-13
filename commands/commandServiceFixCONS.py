import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'получить консультацию'

async def commandServiceFixCONS(event):
    chat = event.chat_id
    
    await event.respond(SERVICEFIXGETCONS)