from datetime import date, timedelta
import random
from sqlalchemy.exc import SQLAlchemyError
from index_sql.connection import DBConnection
import index_sql.models as dm
from index_sql.utils import random_string


def generate_data(num_records):
    """Генератор тестовых данных"""
    start = date(2020, 1, 1)
    end = date(2023, 12, 31)

    for i in range(num_records):
        yield {
            "customer": {
                "name": f"Заказчик {i} {random_string(10)}",
                "email": f"customer{i}@{random_string(10)}.com"
            },
            "order": {
                "order_date": start + timedelta(days=random.randint(0, (end - start).days))
            },
            "item": {
                "product_name": f"Продукт {random_string(11)}",
                "quantity": random.randint(1, 10000),
                "price": random.randint(1, 100000)
            }
        }


def bulk_insert(batch_size=1000, total_records=1000000):
    try:
        with conn.session as session:
            for i, data in enumerate(generate_data(total_records), 1):
                # Создаем объекты и устанавливаем связи
                customer = dm.Customer(**data["customer"])
                order = dm.Order(**data["order"], customer=customer)
                item = dm.OrderItem(**data["item"], order=order)

                session.add_all([customer, order, item])

                # Пакетная вставка
                if i % batch_size == 0:
                    try:
                        session.commit()
                        print(f"ID.1: Inserted {i} records")
                    except SQLAlchemyError as e:
                        session.rollback()
                        print(f"Error at batch {i // batch_size}: {str(e)}")
                        raise

            # Финализация оставшихся записей
            try:
                session.commit()
                print(f"ID.1: Final batch inserted ({i} total records)")
            except SQLAlchemyError as e:
                session.rollback()
                print(f"Final batch error: {str(e)}")
                raise

    except Exception as e:
        print(f"Critical error: {str(e)}")
        raise
    finally:
        conn.session.close()
        print("ID.2: Done")


if __name__ == '__main__':
    conn = DBConnection()
    bulk_insert(batch_size=5000)  # Увеличьте batch_size для лучшей производительности