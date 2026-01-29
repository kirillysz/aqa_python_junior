from selenium.webdriver.common.by import By

import allure
import pytest

@allure.feature("Логин")
@allure.story("Тесты логина")
class TestLogin:
    @allure.title("Успешный логин стандартным пользователем")
    @allure.severity(allure.severity_level.CRITICAL)

    @pytest.mark.login
    @pytest.mark.smoke

    def test_successful_login(self, login_page, standard_user):
        with allure.step("Выполнить логин"):
            login_page.login(
                standard_user["username"], 
                standard_user["password"]
            )

        with allure.step("Проверить успешный вход"):
            assert login_page.is_logged_in(), "Не удалось войти в систему"

        with allure.step("Проверить URL"):
            assert "/inventory.html" in login_page.driver.current_url, "Некорректный URL"

        with allure.step("Проверить отображение элементов на странице"):
            assert login_page.is_element_displayed((By.CLASS_NAME, "inventory_list")), "Список товаров не отображается"

    
    @allure.title("Неуспешный логин заблокированным пользователем")
    @allure.severity(allure.severity_level.NORMAL)

    @pytest.mark.login
    
    def test_locked_user_login(self, login_page, locked_user):
        with allure.step("Выполнить логин с заблокированным пользователем"):
            login_page.login(
                locked_user["username"], 
                locked_user["password"]
            )
        
        with allure.step("Проверить сообщение об ошибке"):
            error_message = login_page.get_error_message()

            assert error_message is not None, "Сообщение об ошибке не отображается"
            assert "locked out" in error_message.lower(), f"Некорректное сообщение об ошибке: {error_message}"

    