#!/usr/bin/env python
"""Tests for `{{ cookiecutter.project_slug }}` package."""
from typer.testing import CliRunner
from {{ cookiecutter.project_slug }}.cli import app
import {{ cookiecutter.project_slug }}


runner = CliRunner()


def test_app():
  """Test the version subcommand"""
  result = runner.invoke(app, ['version'])
  assert result.exit_code == 0
  assert {{ cookiecutter.project_slug }}.__version__ in result.stdout


def test_version():
  """Test there is a version string"""
  assert {{ cookiecutter.project_slug }}.__version__ == '{{ cookiecutter.version }}'
