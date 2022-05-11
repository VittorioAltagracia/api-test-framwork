import time
import unittest

from selenium import webdriver
# importing 'By' allows us to define method
from selenium.webdriver.common.by import By


class TestMaserati(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_Maserati(self):
        self.driver.get('https://www.maserati.com/us/en?redirect=1#/')

        self.assertEqual(self.driver.current_url, "https://www.maserati.com/us/en?redirect=1#/")
        self.driver.fullscreen_window()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[@class='logo ']")
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "nextTrigger").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "nextTrigger").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "nextTrigger").click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,900);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//img[contains(@alt,'Front view of Blue Quattroporte')]").click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,1620);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//h2[contains(text(),'THE QUATTROPORTE COLLECTION')]")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,120);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[contains(text(),'Current Offers')]").click()
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "zip-arrow").click()
        time.sleep(1.5)
        self.driver.find_element(By.TAG_NAME, "input").send_keys("78721")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'update')]").click()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
