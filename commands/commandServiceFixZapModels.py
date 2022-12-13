import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from importlib import reload
import config
from sql import Sql
from math import ceil

key = 'NOTVALIDKEY'

def commandServiceFixZapModels(event, model, page=1):
    full_msg = ""
    page_max = 10

    def createInstance(obj):
        name = name=obj[0].replace("\n", "")
        link = link=obj[1].replace("\n", "")
        duration=obj[2].replace("\n", "")
        price=obj[3].replace("\n", "")

        return config.SERVICEFIXINSTANCE.format(name=name, link=link, duration=duration, price=price) + "\n\n"

    counter = 1
    while counter <= page_max:
        try:
            full_msg += createInstance(config.MODELS_FULL[model][counter + page_max * (page - 1)])
            counter += 1
        except Exception as e:
            print(e)
            break
    
    max_pages = ceil(len(config.MODELS_FULL[model]) / page_max)

    buttons= [[]]

    if page != 1:
        buttons.append([Button.inline(f"↩ Страница {page-1}", f'FIX-LIST_{model}_{page-1}'.encode())])
    if page != max_pages:
        if page != 1:
            buttons[-1].append(Button.inline(f"↪ Страница {page+1}", f'FIX-LIST_{model}_{page+1}'.encode()))
        else:
            buttons.append([Button.inline(f"↪ Страница {page+1}", f'FIX-LIST_{model}_{page+1}'.encode())])
        
        buttons.append([Button.inline(f"↩ К выбору модели", f'fixmodel'.encode())])

    return full_msg, buttons
