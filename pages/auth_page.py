from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=503d6500-327b-4711-8fee-70032591133f&theme&auth_type'
        super().__init__(web_driver, url)

    # Registration Page Elements
    registration_button_main = WebElement(id='kc-register')
    firstName_field_registration = WebElement(name="firstName")
    lastName_field_registration = WebElement(name="lastName")
    email_field_registration = WebElement(id="address")
    password_field_registration = WebElement(id="password")
    passwordConfirm_field_registration = WebElement(id="password-confirm")
    passwordConfirm_error = WebElement(xpath="//span[text()='Необходимо заполнить поле кириллицей. От 2 до 30 символов.']")
    registration_button = WebElement(name="register")
    name_error_registration = WebElement(xpath="//span[text()='Необходимо заполнить поле кириллицей. От 2 до 30 символов.']")
    password_error1 = WebElement(xpath="//span[text()='Пароль должен содержать хотя бы одну заглавную букву']")
    password_error2 = WebElement(xpath="//span[text()='Длина пароля должна быть не менее 8 символов']")
    password_error3 = WebElement(xpath="//span[text()='Пароль должен содержать только латинские буквы']")
    user_agreement = WebElement(xpath='//a[@disabled="false"]')
    lastName_field_registration_error = WebElement(xpath= "//span[text()='Необходимо заполнить поле кириллицей. От 2 до 30 символов.']")

    # Login page elements
    username = WebElement(id="username")
    password = WebElement(id="password")
    login = WebElement(id="kc-login")
    login_error = WebElement(id="form-error-message")
    slogan = WebElement(css_selector="#page-left > div > div.what-is > p")
    logo =WebElement(css_selector="#page-left > div > div.what-is-container__logo-container")
    email = WebElement(xpath="//div[@id='t-btn-tab-mail']")
    logintab = WebElement(xpath="// div[ @ id = 't-btn-tab-login']")
    lc = WebElement(xpath="//div[@id='t-btn-tab-ls']")
    field = WebElement(xpath="//input[@id='username']/../span[2][@class='rt-input__placeholder']")
    phone= WebElement (xpath="// div[ @ id = 't-btn-tab-phone']")

    # Elements of the "Forgot password" form
    forgot_password_button = WebElement(id="forgot_password")
    password_recovery_title = WebElement(xpath="//h1[text()='Восстановление пароля']")
    forgot_mail = WebElement(id="t-btn-tab-mail")
    forgot_login = WebElement(id="t-btn-tab-login")
    forgot_lc = WebElement(id="t-btn-tab-ls")
    forgot_phone = WebElement(id="t-btn-tab-phone")
    captcha = WebElement(css_selector='div.rt-captcha__image-con')
    symbols = WebElement(id='captcha')
    contin = WebElement(id='reset')
    reset = WebElement(id="reset-back")
    capcha_error = WebElement(id="form-error-message")

    # Kod error locators
    kod_error= WebElement(xpath="//span[@id='form-error-message']")
    kod0= WebElement(xpath="//input[@id='rt-code-0']")
    kod1 = WebElement(xpath="//input[@id='rt-code-1']")
    kod2 = WebElement(xpath="//input[@id='rt-code-2']")
    kod3 = WebElement(xpath="//input[@id='rt-code-3']")
    kod4 = WebElement(xpath="//input[@id='rt-code-4']")
    kod5 = WebElement(xpath="//input[@id='rt-code-5']")