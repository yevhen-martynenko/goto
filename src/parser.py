import argparse


def configure_parser():
    parser = argparse.ArgumentParser(
        prog="goto",
        description="Go to a directory passed as an argument",
        add_help=False,
        formatter_class=argparse.HelpFormatter
    )

    commands_group = parser.add_argument_group("Commands")
    commands = commands_group.add_mutually_exclusive_group()
    commands.add_argument(
        "--pin",
        type=str,
        nargs="?",
        metavar="DIR",
        help="pin a directory to a search term"
    )
    commands.add_argument(
        "--pins",
        action="store_true",
        help="lists all the pinned search terms"
    )
    commands.add_argument(
        "--unpin",
        type=str,
        nargs="?",
        metavar="DIR",
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
