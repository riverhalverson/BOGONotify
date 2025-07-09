from PageInteractions import Page
from Database import Database
from SMS import SMS
import asyncio

class Customer:

    def findCustomerItems(self):
        dataBase = Database()
        page = Page()
        customerNum = dataBase.getCustomerLength()

        print("customer num:", customerNum)

        if customerNum > 0:
            results = page.getBogoItems()
            #results = ["Protein Cereal", "Kombucha"]
            print(results)

            if customerNum == 1:
                matchesFound = ""

                items = dataBase.getCustomersItems(1)

                print(items)

                for item in items:
                    itemName = item[0]
                    if itemName in results:
                        matchesFound += str(itemName) + "\n"

                if len(matchesFound) > 0:
                    message = "The following items from your list were found on BOGO! " + "\n" + matchesFound
                    print(message)

                    sms = SMS()

                    sms.sendNotification(6085093061,"Verizon", message)


                    customerInfo = dataBase.getCustomerInfo(1)
                    print(customerInfo)

            else:
                for customer in range(1, customerNum - 1):
                    matchesFound = ""

                    items = dataBase.getCustomersItems(customer)

                    print(items)

                    for item in items:
                        if item in results:
                            matchesFound += str(item) + ", "

                    if len(matchesFound) > 0:
                        message = "The following items from your list were found on BOGO!: " + matchesFound
                        print(message)

                        customerInfo = dataBase.getCustomerInfo(customer)