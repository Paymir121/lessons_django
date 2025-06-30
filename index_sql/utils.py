import random
import string


def random_string(length: int) -> str:
    """Генерирует случайную строку из букв и цифр заданной длины"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

