# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
sbis_site = 'https://sbis.ru/'
tensor_site = 'https://tensor.ru/'

try:
    driver.get(sbis_site)
    time.sleep(1)
    assert driver.current_url == sbis_site, 'Неверный url'
    contacts_link = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-link[href="/contacts"]')
    contacts_link.click()
    time.sleep(1)
    tensor_logo = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__logo-link')
    tensor_logo.click()
    time.sleep(1)
    driver.get(tensor_site)
    time.sleep(1)
    assert driver.current_url == tensor_site, 'Неверный url'
    content_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    content_block.location_once_scrolled_into_view
    assert content_block.is_displayed(), 'Блок не отображается'
    content_block_link = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-link')
    content_block_link.click()
    time.sleep(1)
    assert driver.current_url == 'https://tensor.ru/about', 'Неверный url'
finally:
    driver.quit()