import doctest
import unittest

from importlib import import_module


if __name__ == '__main__':
    for module in ['json_to_csv_convertor_solved', 'reports_solved']:
        mod_loaded = import_module(module, 'homework_5')
        test_suite = doctest.DocTestSuite(mod_loaded)
        unittest.TextTestRunner().run(test_suite)
