from selenium.webdriver.support import expected_conditions as EC
from locators import PERSONAL_ACCOUNT_BUTTON, LOGOUT_BUTTON, LOGIN_PAGE_URL
import time

def test_logout_via_personal_account(authorized_user):
    """Проверка выхода через Личный кабинет и редиректа на страницу входа."""
    wait = authorized_user  # Используем фикстуру для авторизации

    # Шаг 2: Переход в Личный кабинет
    personal_account_button = wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON))
    personal_account_button.click()

    # Шаг 3: Нажатие на кнопку выхода в Личном кабинете
    logout_button = wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON))
    logout_button.click()

    # Ожидание для завершения редиректа
    time.sleep(1)

    # Шаг 4: Проверка, что происходит редирект на страницу входа
    assert wait._driver.current_url == LOGIN_PAGE_URL, \
        f"Ожидался редирект на страницу входа, но текущий URL: {wait._driver.current_url}"
