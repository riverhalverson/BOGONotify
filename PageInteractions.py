from selenium.common import NoSuchElementException
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time







class Page:

    def expandPage(self):
        driver = Page.setupDriver(self)
        time.sleep(5)

        pageEndFound = False

        while not pageEndFound:

            #find "Load more" button on the page
            try:
                loadMore = driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div/div[3]/div[2]/div[4]')
                text = loadMore.get_dom_attribute("text")
                print(text)

                try:
                    loadMore.click()
                    time.sleep(2)

                except WebDriverException:
                    pageEndFound = True

            except NoSuchElementException:
                pageEndFound = True



        #release driver
        driver.quit()

    def setupDriver(self):

        # Start webdriver
        driver = uc.Chrome()

        # Open web page
        driver.get("https://www.publix.com/savings/weekly-ad/bogo?merch=hp_viz_nav_bogo")

        return driver



