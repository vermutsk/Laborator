import time
import json
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

driver = Chrome()
home = 'https://wwww.farpost.ru/vladivostok/realty/sell_flats/?page='

#70 страниц

for i in range(1, 70):
    page = home + str(i)
    driver.get(page)

    content = driver.find_elements_by_class_name('pageableContent')
    if len(content)==0:
        print('не найдено таблиц с данными')
        exit()

    content = content[0]
    flats = content.find_elements_by_class_name('bull-item-content')

    results = []
    for elem in flats:
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

        driver.close()
        driver.switch_to.window(flat_list_handler)
        print(json.dumps(tmp, ensure_ascii=False, indent=4))
        time.sleep(10)


