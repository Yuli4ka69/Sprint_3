from selenium.webdriver.support import expected_conditions as EC
from locators import PLACE_ORDER_BUTTON


def test_login_via_main_page_button(authorized_user):
    """Проверка успешного входа через кнопку 'Войти в аккаунт' на главной странице."""
    authorized_user.start_page = "https://stellarburgers.nomoreparties.site/"
    wait = authorized_user

    # Проверка успешного входа (наличие кнопки 'Оформить заказ')
    assert wait.until(EC.visibility_of_element_located(PLACE_ORDER_BUTTON)), "Кнопка 'Оформить заказ' не найдена, вход не удался"
