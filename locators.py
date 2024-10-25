from selenium.webdriver.common.by import By

# Локаторы для страницы входа
LOGIN_EMAIL_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")  # Поле для ввода email
LOGIN_PASSWORD_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")  # Поле для ввода пароля
LOGIN_SUBMIT_BUTTON = (By.XPATH, "/html/body/div[1]/div/main/div/form/button")  # Кнопка "Войти"

# Локаторы для успешной авторизации
PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")  # Кнопка "Оформить заказ" (на главной странице после входа)

# Локаторы для страницы личного кабинета
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")  # Кнопка перехода в Личный кабинет
LOGOUT_BUTTON = (By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button")  # Кнопка выхода в Личном кабинете

# Локаторы для проверки редиректа
ACCOUNT_PROFILE_URL = "https://stellarburgers.nomoreparties.site/account/profile"  # URL профиля после перехода в Личный кабинет
LOGIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/login"  # URL страницы входа после выхода из Личного кабинета

# Локаторы для вкладок в конструкторе
BUNS_TAB = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]")  # Вкладка "Булки"
SAUCES_TAB = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]")  # Вкладка "Соусы"
FILLINGS_TAB = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]")  # Вкладка "Начинки"

# Локатор для элемента навигации "Личный кабинет"
NAV_ELEMENT = (By.XPATH, "//*[@id='root']/div/header/nav/a")  # Личный кабинет

# Локатор для логотипа "Stellar Burgers"
LOGO_ELEMENT = (By.XPATH, "//*[@id='root']/div/header/nav/div/a")  # Логотип

# Локатор для основного заголовка на главной странице
MAIN_HEADER = (By.XPATH, "//*[@id='root']/div/main/section[1]/h1")  # Заголовок главной страницы

# Локаторы для страницы восстановления пароля
RECOVERY_LOGIN_LINK = (By.XPATH, "//*[@id='root']/div/main/div/div/p/a")  # Кнопка "Войти" на странице восстановления пароля

# Локатор для кнопки входа на странице регистрации
LOGIN_LINK_REGISTRATION_FORM = (By.XPATH, "//*[@id='root']/div/main/div/div/p[1]/a")  # Кнопка входа на странице регистрации

# Локатор для кнопки конструктора
CONSTRUCTOR_ELEMENT = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p")  # Кнопка конструктора

# Локатор для кнопки "Войти в аккаунт" на главной странице
LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")  # Кнопка "Войти в аккаунт" на главной странице

# Локатор для кнопки "Зарегистрироваться"
REGISTRATION_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Кнопка перехода на страницу регистрации

# Локаторы для формы регистрации
NAME_FIELD = (By.NAME, "name")  # Поле для ввода имени
EMAIL_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")  # Поле для ввода email
PASSWORD_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input")  # Поле для ввода пароля
REGISTRATION_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")  # Кнопка "Зарегистрироваться"

# Локатор для сообщения об ошибке
ERROR_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default']")  # Сообщение об ошибке (например, для некорректного пароля)
