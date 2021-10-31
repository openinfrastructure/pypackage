"""Command line interface for {{cookiecutter.project_slug}}."""
import sys
import typer
import debugpy
import pendulum
from {{ cookiecutter.project_slug }} import __version__

app = typer.Typer()


@app.callback()
def main(
  debugger: bool = typer.Option(False, envvar="DEBUGGER"),
  debugger_port: int = typer.Option(5678, envvar="DEBUGGER_PORT"),
):
  """Console script for {{cookiecutter.project_slug}}."""
  if debugger:
    typer.echo(f"Waiting for debugger client to attach to port {debugger_port}")
    debugpy.listen(debugger_port)
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


@app.command()
def mandatory(required: str = typer.Option(..., envvar="REQUIRED")):
  """Example of a required 'option' with a 12-Factor style env var and no default value.

  This is often used for api_key and other auth related flags.
  """
  typer.echo(f"Required 'option': {required}")
  return 0


if __name__ == "__main__":
  sys.exit(main())  # pragma: no cover
