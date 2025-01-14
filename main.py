from src import configure_parser


def main():
    parser = configure_parser()
    args = parser.parse_args()

    print(args)


if __name__ == "__main__":
    main()
