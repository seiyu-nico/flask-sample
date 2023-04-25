import click
from flask.cli import with_appcontext
from libs.random.random import Random


@click.command('spam', help="spamコマンド")
@with_appcontext
def handler():
    print(f'Hello spam! {Random.get_random_int()}')
