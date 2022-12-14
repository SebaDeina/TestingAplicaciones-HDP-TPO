# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCarritoDeCompra():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_carritoDeCompra(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1920, 1055)
    self.driver.find_element(By.LINK_TEXT, "Sign In").click()
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("sample@example.com")
    self.driver.find_element(By.NAME, "password").send_keys("sample")
    self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    element = self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(2) td:nth-child(4) #itemImage")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(2) td:nth-child(7) #itemImage").click()
    self.driver.find_element(By.LINK_TEXT, "Add to Cart").click()
    self.driver.find_element(By.ID, "cartIcon").click()
  
