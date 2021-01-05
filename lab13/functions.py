import time
from pymongo import MongoClient
from config import MAIN_DB, ADMIN_DB
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

client = MongoClient("localhost", 27017) 
db = client['NEW_DB']
new_collection = db[MAIN_DB]
adm_collection = db[ADMIN_DB]
driver = Chrome()
home = 'https://www.dvfu.ru/about/rectorate/scheme/'

def parser():
    driver.get(home)
    content = driver.find_elements_by_class_name('org-schema')
    content = content[0]
    #ректор
    contain = driver.find_elements_by_class_name('secondline')
    print(len(contain))
    contain = contain[0]
    rector = contain.find_elements_by_class_name('node-cell')
    update_db(rector[0])
    #проректоры
    contain = driver.find_elements_by_class_name('node-container')
    contain = contain[0]
    prorectors = contain.find_elements_by_class_name('node-cell')
    for i in range(len(prorectors)):
        update_db(prorectors[i])

def update_db(pers):
    link = pers.find_element_by_tag_name('a').get_attribute('href')
    flat_list_handler = driver.current_window_handle
    driver.execute_script('window.open()')
    driver.switch_to.window(driver.window_handles[1])
    driver.get(link)
    results = []
    tmp = {}
    name = driver.find_elements_by_class_name('author-name')
    if len(name) == 0:
        name = driver.find_elements_by_class_name('helpers-title')
        if len(name) == 0:
            name = ''
        else:
            name  = name[0].text
            name = name.split(' ')
            tmp['Fname'] = name[0]
            tmp['Name'] = name[1]
            tmp['Oname'] = name[2]
    else:
        name  = name[0].text
        name = name.split(' ')
        tmp['Fname'] = name[0]
        tmp['Name'] = name[1]
        tmp['Oname'] = name[2]

    dolj = driver.find_elements_by_class_name('author-dolj')
    if len(dolj) == 0:
        dolj = driver.find_elements_by_class_name('helpers-num')
        if len(dolj) == 0:
            dolj = ''
        else:
            dolj = dolj[0].text
    else:
        dolj = dolj[0].text
    tmp['doljname'] = dolj

    adress = driver.find_elements_by_class_name('block-address')
    if len(adress) == 0:
        adress = ''
    else:
        adress = adress[0].text
    tmp['Room'] = adress

    phone = driver.find_elements_by_class_name('block-phone')
    if len(phone) == 0:
        phone = ''
    else:
        phone = phone[0].text
    tmp['Phone'] = phone

    email = driver.find_elements_by_class_name('block-email')
    if len(email) == 0:
        email = ''
    else:
        email = email[0].text
    tmp['Mail'] = email

    results.append(tmp)
    new_collection.insert_many(results)
    adm_collection.insert_many(results)
    driver.close()
    driver.switch_to.window(flat_list_handler)
    time.sleep(2)

def db_list(js):
    many_doc = []
    one_doc = []
    for doc in js:
        one_doc = []
        for value in doc.values():
            one_doc.append(value)
        many_doc.append(one_doc)
    return many_doc

def create_inline_keyboard():
    lenght = new_collection.find().count()
    js = new_collection.find({}, { 'doljname' : 1, '_id' : 0})
    full = db_list(js)
    board_2 = InlineKeyboardMarkup().add(InlineKeyboardButton(f'{full[0][0]}', callback_data=f'btn{0}'))
    for i in range(1, lenght):
        board_2.add(InlineKeyboardButton(f'{full[i][0]}', callback_data=f'btn{i}'))
    return board_2

def create_reply_keyboard():
    lenght = adm_collection.find().count()
    if lenght >= 4:
        board_4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=4).insert(KeyboardButton('1'))
    else:
        board_4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).insert(KeyboardButton('1'))
    for i in range(2, lenght+1):
        board_4.insert(KeyboardButton(f'{i}'))
    return board_4
    
def create_reply_keyboard_1():
    butt_list = ['Фамилия', 'Имя', 'Отчество', 'Кабинет', 'Телефон', 'Email']
    board_5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).insert(KeyboardButton('Должность'))
    for i in butt_list:
        board_5.insert(KeyboardButton(f'{i}'))
    return board_5