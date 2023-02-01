# id | name | description| price
# id | name | description | price | photo | memory | color |brand | call_back | url
from db import conn, cursor

def create_table_product():
    query = """
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR,
            description VARCHAR,
            price INTEGER,
            photo VARCHAR,
            memory VARCHAR,
            color VARCHAR,
            brand VARCHAR,
            call_back VARCHAR,
            url VARCHAR
        );"""
    cursor.execute(query=query)
    conn.commit()


    
def insert_product(name: str, description: str, price: int, photo: str, memory: str,color: str, brand: str, call_back: str,url: str):
    query = f"""
        INSERT INTO products (
            name, description, price, photo, memory, color, brand, call_back, url
        )VALUES (
            '{name}', '{description}', {price}, '{photo}', '{memory}', '{color}', '{brand}', '{call_back}', '{url}'
        );"""
    cursor.execute(query=query)
    conn.commit()

def get_brands():
    query = """
        SELECT count(brand), brand
        FROM products
        GROUP BY brand;"""
    cursor.execute(query=query)
    response = cursor.fetchall()
    return {i[1]:i[1].title() for i in response}



# get_brands()
def get_phones_callback(brand: str = None):
    if brand is None:
        query = f"""
        SELECT call_back
        FROM products;"""
    else:
        query = f"""
            SELECT call_back
            FROM products
            WHERE brand = '{brand}';"""
    cursor.execute(query=query)
    response = cursor.fetchall()
    return {i[0]:i[0].title().replace('_', ' ') for i in response}


def get_info_phone(call_back: str ):


    query = f"""
        SELECT *
        FROM products
        where call_back = '{call_back}';"""
    cursor.execute(query=query)
    response = cursor.fetchall()
    return response
