from selenium.webdriver.common.by import By

import allure
import pytest

@allure.feature("Логин")
@allure.story("Тесты логина")
class TestLogin:
    @allure.title("Успешный логин стандартным пользователем")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login

    def test_successful_login(self, login_page, standard_user):
        with allure.step("Выполнить логин"):
            login_page.login(
                standard_user["username"], 
                standard_user["password"]
            )

        with allure.step("Проверить успешный вход"):
            assert login_page.is_logged_in(), "Не удалось войти в систему"

        with allure.step("Проверить отображение элементов на странице"):
            assert login_page.is_element_displayed((By.CLASS_NAME, "inventory_list")), "Список товаров не отображается"

    
    @allure.title("Неуспешый логин с неправильными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.login

    def test_invalid_login(self, login_page, invalid_user):
        with allure.step("Выполнить логин"):
            login_page.login(
                invalid_user["username"],
                invalid_user["password"]
            )

        with allure.step("Проверить сообщение об ошибке"):
            error_message = login_page.get_error_message()

            assert error_message is not None, "Сообщение об ошибке не отображается"
            assert "not match" in error_message.lower(), f"Некорректное сообщение об ошибке: {error_message}"


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


    @allure.title("Неуспешный логин с пустыми полями")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.login
    
    def test_null_fields_login(self, login_page):
        with allure.step("Выполнить логин с пустыми полями"):
            login_page.login(
                "",
                ""
            )

        with allure.step("Проверить сообщение об ошибке"):
            error_message = login_page.get_error_message()

            assert error_message is not None, "Сообщение об ошибке не отображается"
            assert "username is required" in error_message.lower(), f"Некорректное сообщение об ошибке: {error_message}"

    
    @allure.title("Успешный логин с лагающим пользователем")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.login

    def test_performance_glitch_user_login(self, login_page, glitch_user):
        with allure.step("Выполнить логин с лагающим пользователем"):
            login_page.login(
                glitch_user["username"],
                glitch_user["password"]
            )


        with allure.step("Проверить успешный вход"):
            is_login = login_page.is_logged_in()

            assert is_login, "У пользователя не прогрузилась страница"

        with allure.step("Проверить отображение элементов на странице"):
            assert login_page.is_element_displayed((By.CLASS_NAME, "inventory_list")), "Список товаров не отображается"