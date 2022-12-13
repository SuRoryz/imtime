import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'загрузка и выгрузка данных в icloud'

async def commandServiceSettingIcloud(event):
    chat = event.chat_id
    
    await event.respond(SERVICESETTINGTROUBLEICLOUD)