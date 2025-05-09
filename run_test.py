import unittest
import HtmlTestRunner
from tests.my_account_tests import MyAccountTest
from tests.order_page_tests import OrderPageTests
from tests.store_page_tests import StorePageTest
from tests.windsurfing_store_tests import WindsurfingStoreTest

"""
Download tests for running
"""
login_tests = unittest.TestLoader().loadTestsFromTestCase(MyAccountTest)
order_tests = unittest.TestLoader().loadTestsFromTestCase(OrderPageTests)
store_tests = unittest.TestLoader().loadTestsFromTestCase(StorePageTest)
windsurfing_tests = unittest.TestLoader().loadTestsFromTestCase(WindsurfingStoreTest)


"""
Test list for running
"""
tests_for_run = [
    login_tests,
    order_tests,
    store_tests,
    windsurfing_tests
]

"""
Create test suite 
"""
test_suite = unittest.TestSuite(tests_for_run)

"""
Run tests and generate report at the end
"""
if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(
        output='reports',           # File where report will be saved
        report_title='FakeStore Test Report',
        descriptions=True,
        combine_reports=True         # All tests in one file
    )
    runner.run(test_suite)
