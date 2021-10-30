"""Command line interface for {{cookiecutter.project_slug}}."""
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'typer' %}
import typer
{%- endif %}
import debugpy
import pendulum
from {{ cookiecutter.project_slug }} import __version__


{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main():
  """Console script for {{cookiecutter.project_slug}}."""
  parser = argparse.ArgumentParser()
  parser.add_argument('_', nargs='*')
  args = parser.parse_args()

  print("Arguments: " + str(args._))
  print("Replace this message by putting your code into "
        "{{cookiecutter.project_slug}}.cli.main")
  return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
def main(args=None):
  """Console script for {{cookiecutter.project_slug}}."""
  click.echo("Replace this message by putting your code into "
              "{{cookiecutter.project_slug}}.cli.main")
  click.echo("See click documentation at https://click.palletsprojects.com/")
  return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'typer' %}

app = typer.Typer()


@app.callback()
def main(debugger: bool = False,
         debug_host: str = "127.0.0.1",
         debug_port: int = 5678):
  """Console script for {{cookiecutter.project_slug}}."""
  # Stash the global option values in state which is accessible to subcommands
  if debugger:
    typer.echo(
        f"Waiting for debugger client to attach to {debug_host}:{debug_port}")
    debugpy.listen(5678)
    debugpy.wait_for_client()
  return 0


@app.command()
def version():
  """Print the version and exit"""
  typer.echo(__version__)
  return 0


@app.command()
def bugged(inbound: str = 'garbage'):
  """Example breakpoint for use with --debugger"""
  typer.echo(f"{inbound} in {inbound} out...")
  # Note, you can also click the red dot to the left of the line number in vs code to set a breakpoint
  debugpy.breakpoint()
  return 0


@app.command()
def future(days: int = 100):
  """Print a RFC 3339 datetime some number of days in the future."""
  stamp = pendulum.now()
  later = stamp.add(days=days)
  typer.echo(later.to_rfc3339_string())
  return 0
{%- endif %}


if __name__ == "__main__":
  sys.exit(main())  # pragma: no cover
