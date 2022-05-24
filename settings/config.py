import os
# импортируем модуль emoji для отображения эмоджи
from emoji import emojize

# токен выдается при регистрации приложения
TOKEN = '5060282753:AAFUTPI6Wj8Hr7CSSwXkpl68SD2vLYAAVm8'
# название БД
NAME_DB = 'products.db'
# версия приложения
VERSION = '0.0.1'
# автор приложния
AUTHOR = 'User'

# родительская директория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до базы данных
DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

# кнопки управления
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать ответы'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize('⚙️ Настройки'),
    'SEMIPRODUCT': emojize(':books: Ответы ЕГЭ 2022'),
    'GROCERY': emojize(':books: Ответы ОГЭ 2022'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Оформить заказ',
    'COPY': '©️'
}

# id категорий продуктов
CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ICE_CREAM': 3,
}

# названия команд
COMMANDS = {
    'START': "start",
    'HELP': "help",
}
