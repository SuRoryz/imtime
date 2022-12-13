import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from sql import Sql

key = 'аксессуар'

async def commandShopBuyDevice(event):
    buttons= [
            [Button.inline('Для iPhone', b'aksessuary/dlya-iphone_1'),
             Button.inline('Для iPad', b'aksessuary/dlya-ipad_1'),
             Button.inline('Для Mac', b'aksessuary/dlya-mac_1'),
            ],
        ]

    await event.respond(SHOPBUYDEVICE, parse_mode='md', buttons=buttons)