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
        main_page.should_be_incorrectness_number_of_characters()

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