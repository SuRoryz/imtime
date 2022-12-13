import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'технику'

async def commandShopBuyTeh(event):
    buttons= [
            [Button.inline('iPhone', b'iphone_1'),
             Button.inline('iPad', b'ipad_1'),
             Button.inline('Mac', b'mac_1'),
            ],
        ]

    await event.respond(SHOPBUYTEH, parse_mode='md', buttons=buttons)