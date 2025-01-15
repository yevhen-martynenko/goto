from src import configure_parser
from src.commands import add_pin, remove_pin, show_pins


def main():
    parser = configure_parser()
    args = parser.parse_args()

    print(f"{args}\n")

    if args.help:
        parser.print_help()
    if args.version:
        # TODO: print_version()
        pass

    if args.pins:
        show_pins()

    if args.pin:
        directory = args.pin
        add_pin(directory)

    if args.unpin:
        directory = args.unpin
        remove_pin(directory)


if __name__ == "__main__":
    main()
