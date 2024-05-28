from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import MainPageLocators, RecoveryPageLocators, RegistrationPageLocators, PasswordRecoveryPageLocators
from selenium.webdriver.common.by import By
import pytest

url_passwordrecovery_page = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/required-action?execution=UPDATE_PASSWORD '


class PasswordRecoveryPage():

    # Номер тест-кейсов по порядку TRK-028

    def should_be_newpassword_field_correctness(self):
        input_password_new = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_NEW)
        input_password_new.clear()
        input_password_new.send_keys('123')
        input_password_confirm = self.find_element(PasswordRecoveryPageLocators.INPUT_PASSWORD_CONFIRM)
        input_password_confirm.click()
        result = input_newpassword.number
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
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=P2FZFyPlzzE'
