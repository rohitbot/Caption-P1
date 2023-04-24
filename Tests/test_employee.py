import time
from lib2to3.pgen2 import driver

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Base.Web_listener import WebDriverWrapper
from Uitilites import data_source


class JavascriptExecutor:
    pass


class TestAddEmployee(WebDriverWrapper):

    @pytest.mark.parametrize('usereamil,password,upload_number,expected_error',
                             data_source.test_invalid_profile_upload_data)
    def test_invalid_profile_upload(self, usereamil, password, upload_number, expected_error):
        self.driver.find_element(By.ID, "user_email").send_keys(usereamil)
        self.driver.find_element(By.ID, "user_password").send_keys(password)
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Sign In'])").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Directory']").click()
        self.driver.find_element(By.XPATH,"//a[normalize-space()='employees']").click()
        self.driver.execute_script("window.scrollTo(0,1350)")
        #time.sleep(3)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "(//span[contains(text(),'Edit')])[1]").click()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Contact']").click()
        self.driver.find_element(By.ID, "phone").send_keys(upload_number)
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Save']").click()
        actual_error = self.driver.find_element(By.XPATH, "//span[@role='alert']").text
        assert_that(actual_error).contains(expected_error)

    @pytest.mark.parametrize(
        "usereamil, password,fullname,email, jobtitle", data_source.test_add_valid_employee_data)
    def test_add_valid_employee(self, usereamil, password, fullname, email, jobtitle):
        self.driver.find_element(By.ID, "user_email").send_keys(usereamil)
        self.driver.find_element(By.ID, "user_password").send_keys(password)
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Sign In'])").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Directory']").click()
        self.driver.execute_script("window.scrollTo(0,1300)")
        #time.sleep(3)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//main//div//div//div//div//span[contains(text(),'New')]").click()
        self.driver.find_element(By.ID, "name").send_keys(fullname)
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "job_title").send_keys(jobtitle)
        self.driver.find_element(By.XPATH, "(//button[@aria-label='open menu'])[2]").send_keys("Selenium HQ")
        #time.sleep(3)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,
                                 "//button[@data-testid='save-new-user']//span[contains(text(),'Save')]").click()
        self.driver.find_element(By.XPATH, "//button[@data-testid='modal__close']").click()

