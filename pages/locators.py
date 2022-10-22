from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USERNAME = (By.ID, "id_login-username1")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    REG_EMAIL = (By.ID, "id_login-username")
    REG_PASSWORD1 = (By.ID, "id_registration-password11")
    REG_PASSWORD2 = (By.ID, "id_registration-password2")
