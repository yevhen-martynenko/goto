import os
import sqlite3


def get_pins():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    db_path = os.path.join(project_root, "data", "database.db")

    try:
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()

            cur.execute("SELECT * FROM pins")
            pins = cur.fetchall()

            return pins

    except sqlite3.Error as e:
        print(f"Error while retrieving data: {e}")
        return []


def print_pins(pins):
    for pin in pins:
        print(f"{pin[1]} \t {pin[0]}")


def show_pins():
    pins = get_pins()
    print_pins(pins)
