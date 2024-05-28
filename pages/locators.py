from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGO_RTK = (By.ID, "rt-logo main-header__logo")
    PAGE_LEFT = (By.ID, "page-left")
    FORM_AUTORIZATION = (By.ID, "form.login-form")
    PAGE_RIGHT = (By.ID, "page-right")
    TAB_PHONE = (By.ID, "t-btn-tab-phone")
    TAB_MAIL = (By.ID, "t-btn-tab-mail")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")
    TAB_LS = (By.ID, "t-btn-tab-ls")
    INPUT_USERNAME = (By.ID, "username")
    INPUT_PASSWORD = (By.ID, "password")
    INPUT_PHONE = (By.ID, "username")
    INPUT_MAIL = (By.ID, "username")
    INPUT_LOGIN = (By.ID, "username")
    INPUT_LS = (By.ID, "username")
    LINK_REGISTER = (By.ID, "kc-register")
    BUTTON_TO_COME_IN = (By.ID, "kc-login")


class RecoveryPageLocators():
    PAGE_RIGHT = (By.ID, "page-right")
    TAB_PHONE = (By.ID, "t-btn-tab-phone")
    TAB_MAIL = (By.ID, "t-btn-tab-mail")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")
    TAB_LS = (By.ID, "t-btn-tab-ls")
    INPUT_PHONE = (By.ID, "username")
    INPUT_MAIL = (By.ID, "username")
    INPUT_LOGIN = (By.ID, "username")
    INPUT_LS = (By.ID, "username")
    INPUT_CAPCHA = (By.ID, "captcha")
    BUTTON_COMEBACK = (By.ID, "reset-back")
    BUTTON_CONTINUE = (By.ID, "reset")
    RECOVERY_FORM = (By.ID, "card-container_wrapper")
    CODE_INPUT_CONTAINER = (By.ID, "code-input-container_timeout")


class PasswordRecoveryPageLocators():
    INPUT_PASSWORD_NEW = (By.ID, "password-new")
    INPUT_PASSWORD_CONFIRM = (By.ID, "password-confirm")
    BUTTON_SAVE = (By.ID, "t-btn-reset-pass")


class RegistrationPageLocators():
    BUTTON_PAGE_REGISTER = (By.CLASS_NAME, "rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded register-form__reg-btn")
    PAGE_LEFT = (By.ID, "page-left")
    INPUT_FIRST_NAME = (By.CLASS_NAME, "rt-input__input rt-input__input--rounded rt-input__input--orange")
    INPUT_LAST_NAME = (By.CLASS_NAME, "rt-input__input rt-input__input--rounded rt-input__input--orange")
    CARD_MODAL = (By.ID, "card-modal_card")
    INPUT_ADDRESS = (By.ID, "address")
    REGION_LIST = (By.CLASS_NAME, "rt-input rt-input--rounded rt-input--orange rt-input--actions")
    INPUT_PASSWORD = (By.ID, "password")
    INPUT_PASSWORD_CONFIRM = (By.ID, "password-confirm")
