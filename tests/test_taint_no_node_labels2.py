import unittest
import HtmlTestRunner


class MyTestCase2(unittest.TestCase):
    def test_something(self):
        self.assertEqual2(True, False)


if __name__ == '__main__':
    print("This is main")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./report'))
