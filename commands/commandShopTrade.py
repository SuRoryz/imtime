from math import ceil
import sys
sys.path.append("..")

from telethon import TelegramClient, events
from telethon.tl.custom import Button
import config as cf
from config import *
from sql import Sql

key = 'трейд-ин'

async def commandShopTrade(event):
    chat = event.chat_id
    
    buttons = [[Button.inline("Iphone", b"trade_iphone"), Button.inline("Apple Watch", b"trade_watch"), Button.inline("Apple TV", b"trade_tv")]]

    await event.respond(cf.SHOPTRADE, buttons=buttons)

# COM

def commandShopComissionModel(event, type, page=1):

    type_table = {
        "iphone": "Iphone",
        "watch": "Apple Watch",
        "tv": "AppleTV"
    }

    if type in type_table:
        type = type_table[type]

    buttons = [[]]
    max_on_page = 8
    max_pages = ceil(len(COMMISSION_TABLE[type])/max_on_page)

    for index, model in enumerate(COMMISSION_TABLE[type]):
        if index >= max_on_page:
            try:
                if page != 1:
                    buttons.append([Button.inline(f"↩ Страница {page-1}", f"com-model-page_{type}_{page-1}".encode())])
                if page != max_pages:
                    if page != 1:
                        buttons[-1].append(Button.inline(f"↪ Страница {page+1}", f"com-model-page_{type}_{page+1}".encode()))
                    else:
                        buttons.append([Button.inline(f"↪ Страница {page+1}", f"com-model-page_{type}_{page+1}".encode())])
            finally:
                buttons.append([Button.inline("↩ К выбору категории", b"com-to-type")])
                break

        try:
            if len(buttons[-1]) != 2:
                buttons[-1].append(Button.inline(list(COMMISSION_TABLE[type].keys())[index + ((page - 1) * max_on_page)], f"crm_{type}_{list(COMMISSION_TABLE[type].keys())[index + ((page - 1) * max_on_page)]}".encode()))
            else:
                buttons.append([Button.inline(list(COMMISSION_TABLE[type].keys())[index + ((page - 1) * max_on_page)], f"crm_{type}_{list(COMMISSION_TABLE[type].keys())[index + ((page - 1) * max_on_page)]}".encode())])
        except Exception as e:
            buttons.append([Button.inline(f"↩ Страница {page-1}", f"com-model-page_{type}_{page-1}".encode())])
            buttons.append([Button.inline("↩ К выбору категории", b"com-to-type")])
            break

        if max_pages == 1 and index == len(COMMISSION_TABLE[type]) - 1:
            buttons.append([Button.inline("↩ К выбору категории", b"com-to-type")])

    return "⚙ Выберите модель", buttons

def commandShopComissionModelConfigs(type, model):
    configs = COMMISSION_TABLE[type][model]

    msg = f"Примерная оценочная стоимость для **{model}**\n\n"

    for cfg in configs:
        msg += f"{cfg} - {configs[cfg]}\n"

    buttons = Button.inline("↩ К выбору модели", f"com-model-page_{type}_1".encode())
    
    return msg, buttons

# REBUY

def commandShopRebuyModel(event, type, page=1):

    type_table = {
        "iphone": "Iphone",
        "watch": "Apple Watch",
        "tv": "AppleTV"
    }

    if type in type_table:
        type = type_table[type]

    buttons = [[]]
    max_on_page = 8
    max_pages = ceil(len(REBUY_TABLE[type])/max_on_page)

    for index, model in enumerate(REBUY_TABLE[type]):
        if index >= max_on_page:
            try:
                if page != 1:
                    buttons.append([Button.inline(f"↩ Страница {page-1}", f"rebuy-model-page_{type}_{page-1}".encode())])
                if page != max_pages:
                    if page != 1:
                        buttons[-1].append(Button.inline(f"↪ Страница {page+1}", f"rebuy-model-page_{type}_{page+1}".encode()))
                    else:
                        buttons.append([Button.inline(f"↪ Страница {page+1}", f"rebuy-model-page_{type}_{page+1}".encode())])
            finally:
                buttons.append([Button.inline("↩ К выбору категории", b"rebuy-to-type")])
                break

        try:
            if len(buttons[-1]) != 2:
                buttons[-1].append(Button.inline(list(REBUY_TABLE[type].keys())[index + ((page - 1) * max_on_page)], f"rrm_{type}_{list(REBUY_TABLE[type].keys())[index + ((page - 1) * max_on_page)]}".encode()))
            else:
                buttons.append([Button.inline(list(REBUY_TABLE[type].keys())[index + ((page - 1) * max_on_page)], f"rrm_{type}_{list(REBUY_TABLE[type].keys())[index + ((page - 1) * max_on_page)]}".encode())])
        except Exception as e:
            buttons.append([Button.inline(f"↩ Страница {page-1}", f"rebuy-model-page_{type}_{page-1}".encode())])
            buttons.append([Button.inline("↩ К выбору категории", b"rebuy-to-type")])
            break

        if max_pages == 1 and index == len(REBUY_TABLE[type]) - 1:
            buttons.append([Button.inline("↩ К выбору категории", b"rebuy-to-type")])

    return "⚙ Выберите модель", buttons

