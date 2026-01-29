from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from config import settings

import logging
import pytest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def driver():
    firefox_options = Options()
    # firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")
    firefox_options.add_argument("--window-size=1920,1080")

    service = Service("/usr/local/bin/geckodriver")

    driver = webdriver.Firefox(service=service, options=firefox_options)
    wait = WebDriverWait(driver, 15)
    logger.info("Браузер создан")

    driver.get(settings.BASE_URL)

    try:
        wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        logger.info("Страница загружена")

    except Exception as e:
        logger.error(f"Ошибка загрузки: {e}")
        driver.save_screenshot("page_load_error.png")

        raise

    yield driver

    driver.quit()
    logger.info("❌ Браузер закрыт")

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)

@pytest.fixture
def login_page(driver, wait):
    page = LoginPage(driver, wait)
    return page


@pytest.fixture
def standard_user():
    return {
        "username": "standard_user", 
        "password": "secret_sauce"
    }

@pytest.fixture
def locked_user():
    return {
        "username": "locked_out_user",
        "password": "secret_sauce"
    }

@pytest.fixture
def glitch_user():
    return {
        "username": "performance_glitch_user",
        "password": "secret_sauce"
    }
