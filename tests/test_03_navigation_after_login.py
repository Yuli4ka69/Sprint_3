import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import (
    PERSONAL_ACCOUNT_BUTTON, LOGO_ELEMENT, MAIN_HEADER,
    CONSTRUCTOR_ELEMENT, ACCOUNT_PROFILE_URL
)
from urls import URLs


class TestNavigationAfterLogin:
    """Тесты для проверки навигации и элементов интерфейса после авторизации"""

    @pytest.mark.parametrize("authorized_user", [URLs.BASE_URL], indirect=True)
    def test_click_on_stellar_burgers_logo(self, authorized_user):
        """Проверка клика на логотип Stellar Burgers после авторизации."""
        wait = WebDriverWait(authorized_user, 30)
        wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(LOGO_ELEMENT)).click()
        main_header = wait.until(EC.visibility_of_element_located(MAIN_HEADER))
        assert main_header.is_displayed(), "Заголовок главной страницы не найден."

    @pytest.mark.parametrize("authorized_user", [URLs.BASE_URL], indirect=True)
    def test_transition_to_constructor_after_login(self, authorized_user):
        """Проверка перехода в конструктор после авторизации."""
        wait = WebDriverWait(authorized_user, 30)
        wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()
        constructor_element = wait.until(EC.element_to_be_clickable(CONSTRUCTOR_ELEMENT))
        constructor_element.click()
        constructor_header = wait.until(EC.visibility_of_element_located(MAIN_HEADER))
        assert constructor_header.is_displayed(), "Заголовок 'Конструктор' не найден на странице."

    @pytest.mark.parametrize("authorized_user", [URLs.BASE_URL], indirect=True)
    def test_go_to_personal_account_after_login(self, authorized_user):
        """Проверка перехода в 'Личный кабинет' после авторизации."""
        wait = WebDriverWait(authorized_user, 30)
        wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(ACCOUNT_PROFILE_URL))
        assert authorized_user.current_url == ACCOUNT_PROFILE_URL, \
            f"Ожидался переход на страницу личного кабинета, но текущий URL {authorized_user.current_url}"

