import random

from index_sql.connection import DBConnection
import index_sql.models as dm
from datetime import date
import index_sql.utils as utls

def create_new_order(customer_id: int):
    try:
        with conn.session as session:
            order = dm.Order(customer_id=customer_id, order_date=date.today())
            session.add(order)
            print("BL.1: Создан заказ:", order)

            for i in range(5):
                item = dm.OrderItem(
                    order=order,
                    product_name=f"{utls.random_string(5)} {i}",
                    quantity=random.randint(-10, 10),
                    price=100
                )
                session.add(item)
                print("BL.2: Добавлен товар:", item)

            session.commit()
            print("BL.4: Done")
    except Exception as e:
        print("BL.5: Ошибка:", e)
        session.rollback()
        print("BL.5.1: rollback")
    print("BL.5: Сессия закрыта")

if __name__ == '__main__':
    conn = DBConnection()
    create_new_order(customer_id=30001)
    print("BL.5: Done")