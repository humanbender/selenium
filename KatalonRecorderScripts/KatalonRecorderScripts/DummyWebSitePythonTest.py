# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class WebSiteTest(unittest.TestCase):   
    browserType = 0 
    def setUp(self):         
        if(self.browserType == "1") :            
            dc = webdriver.DesiredCapabilities.INTERNETEXPLORER
            dc["requireWindowFocus"] = True
            dc["javascriptEnabled"] = True
            self.driver = webdriver.Ie(executable_path=r'C:/Users/bartu.yaman/Desktop/Drivers/IEDriverServer.exe', capabilities = dc)   
        elif(self.browserType == "2"):
            self.driver = webdriver.Chrome(executable_path=r'C:/Users/bartu.yaman/Desktop/Drivers/chromedriver.exe')   
        elif(self.browserType == "3"):
            self.driver=webdriver.Firefox(executable_path=r'C:/Users/bartu.yaman/Desktop/Drivers/geckodriver.exe')
        elif (self.browserType == "4"):
            self.driver=webdriver.Safari()
        
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_dummy_web_site_java(self):
        try:
            driver = self.driver
            driver.get("https://jv96elgwlg.execute-api.us-east-1.amazonaws.com/dev18/")
            driver.find_element_by_id("submitBtn").click()
            driver.find_element_by_link_text("Catalog").click()
            driver.find_element_by_link_text("My Orders").click()
            driver.find_element_by_link_text("Catalog").click()
            driver.find_element_by_id("OpenModal").click()
            driver.find_element_by_id("OpenModal").click()
            driver.find_element_by_link_text("Confirm").click()
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Thank You!'])[1]/following::span[1]").click()    
            #assert "Avocado & Crab Toast"  in driver.page_source            
        except NoSuchElementException as Exception:
            exit(1)
        except AssertionError as Exception:
            exit(2)
        
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
    WebSiteTest.browserType=sys.argv.pop()   
    unittest.main()
