from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It is not URL for login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is broken or not exist"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is broken or not exist"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_FOR_REGISTRATION).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD1_FOR_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD2_FOR_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON).click()
