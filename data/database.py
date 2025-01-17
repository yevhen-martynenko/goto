import os
import sqlite3


def create_db():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    db_path = os.path.join(project_root, "data", "database.db")

    try:
        with sqlite3.connect(db_path) as con:
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
