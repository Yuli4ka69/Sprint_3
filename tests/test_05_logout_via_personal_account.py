import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import PERSONAL_ACCOUNT_BUTTON, LOGOUT_BUTTON, LOGIN_PAGE_URL
from urls import URLs

class TestLogoutViaPersonalAccount:
    """Тесты для проверки выхода через Личный кабинет и редиректа на страницу входа"""

    @pytest.mark.parametrize("authorized_user", [URLs.BASE_URL], indirect=True)
    def test_logout_via_personal_account(self, authorized_user):
        """Проверка выхода через Личный кабинет и редиректа на страницу входа."""
        wait = WebDriverWait(authorized_user, 30)

        # Переход в Личный кабинет
        wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()

        # Нажатие на кнопку выхода в Личном кабинете
        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()

        # Явное ожидание для завершения редиректа на страницу входа
        wait.until(EC.url_to_be(LOGIN_PAGE_URL))

        # Проверка, что произошел редирект на страницу входа
        assert wait._driver.current_url == LOGIN_PAGE_URL, \
            f"Ожидался редирект на страницу входа, но текущий URL: {wait._driver.current_url}"
