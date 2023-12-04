import psycopg2
from psycopg2.extras import RealDictCursor


class DBManager:
    def __init__(self):
        self.conn = psycopg2.connect(
            "dbname=your_db user=your_user password=your_password"
        )

    def save_trade(self, trade_data):
        with self.conn.cursor() as cur:
            query = """
            INSERT INTO trades (token, order_type, price, quantity, timestamp)
            VALUES (%s, %s, %s, %s, %s)
            """
            cur.execute(
                query,
                (
                    trade_data["token"],
                    trade_data["order_type"],
                    trade_data["price"],
                    trade_data["quantity"],
                    trade_data["timestamp"],
                ),
            )
            self.conn.commit()

    def update_trade(self, trade_id, update_data):
        with self.conn.cursor() as cur:
            query = """
            UPDATE trades
            SET price = %s, quantity = %s
            WHERE id = %s
            """
            cur.execute(
                query, (update_data["price"], update_data["quantity"], trade_id)
            )
            self.conn.commit()

    def get_trade(self, trade_id):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            query = "SELECT * FROM trades WHERE id = %s"
            cur.execute(query, (trade_id,))
            return cur.fetchone()

    def get_all_trades(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            query = "SELECT * FROM trades"
            cur.execute(query)
            return cur.fetchall()
