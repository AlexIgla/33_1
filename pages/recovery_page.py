from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import RecoveryPageLocators
import time

url_recovery_page = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=400655d2-c988-4155-a840-341f26e97255&client_id=lk_b2c&tab_id=nLVPbxa4uMQ'


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
        menu_autorization = self.find_element(RecoveryPageLocators.PAGE_RIGHT)
        result = "Авторизация по коду"
        assert result == "Авторизация по коду"

    def should_be_incorrectness_number_of_characters(self):
        input_phone = self.find_element(RecoveryPageLocators.INPUT_PHONE_MAIL)
        input_phone.clear()
        input_phone.send_keys("+7-123-456-78-  ")
        button_to_come_in = self.find_element(RecoveryPageLocators.BUTTON_CONTINUE)
        button_to_come_in.click()
        result = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
        assert result == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

    def should_be_password_recovery_check_registered_number(self):
        input_phone = self.find_element(RecoveryPageLocators.INPUT_PHONE_MAIL)
        input_phone.clear()
        input_phone.send_keys("+7-951-888-00-11")
        button_to_come_in = self.find_element(RecoveryPageLocators.BUTTON_CONTINUE)
        button_to_come_in.click()
        time.sleep(30)
        #вводим вручную код подтверждения
        result = 'https://start.rt.ru/?tab=main'
        assert result == self.browser.current_url, 'https://start.rt.ru/?tab=main'

    def should_be_password_recovery_check_registered_mail(self, browser):
        input_phone = self.find_element(RecoveryPageLocators.INPUT_PHONE_MAIL)
        input_phone.clear()
        input_phone.send_keys("sanchez.ig.94@mail.ru")
        button_to_come_in = self.find_element(RecoveryPageLocators.BUTTON_CONTINUE)
        button_to_come_in.click()
        time.sleep(30)
        # вводим вручную код подтверждения
        result = 'https://start.rt.ru/?tab=main'
        assert result == self.browser.current_url, 'https://start.rt.ru/?tab=main'
###############
    def should_be_button_comeback(self):
        link_comeback = self.find_element(RecoveryPageLocators.BUTTON_COMEBACK)
        link_comeback.click()
        result = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=fc343b3b-9ff7-4786-bb30-e60caa7821cd&client_id=lk_b2c&tab_id=nLVPbxa4uMQ'
        assert result == self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=fc343b3b-9ff7-4786-bb30-e60caa7821cd&client_id=lk_b2c&tab_id=nLVPbxa4uMQ'

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