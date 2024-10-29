import random
import string

def generate_email():
    first_name = "yulia"
    last_name = "zhirova"
    cohort_number = "15"
    random_digits = ''.join(random.choices(string.digits, k=3))
    domain = random.choice(['yandex.ru', 'gmail.com', 'mail.ru'])
    return f"{first_name}_{last_name}_{cohort_number}_{random_digits}@{domain}"

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))
