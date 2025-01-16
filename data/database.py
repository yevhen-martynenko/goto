import os
import sqlite3


def create_db():
    db_name = os.path.join("data", "database.db")

    try:
        with sqlite3.connect(db_name) as con:
            cur = con.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS pins (
                    directory_path TEXT,
                    shortcut TEXT UNIQUE
                )
            """)

            con.commit()

    except sqlite3.Error as e:
        print(f"Error while creating database: {e}")
