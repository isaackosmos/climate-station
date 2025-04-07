import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "aaa.db")


def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL NOT NULL,
            humidity REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()


def insert_data(temperature, humidity):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sensor_data (temperature, humidity)
        VALUES (?, ?)
    ''', (temperature, humidity))
    conn.commit()
    conn.close()


def fetch_data(limit=15):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM sensor_data
        ORDER BY timestamp DESC
        LIMIT ?
    ''', (limit,))
    data = cursor.fetchall()
    conn.close()
    return data
