import os

from data import create_db
from src import configure_parser
from src.commands import add_pin, go_to_pin, remove_pin, show_pins


def is_db_created():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    db_path = os.path.join(project_root, "data", "database.db")
    return os.path.exists(db_path)


def main():
    parser = configure_parser()
    args = parser.parse_args()

    if not is_db_created():
        create_db()

    if args.help:
        parser.print_help()
    if args.version:
        # TODO: print_version()
        pass

    if args.pins:
        show_pins()

    if args.pin:
        shortcut = args.pin
        add_pin(shortcut)

    if args.unpin:
        shortcut = args.unpin
        remove_pin(shortcut)

    if args.goto_pin:
        go_to_pin(args.goto_pin)


if __name__ == "__main__":
    main()
