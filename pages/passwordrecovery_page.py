from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import PasswordRecoveryPageLocators
from selenium.webdriver.common.by import By
import pytest

url_passwordrecovery_page = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=v35qbq1RL4I'


class PasswordRecoveryPage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        # команда для неявного ожидания со значением по умолчанию в 5c:
        self.browser.implicitly_wait(timeout)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def open(self):
        self.browser.get(self.url)

    # Номер тест-кейсов по порядку TRK-028

    def should_be_newpassword_field_correctness(self):
        input_password_new = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_NEW)
        input_password_new.clear()
        input_password_new.send_keys('123')
        input_password_confirm = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_CONFIRM)
        input_password_confirm.click()
        result = input_password_new.number
        assert result == "Длина пароля должна быть не менее 8 символов"

    def should_be_newpassword_passwordconfirm_field_correctness(self):
        input_password_new = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_NEW)
        input_password_new.clear()
        input_password_new.sendkeys('AzwX1223')
        input_password_confirm = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_CONFIRM)
        input_password_confirm.clear()
        input_password_confirm.sendkeys('AzwX1244')
        button_save = self.find_element(PasswordRecoveryPageLocators.BUTTON_SAVE)
        button_save.click()
        result = input_password_new.text, input_password_confirm.text
        assert result == "Пароли не совпадают"

    def should_be_newpassword_passwordconfirm_field_correctness(self):
        input_password_new = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_NEW)
        input_password_new.clear()
        input_password_new.sendkeys('AzwX1223')
        input_password_confirm = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_CONFIRM)
        input_password_confirm.clear()
        input_password_confirm.sendkeys('azwX1223')
        button_save = self.find_element(PasswordRecoveryPageLocators.BUTTON_SAVE)
        button_save.click()
        result = input_password_new.text, input_password_confirm.text
        assert result == "Пароль должен содержать хотя бы одну заглавную букву"

    def should_be_button_save(self):
        button_save = self.find_element(PasswordRecoveryPageLocators.BUTTON_SAVE)
        button_save.click()
        self.browser.current_url = result
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=v35qbq1RL4I'
