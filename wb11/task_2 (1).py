# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from time import sleep

fix_sbis_site = 'https://fix-online.sbis.ru/'

driver = webdriver.Chrome()
driver.maximize_window()
sleep(2)
try:
    driver.get(fix_sbis_site)
    sleep(3)
    user_login, user_password = 'лом', 'лом123'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(5)
    sections_contacts = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"]')
    sections_contacts.click()
    sleep(1)
    menu_contacts = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    menu_contacts.click()
    sleep(3)
    btn_plus = driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus')
    btn_plus.click()
    sleep(3)
    search_emp = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate__top-area-content input')
    search_emp.send_keys('Ломоносов Михаил')
    sleep(3)
    person = driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"][title="Ломоносов Михаил"]')
    person.click()
    sleep(3)
    text = 'Hello AT'
    message_text = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    message_text.send_keys(text)
    send = driver.find_element(By.CSS_SELECTOR, '.icon-BtArrow')
    send.click()
    sleep(3)
    message = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert message.text == text, "В реестре не отображается отправленное сообщение"
    action_chains = ActionChains(driver)
    action_chains.move_to_element(message)
    action_chains.perform()
    sleep(3)
    btn_delete_msg = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    btn_delete_msg.click()
    sleep(3)
    message = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert message.text != text, 'Сообщение не удалилось'
finally:
    driver.quit()