import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from config import CHROME_DRIVER_EXE

browser: webdriver.Chrome = None

# Не инициализируем дважды браузер
if browser is None:
    browser = webdriver.Chrome(executable_path=CHROME_DRIVER_EXE)
    browser.implicitly_wait(5)
    browser.maximize_window()


def browser_get(url: str):
    time.sleep(1)
    browser.get(url)

    pause_on_captcha_page()


def set_data_form(data: dict[str, object]):
    for name in data:
        value: object = data[name]
        elements = browser.find_elements(By.NAME, name)

        for index in range(0, len(elements)):

            if type(value) is str:
                browser.execute_script(f"document.getElementsByName('{name}')[{index}].value = '{value}';")
            elif type(value) is bool:
                browser.execute_script(f"document.getElementsByName('{name}')[{index}].checked = {'true' if value else 'false'};")


def pause_on_captcha_page():
    if 'page_captcha.asp' not in browser.current_url:
        return

    time.sleep(2)
    return pause_on_captcha_page()


def pause_on_loading_page():
    elements = browser.find_elements(By.ID, 'loading')

    if len(elements) == 0:
        return

    loading = browser.find_element(By.ID, 'loading')

    if 'none' in loading.value_of_css_property('display'):
        return

    time.sleep(1.5)
    return pause_on_loading_page()
