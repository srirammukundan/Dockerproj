#!/usr/bin/env python
import click

@click.command()
def hello():
    click.echo('hello word!')

if __name__ == '__main__':
    hello()