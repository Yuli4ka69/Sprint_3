from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generators import generate_email
from locators import (
    PERSONAL_ACCOUNT_BUTTON, REGISTRATION_BUTTON, NAME_FIELD, EMAIL_FIELD, PASSWORD_FIELD,
    REGISTRATION_SUBMIT_BUTTON, ERROR_MESSAGE
)
from urls import URLs

class TestRegistrationWithInvalidPassword:
    """Тесты для проверки регистрации с некорректным паролем"""
    def test_registration_with_invalid_password(self, driver):
        """Проверка регистрации с некорректным паролем."""
        driver.get(URLs.BASE_URL)

        wait = WebDriverWait(driver, 30)

        # Переход на страницу входа
        personal_account_button = wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON))
        personal_account_button.click()

        # Переход на страницу регистрации
        registration_button = wait.until(EC.element_to_be_clickable(REGISTRATION_BUTTON))
        registration_button.click()

        # Генерация данных для регистрации
        email = generate_email()
        invalid_password = "123"  # Некорректный пароль (слишком короткий)
        name = "Test User"

        # Ввод данных для регистрации
        wait.until(EC.visibility_of_element_located(NAME_FIELD)).send_keys(name)
        wait.until(EC.visibility_of_element_located(EMAIL_FIELD)).send_keys(email)
        wait.until(EC.visibility_of_element_located(PASSWORD_FIELD)).send_keys(invalid_password)

        # Отправка формы
        wait.until(EC.element_to_be_clickable(REGISTRATION_SUBMIT_BUTTON)).click()

        # Ожидание появления ошибки
        error_message = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))

        # Проверка, что сообщение об ошибке отображается и содержит корректный текст
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
        assert error_message.text == "Некорректный пароль", f"Неверное сообщение об ошибке: {error_message.text}"
