import click
from test import *

@click.group()
def cli():
    pass

@click.command()
def turn_on():
    click.echo('Turning the lights on')
    # Call your function to turn the lights on

@click.command()
def turn_off():
    click.echo('Turning the lights off')
    # Call your function to turn the lights off

@click.command()
@click.argument('level', type=int)
def set_brightness(level):
    click.echo(f'Setting brightness to {level}')
    # Call your function to set the brightness
    
cli.add_command(turn_on)
cli.add_command(turn_off)
cli.add_command(set_brightness)

def main():
    cli.main(standalone_mode=False)

if __name__ == "__main__":
    main()