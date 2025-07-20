from playwright.sync_api import sync_playwright
import time
from Database import Database


class Page:

    def setupPage(self, session):
        # Open up a new browser session in headless mode and slow it down to let it load properly
        browser = session.chromium.launch(headless=False,
                                    slow_mo=30)

        # Give browser geolocation for store locater function
        # This gets a warning for incorrect type in PyCharm, the following ignores it
        # noinspection PyTypeChecker
        context = browser.new_context(geolocation={"latitude": 28.3164, "longitude": -80.7270},
                                      permissions=["geolocation"],
                                      locale="en-US")

        return context, browser

    # Takes an xpath or css selector and a page and scrolls to that point manually
    # Used when items cannot be located unless visible
    def scrollIntoView(self, path, page):
        # Scroll to item
        found = False
        maxScrolls = 20

        for _ in range(maxScrolls):
            try:
                element = page.query_selector(path)
                if element:
                    element.scroll_into_view_if_needed()
                    found = True
                    break
            except:
                pass

            page.mouse.wheel(0, 1000)
            time.sleep(1)

    def scrollToEnd(self, page):
        # Item at end of page (copyright notice)
        EOP = "/ html / body / div[1] / footer / div / div[3] / div"

        Page.scrollIntoView(self, EOP, page)

    def getChewyItems(self):
        itemList = []

        with sync_playwright() as session:

            context, browser = Page.setupPage(self, session)

            # Opens up a new page with the geolocation parameters
            page = context.new_page()

            # Cat wet food deals
            page.goto("https://www.chewy.com/")

            # Page seems to have an issue loading elements without a refresh after adding the location settings
            time.sleep(3)
            page.reload()
            time.sleep(3)

            # Get total BOGO results found
            Page.getChewyTotalResult(self, page)


            '''
            # Get first page items
            #Page.getPublixBogoItemTitles(self, page, itemList)

            # Get how many pages we'll have to go through
            totalPages = page.locator("button.toggle-button:nth-child(8) > span:nth-child(1)").text_content().strip()
            print("Pages: " + totalPages)

            pageNum = 1

            for pageNum in range(int(totalPages) - 1):
                page.locator("span.caretRight:nth-child(1)").click()
                Page.getPublixBogoItemTitles(self, page, itemList)
                print("Total items found:" + str(len(itemList)))

            time.sleep(10)
            '''
            browser.close()


        return itemList

    def getPublixBogoItems(self):
        itemList = []

        with sync_playwright() as session:
            context, browser = Page.setupPage(self, session)

            # Opens up a new page with the geolocation parameters
            page = context.new_page()
            page.goto("https://www.publix.com/d/all-categories?facet=facetBOGO%3A%3Atrue")

            # Page seems to have an issue loading elements without a refresh after adding the location settings
            time.sleep(.4)
            page.reload()

            # Get total BOGO results found
            Page.getPublixBogoTotalResult(self, page)

            # Get first page items
            Page.getPublixBogoItemTitles(self, page, itemList)

            # Get how many pages we'll have to go through
            totalPages = page.locator("button.toggle-button:nth-child(8) > span:nth-child(1)").text_content().strip()
            print("Pages: " + totalPages)

            pageNum = 1

            for pageNum in range(int(totalPages) - 1):
                page.locator("span.caretRight:nth-child(1)").click()
                Page.getPublixBogoItemTitles(self, page, itemList)
                print("Total items found:" + str(len(itemList)))

            time.sleep(10)
            browser.close()

        return itemList

    def getPublixBogoItemTitles(self, page, itemList):
        Page.scrollToEnd(self, page)
        dataBase = Database()

        className = ".p-grid-item"

        items = page.query_selector_all(className)

        for item in items:
            text = item.text_content().strip()
            title = text.split('\n', 1)[0]

            # Add title to list
            itemList.append(title)
            print("Item found: " + title)


        return itemList

    def getPublixBogoTotalResult(self, page):
        # Get total results we will be getting
        results = str(page.get_by_text("product results").all_inner_texts())
        resultsSplit = results.split(" ")
        resultsNum = resultsSplit[0][2:]
        print(resultsNum, "BOGO results found")

    def getChewyTotalResult(self, page):
        # Get total results we will be getting
        results = str(page.locator(".ProductListingGrid_resultsCountHideSm__u0Zp_").all_inner_texts())
        #resultsSplit = results.split(" ")
        #resultsNum = resultsSplit[0][2:]
        print(results, "Chewy results found")
