import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QMainWindow
from UI.MainWindow import Ui_MainWindow
from Database import Database
from PageInteractions import Page
from Customers import Customer


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.populateCarrierComboBox()
        self.populateCustomerIDComboBox()
        self.populateCustomerTable()
        self.populateProductTable()

        self.AddNewCustomerButton.clicked.connect(self.onAddCustomerClicked)
        self.AddDesiredProductButton.clicked.connect(self.onAddDesiredProductClicked)
        self.ClearDesiredProductsTableButton.clicked.connect(self.onClearDesiredProductTableClicked)
        self.ClearCustomerTableButton.clicked.connect(self.onClearCustomerTableClicked)
        self.FindBogoItemsButton.clicked.connect(self.onFindBOGOItemsClicked)

    @qtc.Slot()
    def onFindBOGOItemsClicked(self):
        customer = Customer()

        customer.findCustomerItems()

    @qtc.Slot()
    def onClearCustomerTableClicked(self):
        dataBase = Database()
        dataBase.clearCustomerTable()
        self.populateCustomerTable()

    @qtc.Slot()
    def onClearDesiredProductTableClicked(self):
        dataBase = Database()
        dataBase.clearDesiredProductTable()
        self.populateProductTable()

    @qtc.Slot()
    def onAddDesiredProductClicked(self):
        product = self.AddDesiredProductInputBox.text()
        customerID = self.AddDesiredProductCustomerIDComboBox.currentText()

        if product != "":
            dataBase = Database()
            dataBase.addDesiredProduct(product, customerID)

            # Clear all input boxes
            self.AddDesiredProductInputBox.clear()

            # Repopulate table with new value
            self.populateProductTable()

    @qtc.Slot()
    def onAddCustomerClicked(self):
        firstName = self.CustomerFirstNameInputBox.text()
        lastName = self.CustomerLastNameInputBox.text()
        carrier = self.CustomerCarrierComboBox.currentText()
        phoneNumber = self.CustomerPhoneNumberInputBox.text()

        name = firstName + " " + lastName

        if name != "" and phoneNumber != "":
            dataBase = Database()
            dataBase.addCustomer(name, carrier, phoneNumber)

            # Clear all input boxes
            self.CustomerFirstNameInputBox.clear()
            self.CustomerLastNameInputBox.clear()
            self.CustomerPhoneNumberInputBox.clear()

            # Repopulate table with new value
            self.populateCustomerTable()

    def populateCustomerTable(self):
        self.CustomerTableView.setColumnWidth(0, 30)
        self.CustomerTableView.setColumnWidth(1, 130)
        self.CustomerTableView.setColumnWidth(3, 120)

        dataBase = Database()

        dbTableLength = dataBase.getCustomerLength()
        qtTableLength = self.CustomerTableView.rowCount()

        if dbTableLength != 0 and qtTableLength != dbTableLength:
            self.CustomerTableView.clearContents()
            self.CustomerTableView.setRowCount(0)

            self.populateCustomerIDComboBox()

            customers = dataBase.getAllCustomers()

            for customer in customers:
                rowPos = self.CustomerTableView.rowCount()
                self.CustomerTableView.insertRow(rowPos)

                customerID = str(customer[0])
                name = customer[1]
                carrier = customer[2]
                phoneNum = customer[3]

                self.CustomerTableView.setItem(rowPos, 0, QTableWidgetItem(customerID))
                self.CustomerTableView.setItem(rowPos, 1, QTableWidgetItem(name))
                self.CustomerTableView.setItem(rowPos, 2, QTableWidgetItem(carrier))
                self.CustomerTableView.setItem(rowPos, 3, QTableWidgetItem(phoneNum))

                self.CustomerTableView.show()


    def populateProductTable(self):
        self.DesiredProductTableView.setColumnWidth(0, 400)
        self.DesiredProductTableView.setColumnWidth(1, 90)

        dataBase = Database()

        dbTableLength = dataBase.getProductsLength()
        qtTableLength = self.DesiredProductTableView.rowCount()

        if dbTableLength != 0 and qtTableLength != dbTableLength:
            self.DesiredProductTableView.clearContents()
            self.DesiredProductTableView.setRowCount(0)

            products = dataBase.getAllProducts()

            for product in products:
                rowPos = self.DesiredProductTableView.rowCount()
                self.DesiredProductTableView.insertRow(rowPos)

                productName = product[0]
                customerID = product[1]
                customerName = dataBase.getCustomerName(customerID)


                self.DesiredProductTableView.setItem(rowPos, 0, QTableWidgetItem(productName))
                self.DesiredProductTableView.setItem(rowPos, 1, QTableWidgetItem(customerName))

                self.DesiredProductTableView.show()

    def populateCarrierComboBox(self):
        carriers = {"Verizon", "T-Mobile", "AT&T"}

        # Adds all carriers to combo box
        for carrier in carriers:
            self.CustomerCarrierComboBox.addItem(carrier)

    def populateCustomerIDComboBox(self):
        self.AddDesiredProductCustomerIDComboBox.clear()

        dataBase = Database()
        customerCount = dataBase.getCustomerLength()
        customerIdList = []

        for num in range(1, customerCount + 1):
            customerIdList.append(num)

        print(customerIdList)



        if customerCount == 1:
            self.AddDesiredProductCustomerIDComboBox.addItem(str(1))

        else:
            # Adds all customer IDs to combobox
            for num in customerIdList:
                self.AddDesiredProductCustomerIDComboBox.addItem(str(num))


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())