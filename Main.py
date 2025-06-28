from PageInteractions import Page
import time
import smtplib
import sys


def main():
    requestedItems = "Cereal"

    page = Page()

    bogoItems = page.getBogoItems()

    for item in bogoItems:
        if requestedItems[0] in item:
            print(item)





if __name__ == "__main__":
    main()