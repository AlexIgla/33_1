from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import MainPageLocators, RegistrationPageLocators
from selenium.webdriver.common.by import By
import pytest


class RegistrationPage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        # команда для неявного ожидания со значением по умолчанию в 5c:
        self.browser.implicitly_wait(timeout)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def open(self):
        self.browser.get(self.url)

    def should_be_register_link(self):
        enter_pass = self.find_element(RegistrationPageLocators.ENTER_PASS)
        enter_pass.click()
        link = self.find_element(RegistrationPageLocators.LINK_REGISTER)
        result = link
        assert result

    def should_be_field_first_name_correctness(self):
        enter_pass = self.find_element(RegistrationPageLocators.ENTER_PASS)
        enter_pass.click()
        link = self.find_element(RegistrationPageLocators.LINK_REGISTER)
        link.click()
        input_first_name = self.find_element(RegistrationPageLocators.INPUT_FIRST_NAME)
        input_first_name.clear()
        input_first_name.send_keys('As')
        button_register = self.find_element(RegistrationPageLocators.BUTTON_PAGE_REGISTER)
        button_register.click()
        register_form = self.find_element(RegistrationPageLocators.REGISTER_FORM)
        result = register_form.text
        assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." == result

    def should_be_field_address_correctness(self):
        input_address = self.find_element(RegistrationPageLocators.INPUT_ADDRESS)
        input_address.clear()
        input_address.send_keys("+7-123-456-78-  ")
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
        input_password = self.find_element(RegistrationPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys('')
        input_password.click()
        result = input_password.text
        assert result == "Длина пароля должна быть не менее 8 символов"

    def should_be_password_confirm_field_correctness(self):
        input_password_confirm = self.find_element(RegistrationPageLocators.INPUT_PASSWORD_CONFIRM)
        input_password_confirm.clear()
        input_password_confirm.send_keys('562312589')
        input_password_confirm.click()
        result = input_password_confirm.number
        assert result == "Пароль должен содержать хотя бы одну заглавную букву"

    # Негативный тест TRK-038

    def should_be_check_telefone_sending_sms(self):
        input_first_name = self.find_element(RegistrationPageLocators.INPUT_FIRST_NAME)
        input_first_name.clear()
        input_first_name.send_keys("Александр")
        input_last_name = self.find_element(RegistrationPageLocators.INPUT_LAST_NAME)
        input_last_name.clear()
        input_last_name.send_keys("Игольников")
        input_phone = self.find_element(RegistrationPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("+7-123-456-78-90")
        input_password = self.find_element(RegistrationPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("AzwX1223")
        input_password_confirm.clear()
        input_password_confirm.send_keys('AzwX1223')
        region_list.click()
        region_list.send_keys('Саратовская обл')
        button_register = self.find_element(RegistrationPageLocators.BUTTON_PAGE_REGISTER)
        button_register.click()
        self.browser.current_url = result
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?session_code=_wuyzycVJSBcUCuN3-ERdHs8g3kAwq--5yR9XvW6Wlo&execution=c0660f76-7bb7-44a8-9df9-b3198f38f550&client_id=account_b2c&tab_id=qvLQ10JRuKg'


url_registration_page = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?response_type=code&scope=openid&client_id=lk_b2c&redirect_uri=https%3A%2F%2Flk-api.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps%253A%252F%252Flk.rt.ru%252F&state=%7B%22uuid%22%3A%22AA2F2F32-0DC5-4B1E-840D-D26E7EE6A84A%22%7D'