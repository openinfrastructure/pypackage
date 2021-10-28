# Open Infrastructure Services Python Template

Use this as a starting point to build a new command line tools.  This template is opinionated about the libraries used and strives to use modern techniques as of late 2021.

This template is built for SRE/DevOps engineers needing to write a controller interface similar to kubectl.  The template is appropriate for any small API integration or data processing utility.

## Quick Start

Choose a project name with no spaces to make things align nicely with the python package name and the URL slug.

```bash
pip install -U cookiecutter
cookiecutter https://github.com/openinfrastructure/pypackage
```

Then cd to the generated directory and initialize the git repository:

```sh
git init
git add .
git commit -m 'Initial commit - cookiecutter https://github.com/openinfrastructure/pypackage'
```

Setup a clean development environment to work in:

```sh
python3 -mvenv env
source env/bin/activate
pip install -r requirements_dev.txt
```

Finally, install an editable version of the new package so you can execute the command line utility against your live code.

```
pip install --editable .
```

You should have a fully functional command line utility at this point:

<details>
  <summary>emanon --help</summary>

```bash
emanon --help
Usage: emanon [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  main     Console script for emanon.
  version  Print the version and exit
```
</details>

Generate documentation with `make docs`.

As you develop your program, use `make` to run tests and keep the format in style.

Refer to the [developing] documentation to learn how to connect VS Code's integrated debugger to the newly generated program.

## Library Opinions

The following libraries are preferred.  Libraries which are recommended by their upstream are preferred, for example Sphinx [recommends][Sphinx] MyST for markdown.  Battle tested, boring, libraries are preferred.

If there's a better library for the use case please let us know by filing an issue.

| Use Case               | Library                  |
| ---------------------- | ------------------------ |
| Command Line Interface | [Typer]                  |
| Config Files           | No opinion (yet)         |
| Structured Logging     | [structlog]              |
| Documentation          | [Sphinx] [MyST] markdown |
| Date Time              | [Pendulum]               |
| HTTP Client            | [requests]               |
| Retries                | [Tenacity]               |
| RPC                    | [grpc]                   |
| JSON loading           | [Dacite]'s `from_dict`   |
| JSON validation        | [jsonschema]             |
| Debugger               | [debugpy]                |
| Testing                | [pytest]                 |
| Testing Matrix         | [tox]                    |
| Web App                | [flask]                  |
| Web App with DB        | [django], [drf]          |
| API Specification      | [OpenAPI]                |
| File Uploads           | NGINX + uwsgi            |

[debugpy]: https://github.com/microsoft/debugpy#debugpy---a-debugger-for-python
[Dacite]: https://github.com/konradhalas/dacite
[Typer]: https://typer.tiangolo.com/features/
[Tenacity]: https://tenacity.readthedocs.io/en/latest/
[Pendulum]: https://pendulum.eustace.io/
[pytest]: https://docs.pytest.org/en/6.2.x/
[Sphinx]: https://www.sphinx-doc.org/en/master/usage/markdown.html
[MyST]: https://myst-parser.readthedocs.io/en/latest/
[developing]: ./%7B%7Bcookiecutter.project_slug%7D%7D/docs/developing.md
[tox]: https://tox.wiki/en/latest/index.html
[flask]: https://flask.palletsprojects.com/en/2.0.x/
[django]: https://www.djangoproject.com/
[drf]: https://www.django-rest-framework.org/
[OpenAPI]: https://swagger.io/specification/
[structlog]: https://www.structlog.org/en/stable/
[requests]: https://docs.python-requests.org/en/latest/
[grpc]: https://grpc.io/docs/languages/python/
[jsonschema]: https://python-jsonschema.readthedocs.io/en/stable/#
