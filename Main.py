from PageInteractions import Page
from Database import Database
from Display import Display
import time
import smtplib
import sys


def main():
    requestedItems = ("Post Great Grains Cereal")

    data = Database()
    display = Display()
    display.initDisplay()

    num = data.getCustomerLength()
    print(num)





    #page = Page()

    #bogoItems = page.getBogoItems()

    #for item in bogoItems:
    #    if requestedItems == item:
    #        print(item)



if __name__ == "__main__":
    main()