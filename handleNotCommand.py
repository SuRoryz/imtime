import config
from sql import Sql
from json import loads, dumps
from telethon.tl.custom import Button
from commands.commandShopBuyTehBuy import commandShopBuyTehBuy
from commands.commandShopBuyDeviceBuy import commandShopBuyDeviceBuy
from commands.commandShopBuyTehDeviceBuy import commandShopBuyTehDeviceBuy
from commands.commandServiceFixZap import commandServiceFixZapPages
from commands.commandServiceFixZapModels import commandServiceFixZapModels
from commands.commandShopTrade import commandShopTradeModel, commandShopTradeModelConfigs, commandShopRebuyModel, commandShopRebuyModelConfigs, commandShopComissionModel, commandShopComissionModelConfigs

async def handleNotCommand(event, client) -> None:
    user = event.chat_id
    cache = loads(Sql.getCache(user)[0][2])
    
    if event.raw_text.lower() ==  "назад":
        prev_location = cache
        return config.MENU_TREE[prev_location['type'].lower()]

    elif cache["type"] in ["другие вопросы с настройками", "получить консультацию", "вопрос по оплате покупок и подписок"]:
        text = f'От пользователя: {event.message.sender.username}\n\n"{event.raw_text}"\n\nЧтобы написать в этот диалог, ответьте на это сообщение\n\nUSER_ID:{event.chat_id}'
        
        await client.send_message(config.ADMIN, text)
        await event.respond("Сообщение отправлено!")
    
    elif cache["type"] == "статус работ":
        text = f'Запрос на статус работ. Номер договора: {event.raw_text}\n\nНажмите на одну из кнопок ниже, чтобы отправить отчёт о статусе\n\n🕛 - в работе\n✅ - можно забирать\n\nUSER_ID:{event.chat_id}'

        buttons= [
            [Button.inline('🕛', b'notready'),
             Button.inline('✅', b'ready'),
            ],
        ]

        await client.send_message(config.ADMIN, text, buttons=buttons)
        await event.respond("Сообщение отправлено!")

    elif event.message.is_reply:
        rpl = await event.message.get_reply_message()
        rpl_text = rpl.message

        if "USER_ID:" in rpl_text:
            user_id = rpl_text.split("USER_ID:")[1]
            text = f"Техническая поддержка ответила на ваш вопрос:\n\n{event.raw_text}"

            await client.send_message(int(user_id), text)
            await event.respond("Сообщение отправлено!")


