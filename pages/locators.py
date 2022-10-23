from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")

class ProductPageLocators():
    PRODUCT_PRICE = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]')
    PRODUCT_NAME = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/h1')
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    BASKET_TOTAL_AMOUNT = (By.XPATH, '/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong')
    ADDED_PRODUCT_NAME = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/strong')



