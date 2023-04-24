import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from Base.Web_listener import WebDriverWrapper
from Uitilites import data_source


class TestLogin(WebDriverWrapper):

    def test_valid_login(self):
        self.driver.find_element(By.ID, "user_email").send_keys("princy@jain.com")
        self.driver.find_element(By.ID, "user_password").send_keys("padmakshi123")
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Sign In'])").click()
        actual_text = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Selenium']").text
        assert_that("Selenium").is_equal_to(actual_text)

    @pytest.mark.parametrize("usereamil,password,expected_error", data_source.test_invalid_login_data)
    def test_invalid_login(self, usereamil, password, expected_error):
        self.driver.find_element(By.ID, "user_email").send_keys(usereamil)
        self.driver.find_element(By.ID, "user_password").send_keys(password)
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Sign In'])").click()
        actual_error = self.driver.find_element(By.XPATH, "//p[@class='field__message']").text
        # print(actual_error)
        assert_that(expected_error).is_equal_to(actual_error)


class TestLoginUI(WebDriverWrapper):
    def test_title(self):
        actual_title = self.driver.title
        assert_that("Sign In | Selenium").is_equal_to(actual_title)

    def test_header(self):
        actual_header = self.driver.find_element(By.XPATH, "//span[normalize-space()='Selenium']").text
        assert_that("Selenium").is_equal_to(actual_header)

    def test_forgot_link(self):
        print("check hrf")

    def test_login_placeholder(self):
        actual_username_placeholder = self.driver.find_element(By.NAME, "user[email]").get_attribute("placeholder")
        assert_that("Email").is_equal_to(actual_username_placeholder)
        actual_password_placeholder = self.driver.find_element(By.NAME, "user[password]").get_attribute("placeholder")
        assert_that("Password").is_equal_to(actual_password_placeholder)
