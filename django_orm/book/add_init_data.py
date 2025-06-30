import json
import os
import django
from django.utils import timezone

from book.models import Author, Review, Book

def load_data_from_json():
    """Загрузка данных из JSON файла в базу данных"""
    with open( os.path.join(os.path.dirname(__file__), "data.json"), 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Сначала создаем всех авторов
    authors = {}
    print(f"Найдено {len(data.get('authors', []))} авторов")
    for author_data in data.get("authors", []):
        author, created = Author.objects.get_or_create(
            email=author_data["email"],
            defaults={
                'first_name': author_data["first_name"],
                'last_name': author_data["last_name"],
                'is_active': author_data.get("is_active", True)
            }
        )
        authors[author_data["email"]] = author
        if created:
            print(f"Создан новый автор: {author.first_name} {author.last_name}")

    # Затем создаем книги
    books = {}
    print(f"Найдено {len(data.get('books', []))} книг")
    for book_data in data.get("books", []):
        try:
            author = authors[book_data["author_email"]]
            book, created = Book.objects.get_or_create(
                title=book_data["title"],
                author=author,
                defaults={
                    'published_date': book_data["published_date"],
                    'price': book_data["price"],
                    'discount': book_data.get("discount", 0),
                    'metadata': book_data.get("metadata", {})
                }
            )
            books[book_data["title"]] = book
            if created:
                print(f"Создана новая книга: {book.title}")
        except KeyError as e:
            print(
                f"Ошибка: автор с email {book_data['author_email']} не найден. Книга '{book_data['title']}' не создана.")
            continue

    # Наконец, создаем отзывы
    print(f"Найдено {len(data.get('reviews', []))} отзывов")
    for review_data in data.get("reviews", []):
        try:
            book = books[review_data["book_title"]]
            review, created = Review.objects.get_or_create(
                book=book,
                rating=review_data["rating"],
                defaults={
                    'comment': review_data.get("comment", ""),
                    'created_at': review_data.get("created_at", timezone.now())
                }
            )
            if created:
                print(f"Создан новый отзыв для книги '{book.title}' с рейтингом {review.rating}")
        except KeyError as e:
            print(f"Ошибка: книга с названием '{review_data['book_title']}' не найдена. Отзыв не создан.")
            continue


if __name__ == "__main__":
    # Настройка окружения Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')  # Замените на ваш проект
    django.setup()


    json_file_path = os.path.join(os.path.dirname(__file__), "data.json")

    if os.path.exists(json_file_path):
        load_data_from_json(json_file_path)
        print("Загрузка данных завершена!")
    else:
        print(f"Файл {json_file_path} не найден!")