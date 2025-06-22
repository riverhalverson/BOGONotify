from Packages import *

class Page:
    url = "https://www.publix.com/savings/weekly-ad/bogo?merch=hp_viz_nav_bogo"

    driver = uc.Chrome()

    def expandPage(self):
        Page.driver.get(Page.url)

