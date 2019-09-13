# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re , sys

class UntitledTestCase(unittest.TestCase):
    browserType = 0 
    def setUp(self):         
        if(self.browserType == "1") :            
            dc = webdriver.DesiredCapabilities.INTERNETEXPLORER
            dc["requireWindowFocus"] = True
            dc["javascriptEnabled"] = True
            self.driver = webdriver.Ie(executable_path=r'C:/Users/bartu.yaman/Desktop/Drivers/IEDriverServer.exe', capabilities = dc)   
        elif(self.browserType == "2"):
            self.driver = webdriver.Chrome(executable_path=r'C:/Users/ege.okumus/Desktop/webDriver/chromedriver.exe')   
        elif(self.browserType == "3"):
            self.driver=webdriver.Firefox(executable_path=r'C:/Users/bartu.yaman/Desktop/Drivers/geckodriver.exe')
        elif (self.browserType == "4"):
            self.driver=webdriver.Safari()
        
        
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.phptravels.net/m-tours")
        driver.find_element_by_link_text("Hotels").click()
        driver.find_element_by_link_text("Flights").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Flights'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Privacy Policy'])[1]/following::img[1]").click()
    
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
    UntitledTestCase.browserType=sys.argv.pop()   

    unittest.main()
