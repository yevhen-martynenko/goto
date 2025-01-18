import os
import sqlite3


def go_to_pin(pin):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    db_path = os.path.join(project_root, "data", "database.db")

    try:
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()

            cur.execute("SELECT directory_path FROM pins WHERE shortcut = ?", (pin,))
            path = cur.fetchone()[0]

            if path:
                os.chdir(path)
                print(os.getcwd())
            else:
                print(f"No pin found for shortcut '{pin}'.")

    except sqlite3.Error as e:
        print(f"Error while accessing the database: {e}")
