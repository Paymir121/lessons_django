from sqlalchemy import text

from index_sql.connection import DBConnection


def create_new_index(index_name: str, table_name: str, column_name: str):
    with conn.session as session:
        session.execute(text(f"""
            CREATE INDEX IF NOT EXISTS {index_name} 
            ON {table_name} ({column_name});
        """))

if __name__ == '__main__':
    conn = DBConnection()
    create_new_index(index_name="idx_orders_customer_id", table_name="orders", column_name="customer_id")
    print("ID.4: Done")