from selenium.webdriver.support import expected_conditions as EC
from locators import PERSONAL_ACCOUNT_BUTTON, CONSTRUCTOR_ELEMENT, MAIN_HEADER

def test_login_via_main_page_button(authorized_user):
    """Проверка входа по кнопке 'Войти в аккаунт' на главной странице и перехода в конструктор."""
    wait = authorized_user  # Используем фикстуру для авторизации

    # Шаг 2: Клик на Личный кабинет
    wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()

    # Шаг 3: Нажатие на элемент "Конструктор" в навигации после авторизации
    constructor_element = wait.until(EC.element_to_be_clickable(CONSTRUCTOR_ELEMENT))
    constructor_element.click()

    # Проверка, что мы на странице конструктора, где есть элемент с заголовком
    constructor_header = wait.until(EC.visibility_of_element_located(MAIN_HEADER))
    assert constructor_header.is_displayed(), "Заголовок 'Конструктор' не найден на странице."
