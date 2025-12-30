"""Day 22: Selenium Web Automation
Automating browser interactions and web testing.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class SeleniumAutomation:
    def __init__(self, headless=False):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
    
    def get(self, url):
        self.driver.get(url)
    
    def find_element(self, by, value):
        return self.driver.find_element(by, value)
    
    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    
    def click_element(self, by, value):
        element = self.wait_for_element(by, value)
        element.click()
    
    def send_keys(self, by, value, text):
        element = self.wait_for_element(by, value)
        element.send_keys(text)
    
    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
    
    def close(self):
        self.driver.quit()

# Example usage
if __name__ == "__main__":
    automation = SeleniumAutomation(headless=True)
    automation.get("https://example.com")
    automation.take_screenshot("example.png")
    automation.close()
