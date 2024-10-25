from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGIN_EMAIL_FIELD, LOGIN_PASSWORD_FIELD, LOGIN_SUBMIT_BUTTON, PLACE_ORDER_BUTTON, RECOVERY_LOGIN_LINK

def test_login_via_password_recovery_form(authorized_user):
    """Проверка входа через кнопку в форме восстановления пароля."""
    authorized_user.start_page = "https://stellarburgers.nomoreparties.site/forgot-password"
    wait = authorized_user

    # Проверка успешного входа (наличие кнопки 'Оформить заказ')
    assert wait.until(EC.visibility_of_element_located(PLACE_ORDER_BUTTON)), "Кнопка 'Оформить заказ' не найдена, вход не удался"
