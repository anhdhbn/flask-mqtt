# coding=utf-8
from app import app, db
import click


@app.cli.command("createall")
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        click.echo('Dropped database.')
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")