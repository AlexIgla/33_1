from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import RegistrationPageLocators
import time

url_registration_page = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=lk_b2c&tab_id=vrMKSwMQTG0'


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

    # EXP-030
    def should_be_register_link(self):
        enter_pass = self.find_element(RegistrationPageLocators.ENTER_PASS)
        enter_pass.click()
        link = self.find_element(RegistrationPageLocators.LINK_REGISTER)
        assert link

    # EXP-031
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
        register_form.click()
        result = "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
        assert result

    # EXP-032
    def should_be_field_address_correctness(self):
        enter_pass = self.find_element(RegistrationPageLocators.ENTER_PASS)
        enter_pass.click()
        link = self.find_element(RegistrationPageLocators.LINK_REGISTER)
        link.click()
        input_address = self.find_element(RegistrationPageLocators.INPUT_PHONE_MAIL)
        input_address.clear()
        input_address.send_keys("+7-123-456-78-  ")
        button_register = self.find_element(RegistrationPageLocators.BUTTON_PAGE_REGISTER)
        button_register.click()
        register_form = self.find_element(RegistrationPageLocators.REGISTER_FORM)
        register_form.click()
        result = "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
        assert result

    # EXP-033
    def should_be_region_list(self):
        enter_pass = self.find_element(RegistrationPageLocators.ENTER_PASS)
        enter_pass.click()
        link = self.find_element(RegistrationPageLocators.LINK_REGISTER)
        link.click()
        result = "Регион"
        assert result

    # EXP-034
    def should_be_password_field_correctness(self):
        enter_pass = self.find_element(RegistrationPageLocators.ENTER_PASS)
        enter_pass.click()
        link = self.find_element(RegistrationPageLocators.LINK_REGISTER)
        link.click()
        input_password = self.find_element(RegistrationPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys('')
        button_register = self.find_element(RegistrationPageLocators.BUTTON_PAGE_REGISTER)
        button_register.click()
        result = "Длина пароля должна быть не менее 8 символов"
        assert result

    # EXP-035
    def should_be_password_confirm_field_correctness(self):
        enter_pass = self.find_element(RegistrationPageLocators.ENTER_PASS)
        enter_pass.click()
        link = self.find_element(RegistrationPageLocators.LINK_REGISTER)
        link.click()
        input_password_confirm = self.find_element(RegistrationPageLocators.INPUT_PASSWORD_CONFIRM)
        input_password_confirm.clear()
        input_password_confirm.send_keys('562312589')
        button_register = self.find_element(RegistrationPageLocators.BUTTON_PAGE_REGISTER)
        button_register.click()
        result = "Пароль должен содержать хотя бы одну заглавную букву"
        assert result

    # EXP-036
    def should_be_check_telefone_sending_sms(self):
        enter_pass = self.find_element(RegistrationPageLocators.ENTER_PASS)
        enter_pass.click()
        link = self.find_element(RegistrationPageLocators.LINK_REGISTER)
        link.click()
        input_first_name = self.find_element(RegistrationPageLocators.INPUT_FIRST_NAME)
        input_first_name.clear()
        input_first_name.send_keys("Александр")
        input_last_name = self.find_element(RegistrationPageLocators.INPUT_LAST_NAME)
        input_last_name.clear()
        input_last_name.send_keys("Игольников")
        input_phone = self.find_element(RegistrationPageLocators.INPUT_PHONE_MAIL)
        input_phone.clear()
        input_phone.send_keys("+7-123-456-78-90")
        input_password = self.find_element(RegistrationPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("AzwX1223")
        input_password_confirm = self.find_element(RegistrationPageLocators.INPUT_PASSWORD)
        input_password_confirm.clear()
        input_password_confirm.send_keys('AzwX1223')
        button_register = self.find_element(RegistrationPageLocators.BUTTON_PAGE_REGISTER)
        button_register.click()
        result = self.browser.current_url, 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?execution=c0660f76-7bb7-44a8-9df9-b3198f38f550&client_id=lk_b2c&tab_id=_EaiPsaZEzw'
        assert result
