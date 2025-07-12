import sqlite3


class Database:
    con = sqlite3.connect("Database/BogoNotify.db")
    cur = con.cursor()

    def getCustomersItems(self, customerID):
        Database.cur.execute("SELECT * FROM items WHERE customerId = ?", (int(customerID),))
        result = Database.cur.fetchall()
        return result

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

    def addProduct(self, productName):
        data = productName
        Database.cur.execute(f"INSERT INTO bogoItems VALUES (?)", data)
        Database.con.commit()

    def getProductsLength(self):
        Database.cur.execute("SELECT COUNT(*) FROM desiredItems")
        count = Database.cur.fetchone()[0]
        return count

    def getAllProducts(self):
        customers = Database.cur.execute("SELECT * FROM desiredItems")
        return customers.fetchall()

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

    def clearCustomerTable(self):
        Database.cur.execute("DELETE from customers")
        Database.con.commit()

    def clearDesiredProductTable(self):
        Database.cur.execute("DELETE from desiredItems")
        Database.con.commit()
