from playwright.sync_api import sync_playwright
import time



class Page:
    #bogoItems = []

    def getBogoItems(self):
        with sync_playwright() as p:

            # Open up a new browser session in headless mode and slow it down to let it load properly
            browser = p.chromium.launch(headless=False,
                                        slow_mo=30)

            # Give browser geolocation for store locater function
            # This gets a warning for incorrect type in PyCharm, the following ignores it
            # noinspection PyTypeChecker
            context = browser.new_context(geolocation={"latitude": 28.3164, "longitude": -80.7270},
                                          permissions=["geolocation"],
                                          locale="en-US")

            # Opens up a new page with the geolocation parameters
            page = context.new_page()
            page.goto("https://www.publix.com/d/all-categories?facet=facetBOGO%3A%3Atrue")

            # Page seems to have an issue loading elements without a refresh after adding the location settings
            time.sleep(.4)
            page.reload()

            # Get total results we will be getting
            results = str(page.get_by_text("product results").all_inner_texts())
            resultsSplit = results.split(" ")
            resultsNum = resultsSplit[0][2:]
            print(resultsNum, "BOGO results found")

            # Wait for the product grid to load
            #page.wait_for_selector("ul[data-testid='product-grid']")

            # Select all product items in the grid
            time.sleep(2)
            items = page.locator(".p-grid-item").nth(0)
            items.scroll_into_view_if_needed()
            text = items.all_text_contents()
            print(text)
            text = items.all()
            print(text)
            print(" ")



            time.sleep(10)
            browser.close()

#    def setupDriver(self):



#    def getItems(self):
