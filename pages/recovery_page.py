from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import RecoveryPageLocators
from selenium.webdriver.common.by import By
import pytest


class RecoveryPage():
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

    # Номер тест-кейсов по порядку EXP-020.....

    def should_be_recovery_form(self):
        recovery_form = self.find_element(RecoveryPageLocators.RECOVERY_FORM)
        result = recovery_form.text
        assert result == "Форма"

    def should_be_correctness_number_of_characters(self):
        input_phone = self.find_element(RecoveryPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("+7-123-456-78-  ")
        button_to_come_in = self.find_element(RecoveryPageLocators.BUTTON_CONTINUE)
        button_to_come_in.click()
        result = input_phone.number
        assert result == "Неверный формат номера"

    def should_be_password_recovery_check_registered_number(self):
        input_phone = self.find_element(RecoveryPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("+7-951-888-00-11")
        input_capcha = self.find_element(RecoveryPageLocators.INPUT_CAPCHA)
        input_capcha.clear()
        input_capcha.send_keys("PAun7GUV")
        button_to_come_in = self.find_element(RecoveryPageLocators.BUTTON_CONTINUE)
        button_to_come_in.click()
        self.browser.current_url = result
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?session_code=RpQteafuCWnxWZkmsk_5CKEUoyfAR2x2PUPtFFEtfsQ&execution=1b1825d2-f76f-4706-8e25-4c71c1f7f120&client_id=account_b2c&tab_id=B8z6Ht7_4rs'

    def should_be_password_recovery_check_registered_mail(self, browser):
        input_mail = self.find_element(RecoveryPageLocators.INPUT_MAIL)
        input_mail.clear()
        input_mail.send_keys('sanchez.ig.94@mail.ru')
        input_capcha = self.find_element(RecoveryPageLocators.INPUT_CAPCHA)
        input_capcha.clear()
        input_capcha.send_keys("3QP8y44")
        button_continue = self.find_element(RecoveryPageLocators.BUTTON_CONTINUE)
        button_continue.click()
        self.browser.current_url = result
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?execution=7ca0b6f9-7c84-472b-94e2-a57c35eb6b08&client_id=account_b2c&tab_id=4JvtA2huco0'

    def should_be_button_comeback(self):
        link_comeback = self.find_element(RecoveryPageLocators.BUTTON_COMEBACK)
        link_comeback.click()
        self.browser.current_url = result
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?execution=1b1825d2-f76f-4706-8e25-4c71c1f7f120&client_id=account_b2c&tab_id=mHPSKFbKvLQ'

    def should_be_button_continue(self):
        input_mail = self.find_element(RecoveryPageLocators.INPUT_MAIL)
        input_mail.clear()
        input_mail.send_keys('sanchez.ig.94@mail.ru')
        input_capcha = self.find_element(RecoveryPageLocators.INPUT_CAPCHA)
        input_capcha.clear()
        input_capcha.send_keys("p8LApsy")
        button_continue = self.find_element(RecoveryPageLocators.BUTTON_CONTINUE)
        button_continue.click()
        self.browser.current_url = result
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?execution=7ca0b6f9-7c84-472b-94e2-a57c35eb6b08&client_id=account_b2c&tab_id=4JvtA2huco0'

    def should_be_button_comeback_main_page(self):
        button_comeback = self.find_element(RecoveryPageLocators.BUTTON_COMEBACK)
        button_comeback.click()
        self.browser.current_url = result
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?session_code=Y0VJ5ZrIyarhrjbmUPmjkjmFdYC9D6gD-rASQlwayCI&execution=1b1825d2-f76f-4706-8e25-4c71c1f7f120&client_id=account_b2c&tab_id=mHPSKFbKvLQ'

    # Негативный тест EXP-027
    def should_be_mail_field_correctness(self):
        input_mail = self.find_element(RecoveryPageLocators.INPUT_MAIL)
        input_mail.clear()
        input_mail.send_keys('йцук')
        button_continue = self.find_element(RecoveryPageLocators.BUTTON_CONTINUE)
        button_continue.click()
        tab_login = self.find_element(RecoveryPageLocators.TAB_LOGIN)
        result = tab_login.click()
        assert result == "Неверный логин или текст с картинки"


url_recovery_page = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?response_type=code&scope=openid&client_id=lk_b2c&redirect_uri=https%3A%2F%2Flk-api.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps%253A%252F%252Flk.rt.ru%252F&state=%7B%22uuid%22%3A%224C105560-C9EC-4ABB-86F8-373A0DABCA9B%22%7D'
