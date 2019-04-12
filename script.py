import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/usr/bin/chromedriver')

    def test_in_python_org(self):
        driver = self.driver
        # for Authentication http://user:pass@test.web.page.com/
        driver.get("http://test.web.page.com/")
        self.assertIn("title", driver.title)
        username = driver.find_element_by_xpath("//input[@name='email']")
        username.send_keys("levchenko.amgrade@gmail.com")
        password = driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys("1")
        loginbutton = driver.find_element_by_xpath("//input[@type='submit']")
        loginbutton.click()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()