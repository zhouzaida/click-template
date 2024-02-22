import click
from ..cli import cli


@cli.command()
@click.argument('name', type=str)
@click.option('--count', default=1, help='Number of greetings.')
def hello(name, count):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")
