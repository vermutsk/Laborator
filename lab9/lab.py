from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

driver = Chrome()
driver.get('https://wwww.farpost.ru/vladivostok/realty/sell_flats/?page=1')

#возвращает список
content = driver.find_elements_by_class_name('bull-item-content')
if len(content)==0:
    print('не найдено таблиц с данными')
    exit()
