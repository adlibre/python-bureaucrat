# Python Bureaucrat

[![Build Status](https://travis-ci.org/adlibre/python-bureaucrat.svg?branch=master)](https://travis-ci.org/adlibre/python-bureaucrat)
[![PyPI version](https://badge.fury.io/py/bureaucrat.svg)](https://pypi.python.org/pypi/bureaucrat/)

Bureaucrat provides support for _Deployfile_ based deployment task management. A _Deployfile_ is basically a _Procfile_
by another name. It is used to define the deployment commands for your project and spawn the processes required to 
run it.

_Deployfile_ commands must be idempotent.

If you're using [Docker](http://docker.io) then you might find this useful to automate your container builds.

## Installation

Install from [PyPI](https://pypi.python.org/pypi/bureaucrat/) with:

    pip install bureaucrat

Or install from source with:

    pip install git+https://github.com/adlibre/python-bureaucrat.git#egg=bureaucrat  

## Config

To use Bureaucrat you will need to create a [Procfile](https://devcenter.heroku.com/articles/procfile), Deployfile
and [.env](https://devcenter.heroku.com/articles/procfile#setting-local-environment-variables) file in your virtual env
root.

### Sample _Procfile_

The following will spawn a single gunicorn web process.

    web: gunicorn project.wsgi:application --workers $WORKERS --log-file $LOGFILE --bind 0.0.0.0:$PORT --timeout 300

### Sample _Deployfile_

The following is suitable for deploying a Django application.

    pip: pip install -r requirements.txt
    migrate: manage.py migrate --noinput
    collectstatic: manage.py collectstatic --noinput
    
### Sample _.env_

    WORKERS=4
    LOGFILE=/var/log/django-project.log
    PORT=8000

## Usage

Basic options are _start_, _stop_, _restart_, _deploy_ and _init_.

    usage: Bureaucrat [-h] {start,stop,restart,deploy,init} ...
    
    Bureaucrat - the Procfile & Deployfile manager for Python Virtual Environments
    
    positional arguments:
      {start,stop,restart,deploy,init}
        start               Starts Procfile processes
        stop                Stops Procfile processes
        restart             Restarts Procfile processes
        deploy              Run tasks in Deployfile
        init                Run Deployfile tasks and then start Procfile processes
                            in foreground
    
    optional arguments:
      -h, --help            show this help message and exit

### Start / Stop / Restart Arguments

Additional arguments for specifying a custom location for `Procfile`, `.env` and log files.

    usage: Bureaucrat start [-h] [--venv VENV] [--app APP] [--procfile PROCFILE]
                            [--envfile ENVFILE] [--logpath LOGPATH]
                            [--pidpath PIDPATH]
                            [process [process ...]]
    
    positional arguments:
      process              Procfile Process Name
    
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
    Spawning web: gunicorn project.wsgi:application --log-file log/gunicorn.$LOGFILE --bind unix:run/gunicorn.sock

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

This used by [Panubo](https://panubo.io/) to support Python environments.
