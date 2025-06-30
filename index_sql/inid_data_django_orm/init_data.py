from datetime import date, timedelta
import random
from sqlalchemy.exc import SQLAlchemyError
from index_sql.connection import DBConnection
import index_sql.inid_data_django_orm.models as dm
from index_sql.utils import random_string


import random
from datetime import datetime, timedelta
from sqlalchemy.exc import SQLAlchemyError
from faker import Faker

fake = Faker()


def generate_data(num_records):
    """Генератор тестовых данных для Author, Book и Review"""
    start = datetime(2020, 1, 1)
    end = datetime(2023, 12, 31)

    for i in range(num_records):
        yield {
            "author": {
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": f"author{i}@{fake.domain_name()}",
                "is_active": random.choice([True, False])
            },
            "book": {
                "title": f"{fake.catch_phrase()} {random_string(5)}",
                "published_date": start + timedelta(days=random.randint(0, (end - start).days)),
                "price": round(random.uniform(5.99, 99.99), 2),
                "discount": round(random.uniform(0, 30.00), 2),
                "metadata": {
                    "genre": random.choice(["fiction", "non-fiction", "science", "biography"]),
                    "pages": random.randint(50, 1000)
                }
            },
            "review": {
                "rating": random.randint(1, 5),
                "comment": fake.text(max_nb_chars=200) if random.choice([True, False]) else None,
                "created_at": datetime.now() - timedelta(days=random.randint(0, 365))
            }
        }

def bulk_insert(batch_size=100, total_records=100):
    try:
        with conn.session as session:
            for i, data in enumerate(generate_data(total_records), 1):
                # Создаем объекты и устанавливаем связи
                author = dm.Author(**data["author"])
                book = dm.Book(**data["book"], author=author)
                review = dm.Review(**data["review"], book=book)

                session.add_all([author, book, review])

                # Пакетная вставка
                if i % batch_size == 0:
                    try:
                        session.commit()
                        print(f"Inserted {i} records")
                    except SQLAlchemyError as e:
                        session.rollback()
                        print(f"Error at batch {i // batch_size}: {str(e)}")
                        raise

            # Финализация оставшихся записей
            try:
                session.commit()
                print(f"Final batch inserted ({i} total records)")
            except SQLAlchemyError as e:
                session.rollback()
                print(f"Final batch error: {str(e)}")
                raise

    except Exception as e:
        print(f"Critical error: {str(e)}")
        raise
    finally:
        conn.session.close()
        print("Done")


if __name__ == '__main__':
    conn = DBConnection()
    bulk_insert(batch_size=5)  # Увеличьте batch_size для лучшей производительности