import os
import sqlite3


def remove_pin(shortcut):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    db_path = os.path.join(project_root, "data", "database.db")

    try:
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()

            cur.execute("DELETE from pins WHERE shortcut = ?", (shortcut,))

            if cur.rowcount > 0:
                print(f'"{shortcut}" shortcut deleted')
            else:
                print(f'No pin found with shortcut: "{shortcut}"')

            con.commit()

    except sqlite3.Error as e:
        print(f"Error while deleting pin: {e}")
