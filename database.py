import sqlite3


def initialize_database(cursor, drop_existing_tables=False):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_information (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            name TEXT UNIQUE
        )
    """)

    # table to store conversations, each associated with a user
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_conversations (
            conversation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_information_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            binary_rating INTEGER,
            FOREIGN KEY (user_information_id) REFERENCES user_information(id)
        )
    """)
    # table to store individual interactions (conversations) within a group of conversations
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_interactions (
        interaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        conversation_id INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        input TEXT NOT NULL,
        output TEXT,
        FOREIGN KEY (conversation_id) REFERENCES user_conversations(interaction_id)

        )
    """)


def get_connection():
    return sqlite3.connect("chat_history.db")
