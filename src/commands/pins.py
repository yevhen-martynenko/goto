import os
import sqlite3


def get_pins():
    db_name = os.path.join("data", "database.db")

    try:
        with sqlite3.connect(db_name) as con:
            cur = con.cursor()

            cur.execute("SELECT * FROM pins")
            pins = cur.fetchall()

            return pins

    except sqlite3.Error as e:
        print(f"Error while creating database: {e}")
        return []


def print_pins(pins):
    for pin in pins:
        print(pin)


def show_pins():
    pins = get_pins()
    print_pins(pins)
