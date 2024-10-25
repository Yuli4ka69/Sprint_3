from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGIN_EMAIL_FIELD, LOGIN_PASSWORD_FIELD, LOGIN_SUBMIT_BUTTON, PLACE_ORDER_BUTTON, LOGIN_LINK_REGISTRATION_FORM


def test_login_via_registration_form(authorized_user):
    """Проверка успешного входа через кнопку в форме регистрации."""
    authorized_user.start_page = "https://stellarburgers.nomoreparties.site/register"
    wait = authorized_user

    # Проверка успешного входа (наличие кнопки 'Оформить заказ')
    assert wait.until(EC.visibility_of_element_located(PLACE_ORDER_BUTTON)), "Кнопка 'Оформить заказ' не найдена, вход не удался"