def commandShopRebuyModelConfigs(type, model):
    configs = REBUY_TABLE[type][model]

    msg = f"Примерная оценочная стоимость для **{model}**\n\n"

    for cfg in configs:
        msg += f"{cfg} - {configs[cfg]}\n"

    buttons = Button.inline("↩ К выбору модели", f"rebuy-model-page_{type}_1".encode())
    
    return msg, buttons

#TRADE

def commandShopTradeModel(event, type, page=1):

    type_table = {
        "iphone": "Iphone",
        "watch": "Apple Watch",
        "tv": "AppleTV"
    }

    if type in type_table:
        type = type_table[type]

    buttons = [[]]
    max_on_page = 8
    max_pages = ceil(len(TRADEIN_TABLE[type])/max_on_page)

    for index, model in enumerate(TRADEIN_TABLE[type]):
        if index >= max_on_page:
            try:
                if page != 1:
                    buttons.append([Button.inline(f"↩ Страница {page-1}", f"trade-model-page_{type}_{page-1}".encode())])
                if page != max_pages:
                    if page != 1:
                        buttons[-1].append(Button.inline(f"↪ Страница {page+1}", f"trade-model-page_{type}_{page+1}".encode()))
                    else:
                        buttons.append([Button.inline(f"↪ Страница {page+1}", f"trade-model-page_{type}_{page+1}".encode())])
            finally:
                buttons.append([Button.inline("↩ К выбору категории", b"trade-to-type")])
                break

        try:
            if len(buttons[-1]) != 2:
                buttons[-1].append(Button.inline(list(TRADEIN_TABLE[type].keys())[index + ((page - 1) * max_on_page)], f"trm_{type}_{list(TRADEIN_TABLE[type].keys())[index + ((page - 1) * max_on_page)]}".encode()))
            else:
                buttons.append([Button.inline(list(TRADEIN_TABLE[type].keys())[index + ((page - 1) * max_on_page)], f"trm_{type}_{list(TRADEIN_TABLE[type].keys())[index + ((page - 1) * max_on_page)]}".encode())])
        except Exception as e:
            buttons.append([Button.inline(f"↩ Страница {page-1}", f"trade-model-page_{type}_{page-1}".encode())])
            buttons.append([Button.inline("↩ К выбору категории", b"trade-to-type")])
            break

        if max_pages == 1 and index == len(TRADEIN_TABLE[type]) - 1:
            buttons.append([Button.inline("↩ К выбору категории", b"trade-to-type")])

    return "⚙ Выберите модель", buttons

def commandShopTradeModelConfigs(type, model):
    configsTrade = TRADEIN_TABLE[type][model]

    try:
        configsRebuy = REBUY_TABLE[type][model]
        configsCom = COMMISSION_TABLE[type][model]
    except:
        pass


    msg = f"Примерная оценочная стоимость для **{model}**\n\n"

    for cfg in configsTrade:
        msg += f"Трейд-ин: {cfg}G - {configsTrade[cfg]}\n"

        try:
            msg += f"Выкуп: {cfg}G - {configsRebuy[cfg]}\n"
            msg += f"Комиссия: {cfg}G - {configsCom[cfg]}\n"
        except:
            pass
        finally:
            msg += "\n"

    buttons = Button.inline("↩ К выбору модели", f"trade-model-page_{type}_1".encode())
    
    return msg, buttons