from sqlalchemy import text

from index_sql.connection import DBConnection


def analyze_index_usage(conn):
    with conn.session as session:
        print("A.1: Анализ запроса для order_items:")
        result = session.execute(
            text("""
            EXPLAIN ANALYZE 
            SELECT * FROM order_items 
            WHERE order_id = 123 AND price > 10000;
        """
                                      )
                                 )
        for row in result:
            print("result =",row[0])

        print("\nA.2: Анализ запроса для orders:")
        result = session.execute(
            text("""
            EXPLAIN ANALYZE 
            SELECT * FROM orders 
            WHERE customer_id = 1;
        """
                                      )
                                 )
        for row in result:
            print("A.3: result =",row[0])


if __name__ == '__main__':
    conn = DBConnection()
    analyze_index_usage(conn)
    print("A.4: Done")