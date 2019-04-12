import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging

class PythonTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/usr/bin/chromedriver')

    def test_in_web_page_com(self):
        driver = self.driver
        # for Authentication http://user:pass@test.web.page.com/
        driver.get("http://test.web.page.com/")
        self.assertIn("title", driver.title)
        username = driver.find_element_by_xpath("//input[@name='email']")
        username.send_keys("user@test.web.page.com")
        password = driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys("1")
        loginbutton = driver.find_element_by_xpath("//input[@type='submit']")
        loginbutton.click()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_search_by_text(self):
        # navigate to the application home page
        self.driver.get("http://www.google.com/")
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")

        # enter search keyword and submit
        self.search_field.send_keys("Selenium WebDriver Interview questions")
        self.search_field.submit()

        #get the list of elements which are displayed after the search
        #currently on result page usingfind_elements_by_class_namemethod

        lists = self.driver.find_elements_by_class_name("r")
        no=len(lists)
        self.assertEqual(10, len(lists))

    def tearDown(self):
        logging.basicConfig(filename = 'log_test.log', level = logging.DEBUG)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
