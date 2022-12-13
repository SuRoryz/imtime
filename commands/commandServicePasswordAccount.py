import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'пароль от учётной записи apple id'

async def commandServicePasswordAccount(event):
    chat = event.chat_id

    await event.respond(SERVICEPASSWORDACCOUNT)
