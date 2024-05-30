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
    ENTER_PASS = (By.ID, 'standard_auth_btn')#OK
    LINK_REGISTER = (By.ID, "kc-register")#OK
    INPUT_FIRST_NAME = (By.NAME, "firstName")#OK
    BUTTON_PAGE_REGISTER = (By.NAME, "register")#OK
    INPUT_PHONE_MAIL = (By.ID, "address")#OK
    INPUT_LAST_NAME = (By.NAME, "lastName")#OK
    INPUT_PASSWORD = (By.ID, "password")#OK
    INPUT_PASSWORD_CONFIRM = (By.ID, "password-confirm")#OK
    REGISTER_FORM = (By.NAME, 'register')#OK

