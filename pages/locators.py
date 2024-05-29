from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO_RTK = (By.CLASS_NAME, "rt-logo main-header__logo")
    PAGE_LEFT = (By.ID, "page-left")#OK
    FORM_AUTORIZATION = (By.CLASS_NAME, "login-form")#OK
    PAGE_RIGHT = (By.ID, "card-title")#OK
    TAB_PHONE = (By.ID, "t-btn-tab-phone")#OK
    TAB_MAIL = (By.ID, "t-btn-tab-mail")#OK
    TAB_LOGIN = (By.ID, "t-btn-tab-login")#OK
    TAB_LS = (By.ID, "t-btn-tab-ls")#OK
    INPUT_PASSWORD = (By.ID, "password")#OK
    INPUT_PHONE = (By.ID, "username")#OK
    INPUT_MAIL = (By.ID, "username")
    INPUT_LOGIN = (By.ID, "username")
    INPUT_LS = (By.ID, "username")
    LINK_REGISTER = (By.ID, "kc-register")
    BUTTON_TO_COME_IN = (By.ID, "kc-login")#OK
    CAPTCHA = (By.ID, 'captcha')#OK


class RecoveryPageLocators():
    PAGE_RIGHT = (By.ID, "card-title")
    ENTER_CODE = (By.ID, 'back_to_otp_btn')
    INPUT_PHONE_MAIL = (By.ID, "address")
    INPUT_CAPCHA = (By.ID, "captcha")
    BUTTON_COMEBACK = (By.ID, "standard_auth_btn")
    BUTTON_CONTINUE = (By.ID, "otp_get_code")
    RECOVERY_FORM = (By.CLASS_NAME, "card-container_wrapper")
    CODE_INPUT_CONTAINER = (By.ID, "otp-code-timeout")


class PasswordRecoveryPageLocators():
    FORGOT_PASSWORD = (By.ID, 'forgot_password')#OK
    INPUT_PHONE = (By.ID, "username")#OK
    RESET_BUTTON = (By.ID, 'reset')#OK
    PHONE = (By.CLASS_NAME, 'rt-radio__circle')#OK
    RESET_FORM_BUTTON = (By.ID, 'reset-form-submit')
    INPUT_PASSWORD_NEW = (By.ID, "password-new")
    INPUT_PASSWORD_CONFIRM = (By.ID, "password-confirm")
    BUTTON_SAVE = (By.ID, "t-btn-reset-pass")


class RegistrationPageLocators():
    BUTTON_PAGE_REGISTER = (By.CLASS_NAME, "rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded register-form__reg-btn")
    PAGE_LEFT = (By.ID, "page-left")
    INPUT_FIRST_NAME = (By.CLASS_NAME, "rt-input__input rt-input__input--rounded rt-input__input--orange")
    INPUT_LAST_NAME = (By.CLASS_NAME, "rt-input__input rt-input__input--rounded rt-input__input--orange")
    #CARD_MODAL = (By.ID, "card-modal_card")#
    INPUT_ADDRESS = (By.ID, "address")
    REGION_LIST = (By.CLASS_NAME, "rt-input__input rt-select__input rt-input__input--rounded rt-input__input--orange")
    INPUT_PASSWORD = (By.ID, "password")
    INPUT_PASSWORD_CONFIRM = (By.ID, "password-confirm")
