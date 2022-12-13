import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'другие вопросы с настройками'

async def commandServiceSettingOther(event):
    chat = event.chat_id
    
    await event.respond(SERVICESETTINGTROUBLEOTHER)