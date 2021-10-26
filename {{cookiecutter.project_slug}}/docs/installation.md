# Installation

## Stable release

To install {{ cookiecutter.project_name }}, run this command in your terminal:

```sh
pip install {{ cookiecutter.project_slug }}
```

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always install the most recent stable release.

If you don't have [pip] installed, this [Python installation guide][guide] can guide
you through the process.

## From sources

The sources for {{ cookiecutter.project_name }} can be downloaded from the [Github repo][repo].

You can either clone the public repository:

```sh
git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
```

Or download the [tarball]:

```sh
curl -OJL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/master
```

Once you have a copy of the source, you can install it with:

```sh
python setup.py install
```

[pip]: https://pip.pypa.io
[guide]: http://docs.python-guide.org/en/latest/starting/installation/
[repo]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
[tarball]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/master
