from pages.recovery_page import RecoveryPage, url_recovery_page
import pytest
from confest import browser


# Тесты идут по порядку

@pytest.mark.recovery_page
class TestBodyFromRecoveryPage():
    def test_should_be_recovery_form(self, browser):
        main_page = RecoveryPage(browser, url_recovery_page)
        main_page.open()
        main_page.should_be_recovery_form()

    def test_should_be_incorrectness_number_of_characters(self, browser):
        main_page = RecoveryPage(browser, url_recovery_page)
        main_page.open()
        main_page.should_be_correctness_number_of_characters()

    def test_should_be_password_recovery_check_registered_number(self, browser):
        main_page = RecoveryPage(browser, url_recovery_page)
        main_page.open()
        main_page.should_be_password_recovery_check_registered_number()

    def test_should_be_password_recovery_check_registered_mail(self, browser):
        main_page = RecoveryPage(browser, url_recovery_page)
        main_page.open()
        main_page.should_be_password_recovery_check_registered_mail()

    def test_should_be_button_comeback(self, browser):
        main_page = RecoveryPage(browser, url_recovery_page)
        main_page.open()
        main_page.should_be_button_comeback()

        # pytest -v --tb=line -m test_recovery_page.py

    def test_should_be_button_continue(browser):
        main_page = RecoveryPage(browser, url_recovery_page)
        main_page.open()
        main_page.should_be_correctness_number_of_characters()

    def test_should_be_button_comeback_main_page(browser):
        main_page = RecoveryPage(browser, url_recovery_page)
        main_page.open()
        main_page.should_be_button_comeback_main_page()

    def test_should_be_mail_field_correctness(browser):
        main_page = RecoveryPage(browser, url_recovery_page)
        main_page.open()
        main_page.should_be_mail_field_correctness()
