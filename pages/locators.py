from selenium.webdriver.common.by import By


class MainPageLocators:
    PAGE_RIGHT = (By.ID, "card-title")  # OK
    FORM_AUTORIZATION = (By.CLASS_NAME, "login-form")  # OK
    PAGE_LEFT = (By.ID, "page-left")  # OK
    TAB_PHONE = (By.ID, "t-btn-tab-phone")  # OK
    TAB_MAIL = (By.ID, "t-btn-tab-mail")  # OK
    TAB_LOGIN = (By.ID, "t-btn-tab-login")  # OK
    TAB_LS = (By.ID, "t-btn-tab-ls")  # OK
    INPUT_PHONE = (By.ID, "username")  # OK
    INPUT_PASSWORD = (By.ID, "password")  # OK
    BUTTON_TO_COME_IN = (By.ID, "kc-login")  # OK
    INPUT_LS = (By.ID, "username")  # OK
    INPUT_LOGIN = (By.ID, "username")  # OK
    INPUT_MAIL = (By.ID, "username")  # OK


class RecoveryPageLocators():
    PAGE_RIGHT = (By.ID, "card-title")#OK
    INPUT_PHONE_MAIL = (By.ID, "address")#OK
    BUTTON_COMEBACK = (By.ID, "standard_auth_btn")#OK
    BUTTON_CONTINUE = (By.ID, "otp_get_code")#OK


class PasswordRecoveryPageLocators():
    FORGOT_PASSWORD = (By.ID, 'forgot_password')#OK
    INPUT_PHONE = (By.ID, "username")#OK
    RESET_BUTTON = (By.ID, 'reset')#OK
    PHONE = (By.CLASS_NAME, 'rt-radio__circle')#OK
    RESET_FORM_BUTTON = (By.ID, 'reset-form-submit')#OK
    INPUT_PASSWORD_NEW = (By.ID, "password-new")#OK
    INPUT_PASSWORD_CONFIRM = (By.ID, "password-confirm")#OK
    BUTTON_SAVE = (By.ID, "t-btn-reset-pass")#OK


class RegistrationPageLocators():
    ENTER_PASS = (By.ID, 'standard_auth_btn')  # OK
    LINK_REGISTER = (By.ID, "kc-register")  # OK
    INPUT_FIRST_NAME = (By.CLASS_NAME, "rt-input__input rt-input__input--rounded rt-input__input--orange")#OK
    BUTTON_PAGE_REGISTER = (By.CLASS_NAME, "rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded register-form__reg-btn")#OK
    INPUT_PHONE_MAIL = (By.ID, "address")  # OK
    PAGE_LEFT = (By.ID, "page-left")
    INPUT_LAST_NAME = (By.CLASS_NAME, "rt-input__input rt-input__input--rounded rt-input__input--orange")
    REGION_LIST = (By.CLASS_NAME, "rt-base-icon rt-base-icon--fill-path rt-select__arrow")
    INPUT_PASSWORD = (By.ID, "password")
    INPUT_PASSWORD_CONFIRM = (By.ID, "password-confirm")
    REGISTER_FORM = (By.CLASS_NAME, 'rt-input-container__meta rt-input-container__meta--error')

