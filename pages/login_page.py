from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config import settings

import allure

class LoginPage:
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    LOGO = (By.CLASS_NAME, "login_logo")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    @allure.step("Открыть страницу логина")
    def open(self):
        self.driver.get(settings.BASE_URL)
        self.wait.until(EC.presence_of_element_located(self.LOGO))

        return self
    
    @allure.step("Ввести username: {username}")
    def enter_username(self, username: str):
        element = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_FIELD)
        )
        element.clear()
        element.send_keys(username)

        return self
    
    @allure.step("Ввести password: {password}")
    def enter_password(self, password):
        element = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        element.clear()
        element.send_keys(password)

        return self
    
    @allure.step("Нажать кнопку Логин")
    def click_login(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        element.click()

        return self
    
    @allure.step("Выполнить логин с данными: {username}/{password}")
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

        return self
    
    @allure.step("Получить текст ошибки")
    def get_error_message(self):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return element.text
        except:
            return None
        
    @allure.step("Проверить URL")
    def check_url_contains(self, text):
        self.wait.until(EC.url_contains(text))

        return text in self.driver.current_url
    
    @allure.step("Проверить отображение элемента")
    def is_element_displayed(self, locator):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except:
            return False
        
    @allure.step("Проверить успешный вход")
    def is_logged_in(self):
        return self.check_url_contains("/inventory.html")
    
    