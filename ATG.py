import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class TestWebsiteLoading(unittest.TestCase):

    def test_website_loading(self):
        # Instantiate the webdriver
        driver = webdriver.Chrome()

        try:
            # Load the webpage
            driver.maximize_window()
        # defining condition for implicit waits - we have set 10 seconds
            driver.implicitly_wait(10)
            driver.get("https://atg.world")

            pageTitel = driver.title
            print("Page Title :"+pageTitel)

          

        except StaleElementReferenceException:
            # Handle StaleElementReferenceException
            print("Element is no longer attached to the DOM.")

        finally:
            # Switch back to the default content
            driver.switch_to.default_content()

            # Quit the webdriver
            #driver.quit()

if __name__ == "__main__":
    unittest.main()
