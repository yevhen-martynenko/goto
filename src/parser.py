import argparse


def configure_parser():
    parser = argparse.ArgumentParser(
        prog="goto",
        description="description",
        add_help=False
    )

    commands_group = parser.add_argument_group("Commands")
    commands = commands_group.add_mutually_exclusive_group()
    commands.add_argument(
        "pin",
        type=str,
        nargs="?",
        help="pin a directory to a search term"
    )
    commands.add_argument(
        "pins",
        type="store_true",
        nargs="?",
        help="lists all the pinned search terms"
    )
    commands.add_argument(
        "unpin",
        type=str,
        nargs="?",
        help="unpin a search term"
    )

    options_group = parser.add_argument_group("Options")
    options = options_group.add_mutually_exclusive_group()
    options.add_argument(
        "-h", "--help",
        action="store_true",
        help="show this screen"
    )
    options.add_argument(
        "-v", "--version",
        action="store_true",
        help="show version"
    )

    return parser

