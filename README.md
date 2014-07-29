# Python Bureaucrat

[![PyPI version](https://badge.fury.io/py/bureaucrat.svg)](https://pypi.python.org/pypi/bureaucrat/)

The _Procfile_ & _Deployfile_ process manager for Python Virtual Environments.

Bureaucrat provides support for _Deployfile_ based deployment task management. A _Deployfile_ is basically a _Procfile_
by another name. It is used to define the deployment commands for your project.

## Installation

Install with `pip install -e git+git@github.com:adlibre/python-bureaucrat.git#egg=bureaucrat` or 
`pip install git+https://github.com/adlibre/python-bureaucrat.git#egg=bureaucrat`.

## Config

To use Bureaucrat you will need to have created a [Procfile](https://devcenter.heroku.com/articles/procfile), Deployfile
and [.env](https://devcenter.heroku.com/articles/procfile#setting-local-environment-variables) file in your virtual env
root.

## Usage

Basic options are _start_, _stop_, _restart_, _deploy_ and _init.

    usage: Bureaucrat [-h] {start,stop,restart,deploy,init} ...
    
    Bureaucrat - the Procfile & Deployfile manager for Python Virtual Environments
    
    positional arguments:
      {start,stop,restart,deploy,init}
        start               Starts Procfile processes
        stop                Stops Procfile processes
        restart             Restarts Procfile processes
        deploy              Run tasks in Deployfile
        init                Run Deployfile tasks and then start Procfile processes
    
    optional arguments:
      -h, --help            show this help message and exit

### Start / Stop / Restart Arguments

Additional arguments for specifying a custom location for `Procfile`, `.env` and log files.

    usage: Bureaucrat start [-h] [--venv VENV] [--app APP] [--procfile PROCFILE]
                            [--envfile ENVFILE] [--logpath LOGPATH]
                            [--pidpath PIDPATH]
    
    optional arguments:
      -h, --help           show this help message and exit
      --venv VENV          Virtualenv root
      --app APP            Application root
      --procfile PROCFILE  Procfile path
      --envfile ENVFILE    .env file path
      --logpath LOGPATH    log file path
      --pidpath PIDPATH    pid file path

Example:

    $ bureaucrat start
    Launching web: gunicorn project.wsgi:application --log-file log/gunicorn.$LOGFILE --bind unix:run/gunicorn.sock

### Deploy Arguments

    usage: Bureaucrat deploy [-h] [--venv VENV] [--app APP]
                             [--deployfile DEPLOYFILE] [--envfile ENVFILE]
                             [--logpath LOGPATH]
    
    optional arguments:
      -h, --help            show this help message and exit
      --venv VENV           Virtualenv root
      --app APP             Application root
      --deployfile DEPLOYFILE
                            Deployfile path
      --envfile ENVFILE     .env file path
      --logpath LOGPATH     log file path

Example:

    $ bureaucrat deploy
    Running task syncdb: manage.py syncdb --noinput
    Running task migrate: manage.py migrate --noinput
    Running task collectstatic: manage.py collectstatic --noinput

## Status

Basic functionality exists, however there are a few [features to implement](TODO.md).
This should be considered Alpha status.
