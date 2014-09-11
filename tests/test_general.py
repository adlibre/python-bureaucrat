import unittest
import os

import .bureaucrat


TESTS_PATH = os.path.abspath(os.path.split(__file__)[0])


class BureaucratTest(unittest.TestCase):

    def test_initialisation(self):

        process_file = os.path.join(TESTS_PATH, 'data', 'Procfile')
        env_file = os.path.join(TESTS_PATH, 'data', 'env')
        virtual_env = '/tmp'
        app_path = '/tmp'
        log_path = '/tmp'
        pid_path = '/tmp'
        named_procs = None
        b = bureaucrat.Bureaucrat(process_file,
                                  env_file,
                                  virtual_env,
                                  app_path,
                                  log_path,
                                  pid_path,
                                  named_procs,
                                  debug=True)
        b.start()