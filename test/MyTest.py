# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest, time, re, sys

class MyTest(unittest.TestCase):
    browserType=0
    def setUp(self):
        if(self.browserType=="1"):
            dc=webdriver.DesiredCapabilities.INTERNETEXPLORER
            dc["requireWindowFocus"]= True
            dc["javascriptEnabled"] =True
            self.driver =webdriver.Ie(executable_path=r'C:/Users/ege.okumus/Desktop/webDriver/IEDriverServer.exe',capabilities = dc )
        elif(self.browserType=="2"):
            self.driver=webdriver.Chrome(executable_path=r'C:/Users/ege.okumus/Desktop/webDriver/chromedriver.exe')
   
        self.driver.implicitly_wait(20)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_my(self):
        try:
            driver = self.driver
            driver.get("file:///C:/Users/ege.okumus/Desktop/build/index.html")
            time.sleep(10)
            driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
            driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
            driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
            driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
            driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
            driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
            driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
            driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
            driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
            driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
            driver.find_element_by_tag_name('body').send_keys('ENTER')
            


            #assert "Avocado & Crab Toast"  in driver.page_source 
        except NoSuchElementException as e:
            print(e)
        except AssertionError as er:
            print(er)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    MyTest.browserType=sys.argv.pop()

    unittest.main()
