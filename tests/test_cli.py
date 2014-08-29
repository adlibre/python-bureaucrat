from subprocess import call
import os

BIN = os.path.abspath(os.path.join(os.path.split(__file__)[0], '..', 'bureaucrat'))


def test_no_args():
    exit_code = call([BIN])
    assert exit_code == 0


def test_help():
    exit_code = call([BIN, '-h'])
    assert exit_code == 0


def test_sub_help():
    for action in ('start', 'stop', 'restart', 'deploy', 'init'):
        exit_code = call([BIN, action, '-h'])
        assert exit_code == 0