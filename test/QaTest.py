# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, sys

class QaTest(unittest.TestCase):
    browserType=0
    def setUp(self):
        if(self.browserType=="1"):
            dc=webdriver.DesiredCapabilities.INTERNETEXPLORER
            dc["requireWindowFocus"]= True
            dc["javascriptEnabled"] =True
            self.driver =webdriver.Ie(executable_path=r'C:/Users/ege.okumus/Desktop/webDriver/IEDriverServer.exe',capabilities = dc )
        elif(self.browserType=="2"):
            self.driver=webdriver.Chrome(executable_path=r'C:/Users/ege.okumus/Desktop/webDriver/chromedriver.exe')
   
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_qa(self):
        try:
            driver = self.driver
            driver.get("https://qa.instantrewards.ihg.com/corporate/index.html#/corporate")
            
            driver.find_element_by_id("selectDepartmentCategory_9").click()
            Select(driver.find_element_by_id("selectDepartmentCategory_9")).select_by_visible_text("Parking")
            driver.find_element_by_id("selectDepartmentCategory_9").click()
            driver.find_element_by_id("inputDisplayNameLocal_9").click()
            driver.find_element_by_id("inputDisplayNameLocal_9").clear()
            driver.find_element_by_id("inputDisplayNameLocal_9").send_keys("efe")
            driver.find_element_by_id("inputDisplayName_9").click()
            driver.find_element_by_id("inputDisplayName_9").clear()
            driver.find_element_by_id("inputDisplayName_9").send_keys("efe")
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Account'])[1]/following::div[1]").click()
            driver.find_element_by_id("btnGlobalSave").click()
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[2]/following::button[1]").click()
            self.accept_next_alert = True
            driver.find_element_by_id("linkCorporateHotel").click()
            self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you would like to Navigate away from this page[\s\S] All changes will be lost$")
            driver.find_element_by_id("linkOutletsAndServices").click()
            driver.find_element_by_id()
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
    QaTest.browserType=sys.argv.pop()
    unittest.main()
