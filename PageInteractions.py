from selenium.common import NoSuchElementException
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time

from undetected_chromedriver import ChromeOptions


class Page:
    #bogoItems = []

    def getBogoItems(self):
        driver = Page.setupDriver(self)
        time.sleep(10)
        driver.quit()
        #wait = WebDriverWait(driver, 10)



        #wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@role='alert']"), "product results"))
        #totalResults = driver.find_element(By.XPATH, "//span[@role='alert']")
        #print(totalResults.text)

        #totalResults = driver.find_element(By.CLASS_NAME, "fullWidth productCardHeaderControls")
        #totalResults.text()
        #print(totalResults)


        bogoItems = []
        index = 0

        '''
        for index in range(47):
            # Create indexed id for all elements on current page
            id = "[data-id=" + "'" + str(index) + "'" + "]"


            # Find next item
            currItem = driver.find_element(By.CSS_SELECTOR, id)

            # Scroll page to keep items loading
            driver.execute_script("arguments[0].scrollIntoView(true);", currItem)

            # Get text from element (Product name)
            #text = currItem.text
            #print("Found item: " + text)

            # Add item to list
            #bogoItems.append(text)

            #time.sleep(.05)

        return bogoItems
        '''

        # release driver
        driver.quit()

    def setupDriver(self):
        options = uc.ChromeOptions()
        prefs = {"profile.default_content_setting_values.geolocation": 1}
        options.add_experimental_option("prefs", prefs)

        # Start webdriver
        driver = uc.Chrome(options=options)

        # Open web page
        driver.get("https://www.publix.com/d/all-categories")

        #options = Options()
        #options.add_argument("--disable-blink-features=AutomationControlled")
        #options.add_argument(
            #"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
        #options.add_argument("--incognito")

        #prefs = {"profile.default_content_setting_values.geolocation": 1}
        #options.add_experimental_option("prefs", prefs)

        #driver = webdriver.Chrome(options=options)
        #driver.get("https://www.publix.com/d/all-categories")

        return driver






    def getItems(self):
        return Page.bogoItems



