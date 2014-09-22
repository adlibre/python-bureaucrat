import os

from .bureaucrat import Bureaucrat


TESTS_PATH = os.path.abspath(os.path.split(__file__)[0])


def test_start(capsys):
    # setup
    process_file = os.path.join(TESTS_PATH, 'data', 'Procfile')
    env_file = os.path.join(TESTS_PATH, 'data', 'env')
    virtual_env = '/tmp'
    app_path = '/tmp'
    log_path = '/tmp'
    pid_path = '/tmp'
    b = Bureaucrat(env_file,
                   virtual_env,
                   app_path,
                   log_path,
                   pid_path)
    b.load_procfile(process_file, named_procs=None)

    #
    # Start test
    #
    b.start()
    output, err = capsys.readouterr()
    expected_output = 'Spawning sleep0: sleep 0\n' \
                      'Spawning sleep5: sleep 5\n' \
                      'Spawning sleep10: sleep 10\n'
    assert output == expected_output

    # used for stop test
    expected_output = ''
    for p in b.process_manager.processes:
        expected_output += 'Spawned process ended: %s (pid: %s exit: 0)\n' % \
                           (p.name, p.sub_process.pid)

    #
    # Monitor test
    #
    b.monitor()

    #
    # stop test
    #
    capsys.close()
    b.stop()
    output, err = capsys.readouterr()
    expected_output += 'All spawned processes have ended.\n'
    assert output == expected_output
