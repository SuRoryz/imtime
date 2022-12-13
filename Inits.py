import config
import requests
import os
import importlib
import xml.etree.ElementTree as ET
import sys
import time

from bs4 import BeautifulSoup

from threading import Thread
from sheets import Sheets

def initTradein() -> None:
    url = "https://store.imtime.ru/blog/trade-in/"

    def parse(div):
        pass

    page = requests.get(url, verify=False).text
    soup = BeautifulSoup(page, features="html.parser")

    tables = soup.findAll('div', {'class': "tab-content"})

    # TRADE IN
    for i, item in enumerate(config.TRADEIN_TABLE.keys()):
        columns = tables[i].findAll('div', {'class': "ty-column3"})
        
        for column in columns:
            name = column.find('div', {'class': "tradein-header"}).text

            config_names = column.findAll('div', {'class': "tradein-config"})
            config_prices = column.findAll('div', {'class': "tradein-price"})
            configs = {}

            for j in range(len(config_names)):
                configs[config_names[j].text] = config_prices[j].text
            
            config.TRADEIN_TABLE[item][name] = configs
    
    # COMMISSIONS
    for i, item in enumerate(config.COMMISSION_TABLE.keys()):
        columns = tables[i + 3].findAll('div', {'class': "ty-column3"})
        
        for column in columns:
            name = column.find('div', {'class': "tradein-header"}).text

            config_names = column.findAll('div', {'class': "tradein-config"})
            config_prices = column.findAll('div', {'class': "tradein-price"})
            configs = {}

            for j in range(len(config_names)):
                configs[config_names[j].text] = config_prices[j].text
            
            config.COMMISSION_TABLE[item][name] = configs
    
    # REBUY 

    for i, item in enumerate(config.REBUY_TABLE.keys()):
        columns = tables[i + 5].findAll('div', {'class': "ty-column3"})
        
        for column in columns:
            name = column.find('div', {'class': "tradein-header"}).text

            config_names = column.findAll('div', {'class': "tradein-config"})
            config_prices = column.findAll('div', {'class': "tradein-price"})
            configs = {}

            for j in range(len(config_names)):
                configs[config_names[j].text] = config_prices[j].text
            
            config.REBUY_TABLE[item][name] = configs
    
    print(config.TRADEIN_TABLE)

def initShop() -> None:

    url = "https://store.imtime.ru/"

    class getSite(Thread):
        def __init__(self, type):
            Thread.__init__(self)

            self.type = type
        
        def parse(self, div):
            obj = div.find('form').find('div', {"style": "cursor: pointer;"})

            name = obj.find('div', {"class": "ty-grid-list__item-name"}).find('a').text
            url = obj.find('div', {"class": "ty-grid-list__item-name"}).find('a')["href"]
            try:
                price = obj.find('div', {"class": "ty-grid-list__price"}).find('span', {"class": "ty-price-num"}).text
            except:
                price = "Нет цены"
            
            config.products_full.append((name, price, url))

            return (name, price, url)

        def run(self):
            try:
                text = requests.get(url + self.type, verify=False).text
                soup = BeautifulSoup(text, features="html.parser")

                table = soup.findAll('div', {"class" : "ty-grid-list__item ty-quick-view-button__wrapper"})
                config.products[self.type].extend(list(map(self.parse, table)))
                pages = soup.find('div', {"class" : "ty-pagination__items"})

                if pages:
                    max_pages = len(pages.findAll())
                
                    for i in range(2, max_pages + 1):
                        text = requests.get(url + self.type + f"/page-{i}", verify=False).text
                        soup = BeautifulSoup(text, features="html.parser")

                        table = soup.findAll('div', {"class" : "ty-grid-list__item ty-quick-view-button__wrapper"})
                        config.products[self.type].extend(list(map(self.parse, table)))
                
                sys.exit()

            except Exception as e:
                print(e)
            finally:
                sys.exit()
    
    for type in config.products.keys():
        getSite(type).start()


