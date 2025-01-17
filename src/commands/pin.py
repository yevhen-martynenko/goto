import os
import sqlite3


def add_pin(shortcut):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    db_path = os.path.join(project_root, "data", "database.db")
    directory_path = os.getcwd()

    try:
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()

            cur.execute(
                "INSERT INTO pins (directory_path, shortcut) VALUES (?, ?)",
                (directory_path, shortcut),
            )

            con.commit()
            print(f'"{shortcut}" shortcut added')

    except sqlite3.Error as e:
        print(f"Error while adding pin: {e}")
