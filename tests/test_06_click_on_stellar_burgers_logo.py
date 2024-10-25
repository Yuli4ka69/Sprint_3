from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PERSONAL_ACCOUNT_BUTTON, LOGO_ELEMENT, MAIN_HEADER

def test_click_tabs_and_verify_classes(authorized_user):
    """Проверка клика на лого Stellar Burgers после авторизации."""
    wait = authorized_user  # Используем фикстуру для авторизации

    # Шаг 2: Клик на Личный кабинет
    personal_account_button = wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON))
    personal_account_button.click()

    # Шаг 3: Клик на логотип "Stellar Burgers"
    logo_element = wait.until(EC.element_to_be_clickable(LOGO_ELEMENT))
    logo_element.click()

    # Проверка, что мы на главной странице, где есть элемент с заголовком
    main_header = wait.until(EC.visibility_of_element_located(MAIN_HEADER))
    assert main_header.is_displayed(), "Заголовок главной страницы не найден."
