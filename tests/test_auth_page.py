import pytest
from conftest import web_browser
from pages.auth_page import AuthPage
from selenium import webdriver
from pages.settings import valid_email, valid_password,valid_phone

driver = webdriver.Chrome()

# 1 "Register" button is presented
@pytest.mark.reg
def test_registration_button(web_browser):
    page = AuthPage(web_browser)
    page.registration_button_main.click()
    current_url = page.get_current_url()
    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/" in current_url

# 2 Availability of registration form fields
@pytest.mark.reg
def test_registration_fields_presented(web_browser):
    page = AuthPage(web_browser)
    page.registration_button_main.click()
    assert page.firstName_field_registration.is_presented()
    assert page.lastName_field_registration.is_presented()
    assert page.email_field_registration.is_presented()
    assert page.password_field_registration.is_presented()
    assert page.passwordConfirm_field_registration.is_presented()

# 3 Registration field "Password Confirmation" works correct
@pytest.mark.reg
def test_field_password_confirm(web_browser):
    page = AuthPage(web_browser)
    page.registration_button_main.click()
    page.password_field_registration.click()
    page.password_field_registration.send_keys(valid_password)
    page.passwordConfirm_field_registration.click()
    page.passwordConfirm_field_registration.send_keys("Vostopolets12")
    page.scroll_down()
    page.registration_button.click()
    assert page.passwordConfirm_error.is_presented()

# 4 Registration field "Name" is required to fill
@pytest.mark.reg
def test_field_name_required(web_browser):
    page = AuthPage(web_browser)
    page.registration_button_main.click()
    page.lastName_field_registration.send_keys("Востополец")
    page.email_field_registration.send_keys(valid_email)
    page.password_field_registration.send_keys(valid_password)
    page.passwordConfirm_field_registration.send_keys(valid_password)
    page.registration_button.click()
    assert page.name_error_registration.is_presented()

# 5 Registration field "Password" without letters raise error
@pytest.mark.reg
def test_field_password_without_letters(web_browser):
    page = AuthPage(web_browser)
    page.registration_button_main.click()
    page.password_field_registration.send_keys("123456789")
    page.passwordConfirm_field_registration.send_keys("123456789")
    page.registration_button.click()
    assert page.password_error1.is_presented()

# 6 Registration field "Password", length-error of the password
@pytest.mark.reg
def test_field_password_length(web_browser):
    page = AuthPage(web_browser)
    page.registration_button_main.click()
    page.password_field_registration.send_keys("123")
    page.registration_button.click()
    assert page.password_error2.is_presented()

# 7 Registration field "Password", not latin characters raise error
@pytest.mark.reg
def test_field_password_russian_letters(web_browser):
    page = AuthPage(web_browser)
    page.registration_button_main.click()
    page.password_field_registration.send_keys("апровстароывампп")
    page.registration_button.click()
    assert page.password_error3.is_presented()

# 8  Link to the User Agreement is presented in the registration form
@pytest.mark.reg
def test_user_agreement_presented(web_browser):
    page = AuthPage(web_browser)
    page.registration_button_main.click()
    page.scroll_down()
    page.user_agreement.click()
    assert page.user_agreement.is_clickable()

# 9 Registration field "Last name"
@pytest.mark.reg
def test_lastName_error(web_browser):
    page = AuthPage(web_browser)
    page.registration_button_main.click()
    page.lastName_field_registration.send_keys("123")
    page.registration_button.click()
    page.firstName_field_registration.click()
    assert page.lastName_field_registration_error.is_visible()
    page.lastName_field_registration.click()
    page.lastName_field_registration.send_keys("ычвсмтоыдвтмыфотмвдфылодтмымвмлфымитаыдлфоимдфодофлимдлмитдфлуаоимржиртаолытимлоаыимлоивыфломилврфаимлоиаымлтимловфиалодваолимфоваимычвсмтоыдвтмыфотмвдфылодтмымвмлфымитаыдлфоимдфодофлимдлмитдфлуаоимржиртаолытимлоаыимлоивыфломилврфаимлоиаымлтимловфиалодваолим")
    page.firstName_field_registration.click()
    assert page.lastName_field_registration_error.is_presented()
    page.lastName_field_registration.click()
    page.lastName_field_registration.send_keys("В")
    page.firstName_field_registration.click()
    assert page.lastName_field_registration_error.is_presented()
    page.lastName_field_registration.click()
    page.lastName_field_registration.send_keys("® ✉ § © ☯ ☭ ? $ £ ¢")
    page.firstName_field_registration.click()
    assert page.lastName_field_registration_error.is_presented()

# 10 Registration successfully
@pytest.mark.reg
@pytest.mark.skip(reason="Аккаунт уже зарегистрирован")
def test_registration_successful(web_browser):
    page = AuthPage(web_browser)
    page.registration_button_main.click()
    page.firstName_field_registration.send_keys("Юлия")
    page.lastName_field_registration.send_keys("Востополец")
    page.email_field_registration.send_keys(valid_email)
    page.password_field_registration.send_keys(valid_password)
    page.passwordConfirm_field_registration.send_keys(valid_password)
    page.registration_button.click()
    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?execution=" in page.get_current_url()

