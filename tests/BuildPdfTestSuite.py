import os
import sys
import unittest

_path = os.path.realpath(os.path.abspath(__file__))
ROOT_PATH = os.path.dirname(os.path.dirname(_path))
sys.path.insert(0, ROOT_PATH)

from tests.test_build_pdf import BuildPdfTest
from tests.test_main import MainTest


buil_pdf_suite = unittest.TestLoader().loadTestsFromTestCase(BuildPdfTest)
main_suite = unittest.TestLoader().loadTestsFromTestCase(MainTest)

test_suites = unittest.TestSuite([main_suite, buil_pdf_suite])

unittest.TextTestRunner(verbosity=2).run(test_suites)
