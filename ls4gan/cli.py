"""Console script for ls4gan."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for ls4gan."""
    click.echo("Replace this message by putting your code into "
               "ls4gan.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
