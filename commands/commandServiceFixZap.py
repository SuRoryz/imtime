import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from config import *
from math import ceil

key = 'записаться в офис'

async def commandServiceFixZap(event):
    chat = event.chat_id

    msg, buttons = await commandServiceFixZapPages(event, 1)
    
    print(msg)
    await event.respond(msg, buttons=buttons)

async def commandServiceFixZapPages(event, page=1):
    buttons = [[]]
    max_on_page = 8
    max_pages = ceil(len(MODELS)/max_on_page)

    for index, model in enumerate(MODELS):
        if index >= max_on_page:
            try:
                if page != 1:
                    buttons.append([Button.inline(f"↩ Страница {page-1}", f"zap-model-page_{page-1}".encode())])
                if page != max_pages:
                    if page != 1:
                        buttons[-1].append(Button.inline(f"↪ Страница {page+1}", f"zap-model-page_{page+1}".encode()))
                    else:
                        buttons.append([Button.inline(f"↪ Страница {page+1}", f"zap-model-page_{page+1}".encode())])
            finally:
                break
        
        try:
            if len(buttons[-1]) != 2:
                buttons[-1].append(Button.inline(MODELS[index + (max_on_page * (page - 1))], f"zap-model_{MODELS[index + (max_on_page * (page - 1))]}".encode()))
            else:
                buttons.append([Button.inline(MODELS[index + (max_on_page * (page - 1))], f"zap-model_{MODELS[index + (max_on_page * (page - 1))]}".encode())])
        
        except Exception as e:
            buttons.append([Button.inline(f"↩ Страница {page-1}", f"zap-model-page_{page-1}".encode())])
            break

    return "⚙ Выберите модель", buttons