# Python Bureaucrat

The Procfile process manager for Python Virtual Environments.

Bureaucrat provides additional support for _Deployfile_ based deployment task management.

## Installation

Install with `pip install -e git+git@github.com:adlibre/python-bureaucrat.git#egg=bureaucrat` or 
`pip install git+https://github.com/adlibre/python-bureaucrat.git#egg=bureaucrat`.

## Config

To use Bureaucrat you will need to have created a [Procfile](https://devcenter.heroku.com/articles/procfile), Deployfile
and [.env](https://devcenter.heroku.com/articles/procfile#setting-local-environment-variables) file in your virtual env
root.

## Usage

Basic options are _start_, _stop_, _restart_ and _deploy_.

    usage: Bureaucrat [-h] {start,stop,restart,deploy} ...

    Bureaucrat - the Procfile manager for Python Virtual Environments

    positional arguments:
      {start,stop,restart,deploy}
        start               Starts daemons
        stop                Stops daemons
        restart             Restarts daemons
        deploy              Run tasks in Deployfile

    optional arguments:
      -h, --help            show this help message and exit


Additional arguments for specifying a custom location for `Procfile`, `.env` and log files.

    usage: Bureaucrat start [-h] [--venv VENV] [--procfile PROCFILE]
                            [--envfile ENVFILE] [--logpath LOGPATH]

    optional arguments:
      -h, --help           show this help message and exit
      --venv VENV          Virtual Env Root
      --procfile PROCFILE  Procfile path
      --envfile ENVFILE    .env file path
      --logpath LOGPATH    log file path


## Status

Basic functionality exists, however there are still a lot of [features to implement](TODO.md). 
This should be considered Alpha status.
