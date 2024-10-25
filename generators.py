import random
import string


def generate_email():
    """Генерирует уникальный адрес электронной почты для регистрации."""
    first_name = "yulia"
    last_name = "zhirova"
    cohort_number = "15"
    random_digits = ''.join(random.choices(string.digits, k=3))  # Генерируем 3 случайные цифры
    domain = random.choice(['yandex.ru', 'gmail.com', 'mail.ru'])  # Выбираем случайный домен

    return f"{first_name}_{last_name}_{cohort_number}_{random_digits}@{domain}"

def generate_password(length=8):
    """Генерирует пароль заданной длины с использованием букв, цифр и символов."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def generate_name(length=6):
    """Генерирует случайное русское имя заданной длины."""
    russian_names = ['Алексей', 'Мария', 'Сергей', 'Екатерина', 'Дмитрий', 'Анна', 'Иван', 'Елена']
    return random.choice(russian_names)  # Возвращаем случайное русское имя
