from sqlalchemy import text

from index_sql.connection import DBConnection


def drop_index(index_name: str):
    with conn.session as session:
        # Пример удаления индекса по product_name, если он не используется
        session.execute(text(f"DROP INDEX IF EXISTS {index_name}"))
        print(f"Индекс {index_name} удален")

if __name__ == '__main__':
    conn = DBConnection()
    drop_index(index_name="idx_order_items_product_name")
    print("ID.5: Done")