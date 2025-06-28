from selenium.common import NoSuchElementException
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time

from undetected_chromedriver import ChromeOptions


class Page:
    #bogoItems = []

    def getBogoItems(self):
        driver = Page.setupDriver(self)
        time.sleep(1)

        # find element that states how many results are in BOGO deals
        resultElement = driver.find_element(By.XPATH,"/html/body/div[1]/section/div[4]/div[1]/div[3]/div/div[2]/div[1]/div/span[1]")

        # Get text of that element
        resultNum = resultElement.text

        # Get just number from that text
        resultNum = resultNum.split()
        num = resultNum[0]

        bogoItems = []
        index = 0

        #// *[ @ id = "bogo-10"]

        for index in range(int(num)):
            id = "bogo-" + str(index)

            xPath = "//*[@id=" + '"' + id + '"' + "]/div/div[2]/div[1]/div/button/span"
            #xPath = "// *[ @ id = " + '"' + id + '"' + "]"

            # Find next item
            currItem = driver.find_element(By.XPATH, xPath)

            # Scroll page to keep items loading
            driver.execute_script("arguments[0].scrollIntoView(true);", currItem)

            # Get text from element (Product name)
            text = currItem.text
            #print("Found item: " + text)

            # Add item to list
            bogoItems.append(text)

            #time.sleep(.05)

        return bogoItems

        # release driver
        driver.quit()

    def setupDriver(self):
        options = ChromeOptions()


        # Start webdriver
        driver = uc.Chrome(options=options)

        #driver.set_window_size(500,500)

        # Open web page
        driver.get("https://www.publix.com/savings/weekly-ad/bogo?merch=hp_viz_nav_bogo")

        return driver

    def getItems(self):
        return Page.bogoItems



