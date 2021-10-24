#!/usr/bin/env python
"""Tests for `{{ cookiecutter.project_slug }}` package."""
{%- if cookiecutter.command_line_interface|lower == 'typer' %}
from typer.testing import CliRunner
from {{ cookiecutter.project_slug }}.cli import app
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner
from {{ cookiecutter.project_slug }} import cli
{%- endif %}
import {{ cookiecutter.project_slug }}
{%- if cookiecutter.command_line_interface|lower == 'typer' %}

runner = CliRunner()
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}


def test_command_line_interface():
  """Test the CLI."""
  runner = CliRunner()
  result = runner.invoke(cli.main)
  assert result.exit_code == 0
  assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
  help_result = runner.invoke(cli.main, ['--help'])
  assert help_result.exit_code == 0
  assert '--help  Show this message and exit.' in help_result.output

{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'typer' %}


def test_app():
  """Test the version subcommand"""
  result = runner.invoke(app, ['version'])
  assert result.exit_code == 0
  assert {{ cookiecutter.project_slug }}.__version__ in result.stdout
{%- endif %}


def test_version():
  """Test there is a version string"""
  assert {{ cookiecutter.project_slug }}.__version__ == '{{ cookiecutter.version }}'
