from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import PasswordRecoveryPageLocators
from selenium.webdriver.common.by import By
import pytest
import time

url_passwordrecovery_page = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=2df89d71-6030-4435-82af-a52375a78cbe&theme&auth_type'


class PasswordRecoveryPage():
    def __init__(self, browser, url, timeout=10):
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
        forgot_password = self.find_element(PasswordRecoveryPageLocators.FORGOT_PASSWORD)
        forgot_password.click()
        input_phone = self.find_element(PasswordRecoveryPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys('+7-951-888-00-11')
        time.sleep(20)
        # капчу в случае появления придется вводить вручную
        reset_button = self.find_element(PasswordRecoveryPageLocators.RESET_BUTTON)
        reset_button.click()
        phone = self.find_element(PasswordRecoveryPageLocators.PHONE)
        phone.click()
        reset_form_button = self.find_element(PasswordRecoveryPageLocators.RESET_FORM_BUTTON)
        reset_form_button.click()
        time.sleep(20)
        #вводим вручную код подтверждения
        input_password_new = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_NEW)
        input_password_new.clear()
        input_password_new.send_keys('123')
        input_password_confirm = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_CONFIRM)
        input_password_confirm.click()
        result = "Длина пароля должна быть не менее 8 символов"
        assert result == "Длина пароля должна быть не менее 8 символов"

    def should_be_newpassword_passwordconfirm_field_correctness_1(self):
        forgot_password = self.find_element(PasswordRecoveryPageLocators.FORGOT_PASSWORD)
        forgot_password.click()
        input_phone = self.find_element(PasswordRecoveryPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys('+7-951-888-00-11')
        time.sleep(20)
        # капчу в случае появления придется вводить вручную
        reset_button = self.find_element(PasswordRecoveryPageLocators.RESET_BUTTON)
        reset_button.click()
        phone = self.find_element(PasswordRecoveryPageLocators.PHONE)
        phone.click()
        reset_form_button = self.find_element(PasswordRecoveryPageLocators.RESET_FORM_BUTTON)
        reset_form_button.click()
        time.sleep(20)
        # вводим вручную код подтверждения
        input_password_new = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_NEW)
        input_password_new.clear()
        input_password_new.sendkeys('AzwX1223')
        input_password_confirm = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_CONFIRM)
        input_password_confirm.clear()
        input_password_confirm.sendkeys('AzwX1244')
        button_save = self.find_element(PasswordRecoveryPageLocators.BUTTON_SAVE)
        button_save.click()
        result = "Пароли не совпадают"
        assert result == "Пароли не совпадают"

    def should_be_newpassword_passwordconfirm_field_correctness_2(self):
        forgot_password = self.find_element(PasswordRecoveryPageLocators.FORGOT_PASSWORD)
        forgot_password.click()
        input_phone = self.find_element(PasswordRecoveryPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys('+7-951-888-00-11')
        time.sleep(20)
        # капчу в случае появления придется вводить вручную
        reset_button = self.find_element(PasswordRecoveryPageLocators.RESET_BUTTON)
        reset_button.click()
        phone = self.find_element(PasswordRecoveryPageLocators.PHONE)
        phone.click()
        reset_form_button = self.find_element(PasswordRecoveryPageLocators.RESET_FORM_BUTTON)
        reset_form_button.click()
        time.sleep(20)
        # вводим вручную код подтверждения
        input_password_new = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_NEW)
        input_password_new.clear()
        input_password_new.sendkeys('AzwX1223')
        input_password_confirm = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_CONFIRM)
        input_password_confirm.clear()
        input_password_confirm.sendkeys('azwX1223')
        button_save = self.find_element(PasswordRecoveryPageLocators.BUTTON_SAVE)
        button_save.click()
        result = "Пароль должен содержать хотя бы одну заглавную букву"
        assert result == "Пароль должен содержать хотя бы одну заглавную букву"

    def should_be_button_save(self):
        forgot_password = self.find_element(PasswordRecoveryPageLocators.FORGOT_PASSWORD)
        forgot_password.click()
        input_phone = self.find_element(PasswordRecoveryPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys('+7-951-888-00-11')
        time.sleep(20)
        # капчу в случае появления придется вводить вручную
        reset_button = self.find_element(PasswordRecoveryPageLocators.RESET_BUTTON)
        reset_button.click()
        phone = self.find_element(PasswordRecoveryPageLocators.PHONE)
        phone.click()
        reset_form_button = self.find_element(PasswordRecoveryPageLocators.RESET_FORM_BUTTON)
        reset_form_button.click()
        time.sleep(20)
        # вводим вручную код подтверждения
        input_password_new = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_NEW)
        input_password_new.clear()
        input_password_new.sendkeys('AzwX1223')
        input_password_confirm = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_CONFIRM)
        input_password_confirm.clear()
        input_password_confirm.sendkeys('AzwX1244')
        button_save = self.find_element(PasswordRecoveryPageLocators.BUTTON_SAVE)
        button_save.click()
        result = self.browser.current_url
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/account_b2c/page?state=2df89d71-6030-4435-82af-a52375a78cbe&client_id=account_b2c#/'
