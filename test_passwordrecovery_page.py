from pages.passwordrecovery_page import PasswordRecoveryPage, url_passwordrecovery_page
import pytest
from confest import browser


# Тесты идут по порядку

@pytest.mark.passwordrecovery_page
class TestBodyFromPasswordRecoveryPage():
    def test_should_be_newpassword_field_correctness(self, browser):
        main_page = PasswordRecoveryPage(browser, url_passwordrecovery_page)
        main_page.open()
        main_page.should_be_newpassword_field_correctness()

    def test_should_be_newpassword_passwordconfirm_field_correctness(self, browser):
        main_page = PasswordRecoveryPage(browser, url_passwordrecovery_page)
        main_page.open()
        main_page.should_be_newpassword_passwordconfirm_field_correctness()

    def test_should_be_newpassword_passwordconfirm_field_correctness(self, browser):
        main_page = PasswordRecoveryPage(browser, url_passwordrecovery_page)
        main_page.open()
        main_page.should_be_newpassword_passwordconfirm_field_correctness()

    def should_be_button_save(self, browser):
        main_page = PasswordRecoveryPage(browser, url_passwordrecovery_page)
        main_page.open()
        main_page.should_be_button_save()
