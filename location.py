from db import cursor, conn
from datetime import datetime

def create_table_location():
    query = """
    CREATE TABLE IF NOT EXISTS location (
        id SERIAL PRIMARY KEY,
        chat_id INT,
        latitude FLOAT,
        longitude FLOAT,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );"""
    cursor.execute(query=query)
    conn.commit()
    print('create table location successfully')

def insert_location(chat_id: int, 
                    latitude: float, 
                    longitude: float):
    query = f"""
    INSERT INTO location(
        chat_id, latitude, longitude
    )VALUES (
        {chat_id}, {latitude}, {longitude}
        );"""
    cursor.execute(query=query)
    conn.commit()
    print('create table location successfully')

def update_location(chat_id: int,
                    latitude: float, 
                    longitude: float):
    date = datetime.now()
    query = f"""
        UPDATE location
        SET latitude= {latitude}, longitude = {longitude}, create_at = CURRENT_TIMESTAMP 
        WHERE chat_id = {chat_id};"""
    cursor.execute(query=query)
    conn.commit()

def does_location_exist(chat_id: int):
    query = f""" 
        SELECT * 
        FROM locations
        WHERE chat_id = {chat_id};"""
    cursor.execute(query=query)
    response = cursor.fetchone()
    if response:
        return True
    return False

# create_table_location()
