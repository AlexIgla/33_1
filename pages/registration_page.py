from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, RecoveryPageLocators, RegistrationPageLocators, PasswordRecoveryPageLocators
from selenium.webdriver.common.by import By
import pytest


class RegistrationPage():

    def should_be_register_link(self):
        link = self.find_element(MainPageLocators.LINK_REGISTER)
        result = link.text
        assert "Зарегистрироваться" == result

    def should_be_field_first_name_correctness(self):
        input_first_name = self.find_element(RegistrationPageLocators.INPUT_FIRST_NAME)
        input_first_name.clear()
        input_first_name.send_keys('Df')
        button_register = self.find_element(RegistrationPageLocators.BUTTON_PAGE_REGISTER)
        button_register.click()
        result = input_first_name.text
        assert result == "Необходимо заполнить поле кириллицей. От 2 до 30 символов"

    def should_be_field_address_correctness(self):
        input_address = self.find_element(RegistrationPageLocators.INPUT_ADDRESS)
        input_address.clear()
        input_address.send_keys("+7-111-123-45-  ")
        button_page_register = self.find_element(RegistrationPageLocators.BUTTON_PAGE_REGISTER)
        button_page_register.click()
        result = input_address.number
        assert result == "Сообщение Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX"

    def should_be_region_list(self):
        region_list = self.find_elements(RegistrationPageLocators.REGION_LIST)
        region_list.click()
        result = region_list.text
        assert result == "Регион"

    def should_be_password_field_correctness(self):
        input_password = self.find_element(RegistrationPageLocator.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys('')
        input_password.click()
        result = input_password.text
        assert result == "Длина пароля должна быть не менее 8 символов"

    def should_be_password_confirm_field_correctness(self):
        input_password_confirm = self.find_element(RegistrationPageLocators.INPUT_PASSWORD_CONFIRM)
        input_password_confirm.clear()
        input_password_confirm.send_keys('5623')
        input_password_confirm.click()
        result = input_password_confirm.number
        assert result == "Пароль должен содержать хотя бы одну заглавную букву"

    # Негативный тест TRK-038

    def should_be_check_telefone_sending_sms(self):
        input_first_name = self.find_element(RegistrationPageLocators.INPUT_FIRST_NAME)
        input_first_name.clear()
        input_first_name.send_keys("Евлампий")
        input_last_name = self.find_element(RegistrationPageLocators.INPUT_LAST_NAME)
        input_last_name.clear()
        input_last_name.send_keys("Титьков")
        input_phone = self.find_element(RegistrationPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("+7-111-123-45-67")
        input_password = self.find_element(RegistrationPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("REGnum678")
        input_password_confirm.clear()
        input_password_confirm.send_keys('REGnum678')
        region_list.click()
        region_list.send_keys('Ярославская обл')
        button_register = self.find_element(RegistrationPageLocators.BUTTON_REGISTER)
        button_register.click()
        self.browser.current_url = result
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?session_code=_wuyzycVJSBcUCuN3-ERdHs8g3kAwq--5yR9XvW6Wlo&execution=c0660f76-7bb7-44a8-9df9-b3198f38f550&client_id=account_b2c&tab_id=qvLQ10JRuKg'
