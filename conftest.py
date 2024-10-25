import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    LOGIN_BUTTON_MAIN_PAGE, LOGIN_EMAIL_FIELD, LOGIN_PASSWORD_FIELD, LOGIN_SUBMIT_BUTTON,
    PLACE_ORDER_BUTTON, RECOVERY_LOGIN_LINK, LOGIN_LINK_REGISTRATION_FORM, PERSONAL_ACCOUNT_BUTTON
)

@pytest.fixture
def driver():
    """Фикстура для инициализации веб-драйвера."""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def login_details():
    """Читает логин и пароль из файла login_details.txt."""
    with open('login_details.txt', 'r') as f:
        lines = f.readlines()
        email = lines[0].split(":")[1].strip()  # Читаем email
        password = lines[1].split(":")[1].strip()  # Читаем пароль
    return email, password

@pytest.fixture
def authorized_user(driver, login_details, start_page="https://stellarburgers.nomoreparties.site/"):
    """Фикстура для авторизации пользователя с разной начальной страницы."""
    driver.get(start_page)
    wait = WebDriverWait(driver, 30)

    # Выбор действий в зависимости от начальной страницы
    if "forgot-password" in start_page:
        # Переход на форму входа через восстановление пароля
        wait.until(EC.element_to_be_clickable(RECOVERY_LOGIN_LINK)).click()
    elif "register" in start_page:
        # Переход на форму входа через страницу регистрации
        wait.until(EC.element_to_be_clickable(LOGIN_LINK_REGISTRATION_FORM)).click()
    elif "login" not in start_page:
        # Переход на форму входа через главную страницу, используя "Войти в аккаунт"
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN_PAGE)).click()
    elif "account" in start_page:
        # Переход на форму входа через личный кабинет
        wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()

    # Ввод email и пароля для авторизации
    email, password = login_details
    wait.until(EC.visibility_of_element_located(LOGIN_EMAIL_FIELD)).send_keys(email)
    wait.until(EC.visibility_of_element_located(LOGIN_PASSWORD_FIELD)).send_keys(password)

    # Нажатие на кнопку "Войти"
    wait.until(EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON)).click()

    # Проверка успешного входа
    assert wait.until(EC.visibility_of_element_located(PLACE_ORDER_BUTTON)), "Кнопка 'Оформить заказ' не найдена, вход не удался"
    return wait
