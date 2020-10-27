import unittest
from unittest import TestSuite
import HtmlTestRunner
import logging
import argparse
import os, sys

logging.basicConfig(level=logging.DEBUG, format="|%(asctime)s|%(levelname)-5s %(message)s")


def load_tests(loader, tests, pattern):
    suite = TestSuite()
    test_pattern = os.getenv("TEST_DISCOVERY_PATTERN")
    for all_test_suite in unittest.defaultTestLoader.discover('tests', pattern=test_pattern):
        logging.info(all_test_suite)
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    return suite


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--test-discovery-pattern", help="test discover pattern", default="test_*")
    args = parser.parse_args()
    logging.info("start testing...")
    os.environ["TEST_DISCOVERY_PATTERN"] = args.test_discovery_pattern
    sys.argv = sys.argv[:1]
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./tests/reports',
                                                           combine_reports=True,
                                                           report_name="test-report",
                                                           report_title="cnvrg-operator test report"))
