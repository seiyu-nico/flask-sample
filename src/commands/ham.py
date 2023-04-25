import click
from flask.cli import with_appcontext
from libs.random.random import Random


@click.command('ham', help="hamコマンド")
@with_appcontext
def handler():
    print(f'Hello ham! {Random.get_random_int()}')
