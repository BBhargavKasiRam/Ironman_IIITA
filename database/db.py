import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "agent_data.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS flagged_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT,
            risk_score INTEGER,
            action_taken TEXT
        )
    """)

    conn.commit()
    conn.close()


def store_flagged_message(message, risk_score, action):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO flagged_messages (message, risk_score, action_taken)
        VALUES (?, ?, ?)
    """, (message, risk_score, action))

    conn.commit()
    conn.close()


def get_all_flagged():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM flagged_messages")
    rows = cursor.fetchall()

    conn.close()
    return rows
