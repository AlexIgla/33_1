from pages.main_page import MainPage, url_main_page
from pages.locators import MainPageLocators, RecoveryPageLocators, RegistrationPageLocators
import pytest
from confest import browser


# Тесты по порядку

def test_should_be_menu_autorization(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_be_menu_autorization()


def test_should_be_form_autorization(browser):
    main_page = MainPage(browser, url_main_page)
    main_page.open()
    main_page.should_be_form_autorization()


@pytest.mark.main_page
class TestBodyFromMainPage():
    def test_should_be_product_slogan(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_product_slogan()

    def test_should_be_tab_click_telefon(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_tab_click_telefon()

    def test_should_be_mobile_number_field_incorrectness(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_mobile_number_field_incorrectness()

    def test_should_be_password_field_incorrectness(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_password_field_incorrectness()

        # pytest -v --tb=line -m test_main_page.py

    def test_should_be_correctness_number_of_characters(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_correctness_number_of_characters()

    def test_should_be_autorization_by_a_registraited_user(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_autorization_by_a_registraited_user()

    def test_should_be_tab_click_mail(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_tab_click_mail()

    def test_should_be_mail_field_correctness(self, browser):
        main_page = MainPage(browser, url_main_page)
        main_page.open()
        main_page.should_be_mail_field_correctness()
