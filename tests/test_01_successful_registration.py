from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generators import generate_email, generate_password, generate_name
from locators import PERSONAL_ACCOUNT_BUTTON, REGISTRATION_BUTTON, NAME_FIELD, EMAIL_FIELD, PASSWORD_FIELD, REGISTRATION_SUBMIT_BUTTON, LOGIN_PAGE_URL

def test_successful_registration(driver):
    """Проверка успешной регистрации с редиректом на страницу логина."""
    driver.get("https://stellarburgers.nomoreparties.site/")

    wait = WebDriverWait(driver, 30)

    # Переход на страницу входа
    personal_account_button = wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON))
    personal_account_button.click()

    # Переход на страницу регистрации
    registration_button = wait.until(EC.element_to_be_clickable(REGISTRATION_BUTTON))
    registration_button.click()

    # Генерация данных для регистрации
    email = generate_email()
    password = generate_password(length=8)
    name = generate_name()

    # Ввод данных для регистрации
    wait.until(EC.visibility_of_element_located(NAME_FIELD)).send_keys(name)
    wait.until(EC.visibility_of_element_located(EMAIL_FIELD)).send_keys(email)
    wait.until(EC.visibility_of_element_located(PASSWORD_FIELD)).send_keys(password)

    # Сохраняем логин и пароль в файл
    with open('login_details.txt', 'w') as f:
        f.write(f"Email: {email}\n")
        f.write(f"Password: {password}\n")

    # Отправка формы
    wait.until(EC.element_to_be_clickable(REGISTRATION_SUBMIT_BUTTON)).click()

    # Проверка перехода на страницу логина
    wait.until(EC.url_to_be(LOGIN_PAGE_URL))  # Ожидаем редиректа на страницу логина
    assert driver.current_url == LOGIN_PAGE_URL, f"Ожидалась страница {LOGIN_PAGE_URL}, но получили {driver.current_url}"
