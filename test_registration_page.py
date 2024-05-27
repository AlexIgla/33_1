from .pages.registration_page import RegistrationPage, url_registration_page
import pytest

#Тесты идут по порядку

@pytest.mark.registration_page

class TestBodyFromRegistrationPage():
    def test_should_be_register_link(self, browser):
        main_page = RegistrationPage(browser, url_registration_page)
        main_page.open()
        main_page.should_be_register_link()
    def test_should_be_field_first_name_correctness(self, browser):
        main_page = RegistrationPage(browser, url_registration_page)
        main_page.open()
        main_page.should_be_field_first_name_correctness()
    def test_should_be_field_address_correctness(self, browser):
        main_page = RegistrationPage(browser, url_registration_page)
        main_page.open()
        main_page.should_be_field_address_correctness()
    def test_should_be_region_list(self, browser):
        main_page = RegistrationPage(browser, url_registration_page)
        main_page.open()
        main_page.should_be_region_list()
    def test_should_be_password_field_correctness(self, browser):
        main_page = RegistrationPage(browser, url_registration_page)
        main_page.open()
        main_page.should_be_password_field_correctness()

        # pytest -v --tb=line -m test_registration_page.py

    def test_should_be_password_confirm_field_correctness(browser):
        main_page = RegistrationPage(browser, url_registration_page)
        main_page.open()
        main_page.should_be_password_confirm_field_correctness()

    def test_should_be_check_telefone_sending_sms(browser):
       main_page = RegistrationPage(browser, url_registration_page)
       main_page.open()
       main_page.should_be_check_telefone_sending_sms()