# 11 Successful authorization by e-mail
@pytest.mark.auth
@pytest.mark.skip(reason="Когда появляется капча, тест может упасть. Попробуйте запустить позднее")
def test_authorisation_email(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded(10)
    page.username.click()
    page.username.send_keys(valid_email)
    page.password.click()
    page.password.send_keys(valid_password)
    page.login.click()
    assert "https://b2c.passport.rt.ru/account_b2c/page" in page.get_current_url()

# 12 Successful authorization by phone number
@pytest.mark.auth
@pytest.mark.skip(reason="Когда появляется капча, тест может упасть. Попробуйте запустить позднее")
def test_authorisation_phone(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded(10)
    page.username.click()
    page.username.send_keys(valid_phone)
    page.password.click()
    page.password.send_keys(valid_password)
    page.login.click()
    assert "https://b2c.passport.rt.ru/account_b2c/page" in page.get_current_url()

# 13 Unsuccessful authorization with not valid e-mail
@pytest.mark.auth
def test_authorisation_email_unsuccessful(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded(10)
    page.username.click()
    page.username.send_keys("yu@mail.ru")
    page.password.click()
    page.password.send_keys(valid_password)
    page.login.click()
    assert page.login_error.is_presented()

# 14 Unsuccessful authorization with not valid phone number
@pytest.mark.auth
def test_authorisation_password_unsuccessful(web_browser):
    page = AuthPage(web_browser)
    page.username.click()
    page.username.send_keys(valid_email)
    page.password.click()
    page.password.send_keys('12345d')
    page.login.click()
    assert page.login_error.is_presented()

# 15 Logo and product slogan are presented
@pytest.mark.auth
def test_logo_and_slogan(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded(10)
    assert page.slogan.is_presented()
    assert page.logo.is_presented()

# 16 Password recovery form. Availability of all fields
@pytest.mark.password
def test_forgot_password_elements(web_browser):
    page = AuthPage(web_browser)
    page.forgot_password_button.click()
    page.wait_page_loaded(10)
    assert page.username.is_presented()
    assert page.password_recovery_title.is_presented()
    assert page.symbols.is_presented()
    assert page.contin.is_presented()
    assert page.reset.is_presented()
    assert page.forgot_mail.is_presented()
    assert page.forgot_lc.is_presented()
    assert page.forgot_phone.is_presented()
    assert page.forgot_login.is_presented()
    assert page.captcha.is_presented()

# 17 Password recovery form. Button "GO BACK"
@pytest.mark.password
def test_reset_back(web_browser):
    page = AuthPage(web_browser)
    page.forgot_password_button.click()
    page.wait_page_loaded(10)
    page.reset.click()
    page.wait_page_loaded()
    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate" in page.get_current_url()

# 18 Password recovery form. 'Continue' button
@pytest.mark.password
def test_capcha(web_browser):
    page = AuthPage(web_browser)
    page.forgot_password_button.click()
    page.username.click()
    page.username.send_keys(valid_email)
    symbol = page.captcha.get_text()
    page.symbols.send_keys(symbol)
    page.contin.click()
    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" in page.get_current_url()

# 19 Password recovery form. Captcha input error
@pytest.mark.password
def test_capcha_error(web_browser):
    page = AuthPage(web_browser)
    page.forgot_password_button.click()
    page.username.click()
    page.username.send_keys(valid_email)
    page.symbols.send_keys("1234")
    page.contin.click()
    assert page.capcha_error.is_presented()

# 20 Hints in the authorization fields are presented
@pytest.mark.auth
def test_hints(web_browser):
    page = AuthPage(web_browser)
    page.scroll_down()
    page.phone.click()
    text=page.field.get_text()
    assert text == "Мобильный телефон"
    page.email.click()
    text = page.field.get_text()
    assert text == "Электронная почта"
    page.logintab.click()
    text = page.field.get_text()
    assert text == "Логин"
    page.lc.click()
    text = page.field.get_text()
    assert text == "Лицевой счёт"

# 21 Wrong kode for registration error
@pytest.mark.reg
def test_reg(web_browser):
    page = AuthPage(web_browser)
    page.registration_button_main.click()
    page.firstName_field_registration.send_keys("Юлия")
    page.lastName_field_registration.send_keys("Востополец")
    page.email_field_registration.send_keys("89008976543")
    page.password_field_registration.send_keys("Vostopolets123")
    page.passwordConfirm_field_registration.send_keys("Vostopolets123")
    page.registration_button.click()
    page.kod0.send_keys('0')
    page.kod1.send_keys('1')
    page.kod2.send_keys('2')
    page.kod3.send_keys('3')
    page.kod4.send_keys('4')
    page.kod5.send_keys('5')
    assert page.kod_error.is_presented()