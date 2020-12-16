import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def test_CT(self):
        user = "zacht"
        pwd = "gomavs"
        cit = "Bellevue"
        zipC = "68005"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        driver.get("http://127.0.0.1:8000/client_list")
        time.sleep(3)
        driver.get("http://127.0.0.1:8000/client/1/edit/")
        time.sleep(3)
        elem = driver.find_element_by_id("id_city")
        elem.send_keys(cit)
        time.sleep(5)
        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys(zipC)
        time.sleep(5)
        elem.send_keys(Keys.RETURN)
        time.sleep(8)


def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()
