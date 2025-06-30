from PageInteractions import Page
import time
import smtplib
import sys


def main():
    requestedItems = ("Post Great Grains Cereal")

    page = Page()

    bogoItems = page.getBogoItems()

    #for item in bogoItems:
    #    if requestedItems == item:
    #        print(item)





if __name__ == "__main__":
    main()