async def handleInlineCommand(event, client) -> None:
    table = {
        "notready": "В работе.",
        "ready": "Заказ готов, можно забирать"
    }

    table_buyteh = ["iphone", "ipad", "mac"]
    table_buydevice = ["aksessuary/dlya-iphone", "aksessuary/dlya-ipad", "aksessuary/dlya-mac"]

    answer = event.data.decode("UTF-8")
    cmd = answer.split("_")[0]
    
    if answer == "to_buy":
        markup = event.client.build_reply_markup(
            [[Button.text(x, resize=True)] if type(x) != list else [Button.text(y, resize=True) for y in x] for x in config.MENU_BUTTONS["Магазин"]["Купить"]]
        )
    
        await event.edit(config.SHOPBUY, buttons=markup)
    
    elif answer == "fixmodel":
        msg, buttons = await commandServiceFixZapPages(event, 1)

        await event.edit(msg, buttons=buttons)
    
    elif answer == "trade-to-type":
        buttons = [[Button.inline("Iphone", b"trade_iphone"), Button.inline("Apple Watch", b"trade_watch"), Button.inline("Apple TV", b"trade_tv")]]

        await event.edit("⚙ Выберите категорию", buttons=buttons)
    
    elif answer == "trade-to-type":
        buttons = [[Button.inline("Iphone", b"trade_iphone"), Button.inline("Apple Watch", b"trade_watch"), Button.inline("Apple TV", b"trade_tv")]]

        await event.edit("⚙ Выберите категорию", buttons=buttons)
    
    elif answer == "rebuy-to-type":
        buttons = [[Button.inline("Iphone", b"rebuy_iphone"), Button.inline("Apple Watch", b"rebuy_watch")]]

        await event.edit("⚙ Выберите категорию", buttons=buttons)
    
    elif answer == "com-to-type":
        buttons = [[Button.inline("Iphone", b"com_iphone"), Button.inline("Apple Watch", b"com_watch")]]

        await event.edit("⚙ Выберите категорию", buttons=buttons)

    elif answer == "buyteh":
        buttons= [
            [Button.inline('iPhone', b'iphone_1'),
             Button.inline('iPad', b'ipad_1'),
             Button.inline('Mac', b'mac_1'),
            ]
        ]

        await event.edit(config.SHOPBUYTEH, parse_mode='md', buttons=buttons)
    
    elif answer == "buydevice":
        buttons= [
            [Button.inline('Для iPhone', b'aksessuary/dlya-iphone_1'),
             Button.inline('Для iPad', b'aksessuary/dlya-ipad_1'),
             Button.inline('Для Mac', b'aksessuary/dlya-mac_1'),
            ]
        ]

        await event.edit(config.SHOPBUYDEVICE, parse_mode='md', buttons=buttons)

    elif answer in table.keys():
        rpl = await event.get_message()
        rpl_text = rpl.message

        if "USER_ID:" in rpl_text:
            user_id = rpl_text.split("USER_ID:")[1]
            ans = table[answer]

            dg = rpl_text.split("\n\n")[0].split()[-1]
            text = f"⚙ Статус для договора {dg}:\n\n{ans}"

            await client.send_message(int(user_id), text)
            await event.edit(f"⚙ Статус заказа {dg} обновлён.")
    
    elif cmd in table_buyteh:
        page = int(answer.split("_")[-1])
        type_ = answer.split("_")[0]

        msg, buttons = commandShopBuyTehBuy(event, type_, page)

        print(msg)
        await event.edit(msg, buttons=buttons, link_preview=False)
    
    elif cmd in table_buydevice:
        page = int(answer.split("_")[-1])
        type_ = answer.split("_")[0]

        msg, buttons = commandShopBuyDeviceBuy(event, type_, page)
        await event.edit(msg, buttons=buttons, link_preview=False)
    
    elif cmd == "full-buy":
        page = int(answer.split("_")[-1])

        msg, buttons = commandShopBuyTehDeviceBuy(event, page)
        await event.edit(msg, buttons=buttons, link_preview=False)
    
    elif cmd == "zap-model-page":
        page = int(answer.split("_")[-1])

        msg, buttons = await commandServiceFixZapPages(event, page)
        await event.edit(msg, buttons=buttons, link_preview=False)
    
    elif cmd == "zap-model":
        model = answer.split("_")[-1]

        msg, buttons = commandServiceFixZapModels(event, model, page=1)

        print(msg, buttons)
        await event.edit(msg, buttons=buttons, link_preview=False)
    
    elif cmd == "FIX-LIST":
        model = answer.split("_")[1]
        page = int(answer.split("_")[-1])

        msg, buttons = commandServiceFixZapModels(event, model, page=page)

        print(msg, buttons)
        await event.edit(msg, buttons=buttons, link_preview=False)
    #
    elif cmd == "trade":
        type_ = answer.split("_")[1]

        msg, buttons = commandShopTradeModel(event, type_, page=1)
        await event.edit(msg, buttons=buttons, link_preview=False)
    
    elif cmd == "trade-model-page":
        type_ = answer.split("_")[1]
        page = int(answer.split("_")[-1])

        msg, buttons = commandShopTradeModel(event, type_, page=page)
        await event.edit(msg, buttons=buttons, link_preview=False)
    
    elif cmd == "trm":
        type_ = answer.split("_")[1]
        model = answer.split("_")[-1]

        msg, buttons = commandShopTradeModelConfigs(type_, model)
        await event.edit(msg, buttons=buttons, link_preview=False)
    #
    elif cmd == "rebuy":
        type_ = answer.split("_")[1]

        msg, buttons = commandShopRebuyModel(event, type_, page=1)
        await event.edit(msg, buttons=buttons, link_preview=False)
    
    elif cmd == "rebuy-model-page":
        type_ = answer.split("_")[1]
        page = int(answer.split("_")[-1])

        msg, buttons = commandShopRebuyModel(event, type_, page=page)
        await event.edit(msg, buttons=buttons, link_preview=False)
    
    elif cmd == "rrm":
        type_ = answer.split("_")[1]
        model = answer.split("_")[-1]

        msg, buttons = commandShopRebuyModelConfigs(type_, model)
        await event.edit(msg, buttons=buttons, link_preview=False)
    #
    elif cmd == "com":
        type_ = answer.split("_")[1]

        msg, buttons = commandShopComissionModel(event, type_, page=1)
        await event.edit(msg, buttons=buttons, link_preview=False)
    
    elif cmd == "com-model-page":
        type_ = answer.split("_")[1]
        page = int(answer.split("_")[-1])

        msg, buttons = commandShopComissionModel(event, type_, page=page)
        await event.edit(msg, buttons=buttons, link_preview=False)
    
    elif cmd == "crm":
        type_ = answer.split("_")[1]
        model = answer.split("_")[-1]

        msg, buttons = commandShopComissionModelConfigs(type_, model)
        await event.edit(msg, buttons=buttons, link_preview=False)



