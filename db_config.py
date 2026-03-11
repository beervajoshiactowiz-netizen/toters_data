import pymysql
from pymysql import connect
import json

def make_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='actowiz',
        database='Products_db'
    )
    return conn

def create(table_name: str):
    q = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
    id                  INTEGER PRIMARY KEY,
    name                TEXT,
    original_price      BIGINT,
    original_price_usd  DECIMAL(10, 2),
    category_id         INTEGER,
    store_id            INTEGER,
    store_item_id       INTEGER,
    imgs                JSON,
    final_price         BIGINT,
    final_price_usd     DECIMAL(10, 2),
    local_currency      VARCHAR(10),
    measurement_value   VARCHAR(20),
    measurement_unit    VARCHAR(10),
    stock_level         INTEGER,
    is_available        BOOLEAN,
    unavailable_until   TIMESTAMP,
    reward_id           INTEGER,
    reward_points       INTEGER,
    reward_tier         VARCHAR(10),
    offers              JSON,
    Diet                JSON,
    substance_free_diet JSON,
    allergies           JSON
);
    """
    conn = make_connection()
    cursor = conn.cursor()
    cursor.execute(q)
    conn.commit()
    conn.close()

def fetch():
    pass

def insert_into_db(table_name: str, data: list):

    Values = []
    for item in data:
        item['imgs'] = json.dumps(item.get('imgs') or [])
        item['offers'] = json.dumps(item.get('offers') or [])
        item['Diet'] = json.dumps(item.get('Diet') or [])
        item['substance_free_diet'] = json.dumps(item.get('substance_free_diet') or [])
        item['allergies'] = json.dumps(item.get('allergies') or [])
        Values.append(tuple(item.values()))

    # build query from first item's keys
    cols = ", ".join(data[0].keys())
    placeholders = ", ".join(['%s'] * len(data[0].keys()))
    q = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
    conn = make_connection()
    cursor = conn.cursor()
    cursor.executemany(q, Values)
    conn.commit()


if __name__ == '__main__':
    pass