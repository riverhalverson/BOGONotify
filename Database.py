import sqlite3


class Database:
    con = sqlite3.connect("Database/BogoNotify.db")
    cur = con.cursor()

    def getCustomersItems(self, customerID):
        Database.cur.execute("SELECT * FROM items WHERE customerId = ?", str(customerID))
        result = Database.cur.fetchall()
        return result

    def getCustomerInfo(self, customerID):
        Database.cur.execute("SELECT * FROM customers WHERE customerId = ?", str(customerID))
        result = Database.cur.fetchall()
        return result

    def addCustomer(self, name, carrier, phoneNum):
        customerCount = Database.getCustomerLength(self)
        customerID = customerCount + 1

        data = (customerID, name, carrier, phoneNum)

        Database.cur.execute(f"INSERT INTO customers VALUES (?, ?, ?, ?)", data)

        Database.con.commit()

    def addProduct(self, productName, customerID):

        data = (productName, customerID)

        Database.cur.execute(f"INSERT INTO items VALUES (?, ?)", data)

        Database.con.commit()

    def getProductsLength(self):
        Database.cur.execute("SELECT COUNT(*) FROM items")
        count = Database.cur.fetchone()[0]
        return count

    def getAllProducts(self):

        customers = Database.cur.execute("SELECT * FROM items")
        return customers.fetchall()

    def getCustomerLength(self):
        Database.cur.execute("SELECT COUNT(*) FROM customers")
        count = Database.cur.fetchone()[0]
        return count

    def getAllCustomers(self):

        customers = Database.cur.execute("SELECT * FROM customers")
        return customers.fetchall()

    def getAllProducts(self):

        products = Database.cur.execute("SELECT * FROM items")
        return products.fetchall()

    def clearCustomerTable(self):
        Database.cur.execute("DELETE from customers")
        Database.con.commit()

    def clearProductTable(self):
        Database.cur.execute("DELETE from items")
        Database.con.commit()
