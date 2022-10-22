from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login1" in self.browser.current_url(), "It is not login URL"

    def should_be_login_form(self):
        assert self.is_element_present(LoginPageLocators.LOGIN_USERNAME, LoginPageLocators.LOGIN_PASSWORD),\
            "Login form is broken or not exist"

    def should_be_register_form(self):
        assert self.is_element_present(LoginPageLocators.REG_EMAIL,
                                       LoginPageLocators.REG_PASSWORD1,
                                       LoginPageLocators.REG_PASSWORD2), \
            "Registration form is broken or not exist"