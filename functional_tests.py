from selenium import webdriver
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_and_retrieve_a_list_laster(self):
        # Customer has heard about a cool new "to-do" web application
        # and goes to check it out
        self.browser.get('http://localhost:8000')

        # she notices "to-do" mentioned in the title header
        print('the current title is ' + self.browser.title)
        time.sleep(3)
        self.assertIn('To-Do',self.browser.title)
        #self.fail('finish the test')

        # she is invited to add a to-do item straight away
        #self.assertIn('Add a new To-do item?', self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')