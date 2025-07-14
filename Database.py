import sqlite3


class Database:
    con = sqlite3.connect("Database/BogoNotify.db")
    cur = con.cursor()

    def getCustomersItems(self, customerID):
        strList = []

        productResult = Database.cur.execute("SELECT * FROM desiredItems WHERE customerId = ?", (str(customerID),))
        products = productResult.fetchall()

        for product in products:
            productTitle = product[0]
            strList.append(productTitle)

        return strList

    def getCustomerInfo(self, customerID):
        Database.cur.execute("SELECT * FROM customers WHERE customerId = ?", (int(customerID),))
        result = Database.cur.fetchall()
        return result

    def addCustomer(self, name, carrier, phoneNum):
        customerCount = Database.getCustomerLength(self)
        customerID = customerCount + 1
        data = (customerID, name, carrier, phoneNum)
        Database.cur.execute(f"INSERT INTO customers VALUES (?, ?, ?, ?)", data)
        Database.con.commit()

    def addDesiredProduct(self, productName, customerID):
        data = (productName, customerID)
        Database.cur.execute(f"INSERT INTO desiredItems VALUES (?, ?)", data)
        Database.con.commit()

    def addBogoProducts(self, productList):
        for product in productList:
            print(product)
            Database.cur.execute(f"INSERT INTO bogoItems VALUES (?)", (str(product),))
            Database.con.commit()

    def getDesiredProductsLength(self):
        Database.cur.execute("SELECT COUNT(*) FROM desiredItems")
        count = Database.cur.fetchone()[0]
        return count

    def getProductsLength(self):
        Database.cur.execute("SELECT COUNT(*) FROM bogoItems")
        count = Database.cur.fetchone()[0]
        return count

    def getAllDesiredProducts(self):
        products = Database.cur.execute("SELECT * FROM desiredItems")
        return products.fetchall()

    def getAllProducts(self):
        strList = []

        productResult = Database.cur.execute("SELECT * FROM bogoItems")
        products = productResult.fetchall()

        for product in products:
            productTitle = product[0]
            strList.append(productTitle)

        return strList

    def getCustomerLength(self):
        Database.cur.execute("SELECT COUNT(*) FROM customers")
        count = Database.cur.fetchone()[0]
        return count

    def getAllCustomers(self):
        customers = Database.cur.execute("SELECT * FROM customers")
        return customers.fetchall()

    def getCustomerName(self, customerId):
        Database.cur.execute("SELECT name FROM customers WHERE customerId = ?", (int(customerId),) )
        result = Database.cur.fetchone()
        fullName = result[0]
        firstName = fullName.split(" ")[0]
        return str(firstName)

    def removeDesiredProduct(self, productName):
        print("Removing product:", productName, "from desiredItems table")
        Database.cur.execute("DELETE FROM desiredItems WHERE title = ?",(str(productName),))
        Database.con.commit()

    def removeCustomer(self, customerName):
        print("Removing customer:", customerName, "from customers table")
        Database.cur.execute("DELETE FROM customers WHERE name = ?", (str(customerName),))
        Database.con.commit()

    def clearCustomerTable(self):
        Database.cur.execute("DELETE from customers")
        Database.con.commit()

    def clearDesiredProductTable(self):
        Database.cur.execute("DELETE from desiredItems")
        Database.con.commit()

    def clearProductTable(self):
        Database.cur.execute("DELETE from bogoItems")
        Database.con.commit()