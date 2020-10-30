import time
import json
from pymongo import MongoClient
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

client = MongoClient("localhost", 27017) 
db = client['NEW_DB']
new_collection = db['hata_list']
driver = Chrome()
home = 'https://wwww.farpost.ru/vladivostok/realty/sell_flats/?page='

for i in range(1, 70):
    page = home + str(i)
    driver.get(page)

    content = driver.find_elements_by_class_name('pageableContent')
    if len(content)==0:
        print('не найдено таблиц с данными')
        exit()
    content = content[0]
    flats = content.find_elements_by_class_name('bull-item-content')
    
    for elem in flats:
        results = []
        link = elem.find_elements_by_class_name('bull-item__self-link')
        if len(link) == 0:
            print('не найдено ссылок')
            exit()
        tmp = {}
        tmp['url'] = link[0].get_attribute('href')

        price = elem.find_elements_by_class_name('price-block__price')
        if len(price) == 0:
            print('не найдено цены')
            price = ''
        else:
            price  = price[0].text
        tmp['цена'] = price

        annotation = elem.find_elements_by_class_name('bull-item__annotation-row')
        if len(annotation) == 0:
            print('не найдено описания')
            annotation = ''
        else:
            annotation  = annotation[0].text
        tmp['описание'] = annotation

        #glaz = elem.find_elements_by_class_name('nano-eye-text')
        #glaz = glaz[0].text
        #print(glaz)

        flat_list_handler = driver.current_window_handle
        driver.execute_script('window.open()')
        driver.switch_to.window(driver.window_handles[1])
        driver.get(tmp['url'])
        field_set = driver.find_element_by_id('fieldsetView')
        fields = field_set.find_elements_by_class_name('field')

        for field in fields:
            key = field.find_elements_by_class_name('label')
            value = field.find_elements_by_class_name('value')
            for i in range(len(key)):
                tmp[f'{key[i].text}'] = value[i].text
        results.append(tmp)

        #добавить проверку на совпадения в бд
        print(json.dumps(tmp, ensure_ascii=False, indent=4))
        js = new_collection.find({'url' : tmp['url']}, { '_id' : 0})
        one_doc = []
        for doc in js:
            for value in doc.values():
                one_doc.append(value)
        if len(one_doc) > 0:
            if one_doc[0] != tmp['url']:
                new_collection.insert_many(results)
        else:
            new_collection.insert_many(results)

        driver.close()
        driver.switch_to.window(flat_list_handler)
        time.sleep(10)


