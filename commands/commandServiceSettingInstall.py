import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'не устанавливается приложение'

async def commandServiceSettingInstall(event):
    chat = event.chat_id
    
    await event.respond(SERVICESETTINGTROUBLENOTINSTALLING)