import sqlite3


class Database:
    con = sqlite3.connect("BogoNotify.db")
    cur = con.cursor()


    def insertCustomer(self, name, carrier, phoneNum):
        # foo
        print("done")

    def getCustomerLength(self):

        return Database.cur.execute("SELECT Count(*) FROM customers")