def initModels() -> None:
    url = "https://imtime.ru/ustrojstva/modeli-telefonov/"

    class getSite(Thread):
        def __init__(self, model, model_url):
            Thread.__init__(self)

            self.model = model
            self.model_url = model_url

        def parse(self, item):
            tds = item.findAll('td')
            name = tds[0].find('a').text
            try:
                link = "https://imtime.ru/" + tds[-1].find('a')["href"]
            except:
                link = "no_link"
            try:
                duration = tds[1].text
            except:
                duration = "no_time"
            try:
                price = tds[2].text
            except:
                price = "no_price"

            return name, link, duration, price

        def run(self):
            try:
                text = requests.get(url + self.model_url, verify=False).text
                soup = BeautifulSoup(text, features="html.parser")

                table = soup.findAll('tr')[1:]

                config.MODELS_FULL[self.model] = list(map(self.parse, table))

            except Exception as e:
                print(e)
            finally:
                sys.exit()

    for index, item in enumerate(config.MODELS):
        getSite(item, config.MODELS_URL[index]).start()


def initCommands() -> dict:
    # Получаем модули комманд из папки commands
    modules: list = os.listdir('commands')
    commands: dict = dict()
    
    # Проходим через все py файлы и импортируем функцию команды
    # А так же её ключ
    for module in modules:
        if module == "__pycache__":
            continue

        print(module)
        
        module = module.replace('.py', '')

        print(module)
        
        module_module = importlib.import_module(f'commands.{module}')
        module_func = getattr(module_module, module)
        module_key = getattr(module_module, "key")

        if type(module_key) == tuple:
            for key in module_key:
                commands[key] = module_func
        else:
            commands[module_key] = module_func
    
    return commands

# Получаем данные из гугл таблицы
def initConfig() -> None:
    sh = Sheets()
    table = sh.getTable()
    
    wks = table.sheet1

    config.ADMIN = wks.cell('B3').value
    
    config.MENU = wks.cell('B2').value
    config.SHOP = wks.cell('C2').value
    config.SERVICE = wks.cell('K2').value
    
    config.SHOPBUY = wks.cell('D2').value
    config.SHOPTRADE = wks.cell('E2').value
    config.SHOPREBUY = wks.cell('F2').value
    config.SHOPCOMMISSION = wks.cell('G2').value
    
    config.SHOPBUYTEH = wks.cell('H2').value
    config.SHOPBUYDEVICE = wks.cell('I2').value
    config.SHOPBUYTEHDEVICE = wks.cell('J2').value

    config.SHOPBUYTEHINSTANCE = wks.cell('H4').value
    config.SERVICEFIXINSTANCE= wks.cell('I4').value

    config.SERVICEFIX = wks.cell('L2').value
    config.SERVICEFIXGETIN = wks.cell('S2').value
    config.SERVICEFIXGETINUD = wks.cell('T2').value
    config.SERVICEFIXGETCONS = wks.cell('U2').value

    config.SERVICESETTINGTROUBLE = wks.cell('M2').value
    config.SERVICESETTINGTROUBLEABOUTBUY = wks.cell('V2').value
    config.SERVICESETTINGTROUBLENOTINSTALLING = wks.cell('W2').value
    config.SERVICESETTINGTROUBLENOTDEVICE = wks.cell('X2').value
    config.SERVICESETTINGTROUBLEICLOUD = wks.cell('Y2').value
    config.SERVICESETTINGTROUBLEACCOUNT = wks.cell('Z2').value
    config.SERVICESETTINGTROUBLEOTHER = wks.cell('AA2').value

    config.SERVICEPASSWORD = wks.cell('N2').value
    config.SERVICEPASSWORDACCOUNT = wks.cell('AB2').value
    config.SERVICEPASSWORDSCREEN = wks.cell('AC2').value

    config.SERVICEGARANTTIME = wks.cell('O2').value
    config.SERVICEDEVICEFIX = wks.cell('P2').value
    config.SERVICESTATUS = wks.cell('Q2').value
    config.SERVICEGETIN = wks.cell('R2').value

    config.CATEGORIES = wks.get_col(10, include_tailing_empty=False)[1:]

    wks = table.worksheet_by_title("Модели")

    config.MODELS.extend(wks.get_row(1, include_tailing_empty=False)[1:])
    config.MODELS_URL.extend(wks.get_row(2, include_tailing_empty=False)[1:])