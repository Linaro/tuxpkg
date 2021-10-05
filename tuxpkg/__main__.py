import argparse
import sys
import tuxpkg
import tuxpkg.get_makefile


def main():
    parser = argparse.ArgumentParser(
        prog="tuxpkg",
        description=tuxpkg.__doc__.strip(),
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {tuxpkg.__version__}",
    )
    parser.set_defaults(func=parser.print_usage)

    subparsers = parser.add_subparsers(
        title="Subcommands",
        description="All tuxpkg is available through one of its subcommands.",
    )

    get_makefile = subparsers.add_parser(
        "get-makefile",
        aliases=["mk"],
        help="Prints the path to the tuxpkg shared makefile. It can be included in a Makefile using a construct like like `$(include $(shell tuxpkg get-makefile))`.",
    )
    get_makefile.set_defaults(func=tuxpkg.get_makefile.run)

    options = parser.parse_args(sys.argv[1:])
    options.func()

    return 0


def run() -> None:
    if __name__ == "__main__":
        sys.exit(main())


run()
