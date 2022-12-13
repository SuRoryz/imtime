import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'создание учетной записи'

async def commandServiceSettingAccount(event):
    chat = event.chat_id
    
    await event.respond(SERVICESETTINGTROUBLEACCOUNT)