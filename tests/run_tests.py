import unittest
from unittest import TestSuite
import HtmlTestRunner


def load_tests(loader, tests, pattern):
    ''' Discover and load all unit tests in all files named ``*_test.py`` in ``./src/``
    '''
    suite = TestSuite()
    for all_test_suite in unittest.defaultTestLoader.discover('tests', pattern='test_*'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    return suite


if __name__ == '__main__':
    print("This is main")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./report', combine_reports=True,report_title="cnvrg-operator test report"))
