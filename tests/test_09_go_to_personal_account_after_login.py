from selenium.webdriver.support import expected_conditions as EC
from locators import PERSONAL_ACCOUNT_BUTTON, ACCOUNT_PROFILE_URL

def test_go_to_personal_account_after_login(authorized_user):
    """Проверка перехода в 'Личный кабинет' после авторизации."""
    wait = authorized_user  # Используем фикстуру для авторизации

    # Шаг 2: Переход в 'Личный кабинет'
    personal_account_button = wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON))
    personal_account_button.click()

    # Ожидание перехода на страницу личного кабинета
    wait.until(EC.url_to_be(ACCOUNT_PROFILE_URL))

    # Проверка, что пользователь находится на странице личного кабинета
    assert wait._driver.current_url == ACCOUNT_PROFILE_URL, \
        f"Ожидался переход на страницу личного кабинета, но текущий URL {wait._driver.current_url}"
