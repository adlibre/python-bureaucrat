# Python Bureaucrat

The Procfile process manager for Python Virtual Environments.

## Installation

Install with `pip install git+git@github.com:adlibre/python-bureaucrat.git`.

## Config

To use Bureaucrat you will need to have created a [Procfile](https://devcenter.heroku.com/articles/procfile) and
[.env](https://devcenter.heroku.com/articles/procfile#setting-local-environment-variables) file in your virtual env
root.

## Usage

Basic options are _start_, _stop_ and _start_.

    usage: Bureaucrat [-h] {start,stop,restart} ...

    Bureaucrat - the Procfile manager for Python Virtual Environments

    positional arguments:
      {start,stop,restart}
        start               Starts daemons
        stop                Stops daemons
        restart             Restarts daemons

    optional arguments:
      -h, --help            show this help message and exit


Additional arguments for specifying a custom location for `Procfile` and `.env`

    usage: Bureaucrat start [-h] [--venv VENV] [--procfile PROCFILE]
                            [--envfile ENVFILE]

    optional arguments:
      -h, --help           show this help message and exit
      --venv VENV          Virtual Env Root
      --procfile PROCFILE  Procfile path
      --envfile ENVFILE    .env file path


## Status

Basic functionality exists, however there are still a lot of [features to implement](TODO.md). 
This should be considered Alpha status.
