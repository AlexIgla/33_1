from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pages.locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait


# создаем конструктор, который принимает browser — экземпляр webdriver.
# Указываем url, который будет использоваться для открытия страницы.
class MainPage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        # команда для неявного ожидания со значением по умолчанию в 5c:
        self.browser.implicitly_wait(timeout)

    # создаем метод find_element (ищет один элемент и возвращает его)
    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    # создаем метод find_elements (ищет множество элементов и возвращает в виде списка)
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    # метод open должен открывать нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)

    # метод is_element_present перехватывает исключение.
    # будет использоваться для проверки присутствия элемента на странице
    # В него будем передавать два аргумента: как искать и что искать.
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # метод is_not_element_present будет использоваться для проверки отсутствия элемента на странице
    def is_not_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((how, what)))
        except (TimeoutException):
            return True
        return False

    ####################### ДАЛЕЕ ИДУТ ОБЩИЕ ДЛЯ ВСЕХ СТРАНИЦ МЕТОДЫ ПРОВЕРОК #########################

    # Номер тест-кейсов по порядку EXP-002.....

    def should_be_menu_autorization(self):
        menu_autorization = self.find_element(MainPageLocators.PAGE_RIGHT)
        result = menu_autorization.text
        assert result == "Авторизация"

    def should_be_form_autorization(self):
        form_autorization = self.find_element(MainPageLocators.FORM_AUTORIZATION)
        result = form_autorization.text
        assert result == "ФОРМА"

    def should_be_product_slogan(self):
        product_slogan = self.find_element(MainPageLocators.PAGE_LEFT)
        result = product_slogan.text
        assert result == "Личный кабинет"

    def should_be_tab_click_telefon(self):
        tab = self.find_element(MainPageLocators.TAB_PHONE, TAB_MAIL, TAB_LOGIN, TAB_LS)
        tab.click()
        result = tab.text
        assert "Телефон" == result

    def should_be_tab_click_telefon(self):
        tab = self.find_element(MainPageLocators.TAB_PHONE)
        tab.click()
        result = tab.text
        assert "Телефон" == result

    def should_be_mobile_number_field_correctness(self):
        input_phone = self.find_element(MainPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("+7-123-456-78-90")
        button_to_come_in = self.find_element(MainPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()
        result = input_phone.number
        assert result == "Неверный логин или пароль"

    def should_be_field_correctness_phone_password(self):
        input_phone = self.find_element(MainPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("+7-123-456-78-90")
        input_password = self.find_element(MainPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("AzwX1223")
        button_to_come_in = self.find_element(MainPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()
        result = input_phone.number, input_password.text
        assert result == "Неверный логин или пароль"

    def should_be_correctness_number_of_characters(self):
        input_phone = self.find_element(MainPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("+7-123-456-78-  ")
        button_to_come_in = self.find_element(MainPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()
        result = input_phone.number
        assert result == "Неверный формат телефона"

    def should_be_autorization_by_a_registraited_user(self):
        input_phone = self.find_element(MainPageLocators.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("+7-951-888-00-11")
        input_password = self.find_element(MainPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("AzwX1223")
        button_to_come_in = self.find_element(MainPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()
        self.browser.current_url = result
        assert result == self.browser.current_url, 'https://start.rt.ru/?tab=main'

    def should_be_tab_click_mail(self):
        tab = self.find_element(MainPageLocators.TAB_MAIL)
        tab.click()
        result = tab.text
        assert "Почта" == result

    def should_be_mail_field_correctness(self):
        input_mail = self.find_element(MainPageLocators.INPUT_MAIL)
        input_mail.clear()
        input_mail.send_keys('ва')
        button_to_come_in = self.find_element(MainPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()
        result = input_mail.text
        assert result == "Неверный логин или пароль"

    def should_be_autorization_by_mail_a_unregistraited_user(self):
        input_mail = self.find_element(MainPageLocators.INPUT_MAIL)
        input_mail.clear()
        input_mail.send_keys("qwerty@mail.ru")
        input_password = self.find_element(MainPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("AzwX1223")
        button_to_come_in = self.find_element(MainPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()
        result = input_mail.text, input_password.text
        assert result == "Неверный логин или пароль"

    def should_be_tab_click_login(self):
        tab = self.find_element(MainPageLocators.TAB_LOGIN)
        tab.click()
        result = tab.text
        assert "Логин" == result

    def should_be_login_field_correctness(self):
        input_login = self.find_element(MainPageLocators.INPUT_LOGIN)
        input_login.clear()
        input_login.send_keys('йцук')
        button_to_come_in = self.find_element(MainPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()
        result = input_login.text
        assert result == "Неверный логин или пароль"

    def should_be_login_field(self):
        input_login = self.find_element(MainPageLocators.INPUT_LOGIN)
        input_login.clear()
        yield input_login.click()
        result = input_login.text
        assert result == "Укажите логин указанный при регистрации"

    def should_be_field_login_plus_password_correctness(self):
        input_login = self.find_element(MainPageLocators.INPUT_LOGIN)
        input_login.clear()
        input_login.send_keys('rtkid_171627802083')
        input_password = self.find_element(MainPageLocators.INPUT_PASSWORD)
        input_password.clear()
        input_password.send_keys("AzwX1223")
        button_to_come_in = self.find_element(MainPageLocators.BUTTON_TO_COME_IN)
        button_to_come_in.click()
        result = input_login.text, input_password.text
        assert result == "Неверный логин или пароль"

    def should_be_ls_field_correctness(self):
        input_ls = self.find_element(MainPageLocators.INPUT_LS)
        input_ls.clear()
        input_ls.send_keys('123456____')
        result = input_ls.text
        assert result == "Проверьте, пожалуйста, номер лицевого счета"

    def should_be_ls_field(self):
        input_ls = self.find_element(MainPageLocators.INPUT_LOGIN)
        input_ls.clear()
        yield input_ls.click()
        result = input_ls.text
        assert result == "Проверьте, пожалуйста, номер лицевого счета"


url_main_page = "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=cb376b9f-59e8-4feb-9c37-5514d8a10e14&theme=light&auth_type"
