from PageInteractions import Page
from Database import Database
from SMS import SMS
import asyncio

class Customer:

    def findCustomerItems(self):
        dataBase = Database()
        customerNum = dataBase.getCustomerLength()

        print(customerNum, "customers found, looking for their items")

        if customerNum > 0:
            allProducts = dataBase.getAllProducts()
            for product in allProducts:

            if customerNum == 1:
                matchesFound = ""

                desiredProducts = dataBase.getCustomersItems(1)

                for item in desiredProducts:
                    if item in allProducts:
                        matchesFound += str(item) + "\n"

                if len(matchesFound) > 0:
                    message = "The following items from your list were found on BOGO! " + "\n" + matchesFound
                    print(message)

                    sms = SMS()
                    sms.sendNotification(6085093061,"Verizon", message)

                    customerInfo = dataBase.getCustomerInfo(1)
                    print(customerInfo)

            else:
                for customer in range(1, customerNum + 1):
                    print("Customer ID:", customer, " desired item search starting")

                    matchesFound = ""
                    desiredProducts = dataBase.getCustomersItems(customer)

                    for item in desiredProducts:
                        print("Looking in BOGO items for a match for:", item)

                        for bogoItem in allProducts:
                            if item in bogoItem:
                                print("Item Found!:", item, "in bogo item:", bogoItem)
                                matchesFound += str(bogoItem) + "\n"


                    if len(matchesFound) > 0:
                        message = "The following items from your list were found on BOGO!: \n" + matchesFound
                        print(message)

                        sms = SMS()
                        #sms.sendNotification(6085093061, "Verizon", message)
                        sms.sendEmail(message)

                        customerInfo = dataBase.getCustomerInfo(customer)