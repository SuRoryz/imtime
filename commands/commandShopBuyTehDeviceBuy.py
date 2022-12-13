import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from importlib import reload
import config
from sql import Sql
from math import ceil

key = 'NOTVALIDKEY'

def commandShopBuyTehDeviceBuy(event, page=1):
    full_msg = ""
    page_max = 10

    Button.clear()
    
    def createInstance(obj):
        return config.SHOPBUYTEHINSTANCE.format(name=obj[0], price=obj[1], url=obj[2]) + "\n\n"

    counter = 1
    while counter <= page_max:
        try:
            full_msg += createInstance(config.products_full[counter + page_max * (page - 1)])
            counter += 1
        except:
            break
    
    max_pages = ceil(len(config.products_full) / page_max)

    buttons= [[]]

    if page != 1:
        buttons[0].append(Button.inline(f'↩ Страница {page-1}', f'full-buy_{page-1}'.encode()))
    if page != max_pages:
        buttons[0].append(Button.inline(f'↪ Страница {page+1}', f'full-buy_{page+1}'.encode()))
    
    buttons.append([Button.inline('↩ Назад', b'to_buy')])

    return full_msg, buttons
