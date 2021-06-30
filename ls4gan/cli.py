"""Console script for ls4gan."""
import sys
import click
import ls4gan

@click.group()
@click.pass_context
def cli(ctx):
    '''
    LS4GAN main command line interface
    '''
    ctx.obj = {}


@cli.command()
def version():
    'Print the version'
    click.echo(ls4gan.__version__)


def main():
    cli(obj=None)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
