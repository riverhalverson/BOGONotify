from PageInteractions import Page
from Database import Database
from Mail import SMS
import asyncio

class Customer:

    def findCustomerItems(self):
        dataBase = Database()
        customerNum = dataBase.getCustomerLength()
        matchesFound = ""


        print(customerNum, "customers found, looking for their items")

        if customerNum > 0:
            allProducts = dataBase.getAllProducts()

            if customerNum == 1:

                desiredProducts = dataBase.getCustomersItems(1)

                for item in desiredProducts:
                    print("Looking in BOGO items for a match for:", item)
                    if item in allProducts:
                        matchesFound += str(item) + "\n"

                if len(matchesFound) > 0:
                    message = "The following items from your list were found on BOGO! " + "\n" + matchesFound
                    print(message)

                    customerInfo = dataBase.getCustomerInfo(0)
                    customerPhoneNum = customerInfo[3]
                    customerCarrier = customerInfo[2]

                    sms = SMS()
                    sms.sendNotification(customerPhoneNum,customerCarrier, message)

                    customerInfo = dataBase.getCustomerInfo(1)
                    print("Customer Info:", customerInfo)

            else:
                for customer in range(1, customerNum + 1):
                    message = ""
                    matchesFound = ""
                    customerInfo = dataBase.getCustomerInfo(customer)
                    customerId = customerInfo[0][0]
                    print("Customer ID:", customerId, " desired item search starting")

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
                        sms.sendNotification(6085093061, "Verizon", message)

                        print("Customer Info:", customerInfo, "\n\n")

 #   def notifyCustomer(self, allProductList, desiredProductList):