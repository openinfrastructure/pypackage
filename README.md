OIS Python Template
===

Use this as a starting point for command line tools.

Quick Start
===

```bash
pip install -U cookiecutter
cookiecutter https://github.com/openinfrastructure/pypackage.git
```

Libraries
===

The following libraries are preferred.

| Use Case | Library        |
| -------- | -------        |
| Time     | Pendulum       |
| Retries  | Tenacity       |
| CLI      | Typer or Click |
| Debugger | [ptvsd][ptvsd] |

[ptvsd]: https://github.com/microsoft/ptvsd
