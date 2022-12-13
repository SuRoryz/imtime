SESSION = "rsue"
APP_ID = 5784890
APP_HASH = "ab9cc8abe39e882966993a8c454046e0"
BOT_TOKEN = "5778190136:AAHxfngln6bYsDDhoFvL7gN8zyT9McTifwI"

MAX_BOOK_ON_PAGE = 5

MENU_TREE = {
    "другие вопросы с настройками": "Нужен ремонт",
    "статус работ": "Сервис",
    "получить консультацию": "Сервис",
    "меню": "Меню",
    "магазин": "Меню",
    "сервис": "Меню",
    "технику": "Купить",
    "аксессуар": "Купить",
    "технику и аксессуары": "Купить",
    "купить": "Магазин",
    "трейд-ин": "Магазин",
    "выкуп": "Магазин",
    "комиссия": "Магазин",
    "записаться в офис": "Нужен ремонт",
    "записаться на удалённую диагностику": "Нужен ремонт",
    "получить консультацию": "Нужен ремонт",
    "нужен ремонт": "Сервис",
    "вопрос по оплате покупок и подписок": "Проблемы с настройкой",
    "не устанавливается приложение": "Проблемы с настройкой",
    "проблема с подключением акксесуаров": "Проблемы с настройкой",
    "создание учётной записы": "Проблемы с настройкой",
    "другие вопросы с настройками": "Проблемы с настройкой",
    "проблемы с настройкой": "Сервис",
    "забыли пароль": "Сервис",
    "пароль от учетной записи apple ID": "Забыли пароль",
    "код-пароль от экрана блокировки": "Забыли пароль",
    "узнать сроки гарантии": "Сервис",
    "узнать правила обслуживания": "Сервис",
    "статус работ": "Сервис",
    "записаться на выдачу готовой техники": "Сервис",
}

MENU_BUTTONS = {
    'Магазин': {"Купить": [
                      ["Технику",
                      "Аксессуар"],
                      "Технику и аксессуары",
                      "Назад" 
                ],
                "Трейд-ин": "",
                "Назад": ""},
    'Сервис': {"Нужен ремонт": ["Записаться в офис",
                                "Записаться на удалённую диагностику",
                                "Получить консультацию",
                                "Назад"],
                "Проблемы с настройкой": [
                        "Вопрос по оплате покупок и подписок",
                        "Не устанавливается приложение",
                        "Проблема с подключением акксесуаров",
                        "Загрузка и выгрузка данных в ICloud",
                        "Создание учетной записи",
                        "Другие вопросы с настройками",
                        "Назад"
                    ],
                "Забыли пароль": [
                    "Пароль от учётной записи apple ID",
                    "Код-пароль от экрана блокировки",
                    "Назад"
                ],
                "Узнать сроки гарантии": "",
                "Узнать правила обслуживания": "",
                "Статус работ": "",
                "Записаться на выдачу готовой техники": "",
                "Назад": ""}
}

CACHED = []

products_full = []

products = {
        "iphone": [],
        "ipad": [],
        "mac": [],
        "aksessuary/aksessuary-apple": [],
        "aksessuary/chehly": [],
        "aksessuary/zaschitnye-stekla":  [],
        "aksessuary/dlya-iphone":  [],
        "aksessuary/dlya-mac":  [],
        "aksessuary/dlya-ipad": []
    }

CATEGORIES = []

MODELS = []
MODELS_URL = []
MODELS_FULL = {}

ADMIN = ""

MENU = ""
SHOP = ""
SERVICE = ""

SHOPBUY = ""
SHOPTRADE = ""
SHOPREBUY = ""
SHOPCOMMISSION = ""
SHOPBUYTEH = ""
SHOPBUYDEVICE = ""
SHOPBUYTEHDEVICE = ""
SERVICEFIX = ""
SERVICEFIXGETIN = ""
SERVICEFIXGETINUD = ""
SERVICEFIXGETCONS = ""
SERVICESETTINGTROUBLE = ""
SERVICESETTINGTROUBLEABOUTBUY = ""
SERVICESETTINGTROUBLENOTINSTALLING = ""
SERVICESETTINGTROUBLENOTDEVICE = ""
SERVICESETTINGTROUBLEICLOUD = ""
SERVICESETTINGTROUBLEACCOUNT = ""
SERVICESETTINGTROUBLEOTHER = ""
SERVICEPASSWORD = ""
SERVICEPASSWORDACCOUNT = ""
SERVICEPASSWORDSCREEN = ""
SERVICEGARANTTIME = ""
SERVICEDEVICEFIX = ""
SERVICESTATUS = ""
SERVICEGETIN = ""

SHOPBUYTEHINSTANCE = ""
SERVICEFIXINSTANCE = ""

TRADEIN_TABLE= {"Iphone": {},
                "Apple Watch": {},
                "AppleTV": {}}

COMMISSION_TABLE = {"Iphone": {},
                "Apple Watch": {}}

REBUY_TABLE = {"Iphone": {},
                "Apple Watch": {}}

