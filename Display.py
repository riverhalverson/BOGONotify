import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtWidgets import QTableWidgetItem

from UI.MainWindow import Ui_MainWindow
from Database import Database
from PageInteractions import Page
from Customers import Customer


class MainWindow(qtw.QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.populateCarrierComboBox()
        self.populateCustomerIDComboBox()
        self.populateCustomerTable()
        self.populateProductTable()

        self.AddCustomerButton.clicked.connect(self.onAddCustomerClicked)
        self.AddProductButton.clicked.connect(self.onAddProductClicked)
        self.ClearProductTableButton.clicked.connect(self.onClearProductTableClicked)
        self.ClearCustomerTableButton.clicked.connect(self.onClearCustomerTableClicked)
        self.FindItemsButton.clicked.connect(self.onFindBOGOItemsClicked)

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
    def onClearProductTableClicked(self):
        dataBase = Database()
        dataBase.clearProductTable()
        self.populateProductTable()

    @qtc.Slot()
    def onAddProductClicked(self):
        product = self.ProductNameInputBox.text()
        customerID = self.ProductCustomerIDComboBox.currentText()

        print(product, customerID)

        # Clear selections
        self.ProductNameInputBox.text()
        self.ProductCustomerIDComboBox.clear()

    @qtc.Slot()
    def onAddProductClicked(self):
        product = self.ProductNameInputBox.text()
        customerID = self.ProductCustomerIDComboBox.currentText()

        if product != "":
            dataBase = Database()
            dataBase.addProduct(product, customerID)

            # Clear all input boxes
            self.ProductNameInputBox.clear()

            # Repopulate table with new value
            self.populateProductTable()

    @qtc.Slot()
    def onAddCustomerClicked(self):
        firstName = self.FirstNameInputBox.text()
        lastName = self.LastNameInputBox.text()
        carrier = self.CarrierComboBox.currentText()
        phoneNumber = self.PhoneNumberInputBox.text()

        name = firstName + " " + lastName

        if name != "" and phoneNumber != "":
            dataBase = Database()
            dataBase.addCustomer(name, carrier, phoneNumber)

            # Clear all input boxes
            self.FirstNameInputBox.clear()
            self.LastNameInputBox.clear()
            self.PhoneNumberInputBox.clear()

            # Repopulate table with new value
            self.populateCustomerTable()


    def populateCustomerTable(self):
        self.CustomerTable.setColumnWidth(0, 30)
        self.CustomerTable.setColumnWidth(1, 130)
        self.CustomerTable.setColumnWidth(3, 120)

        dataBase = Database()

        dbTableLength = dataBase.getCustomerLength()
        qtTableLength = self.CustomerTable.rowCount()

        if dbTableLength != 0 and qtTableLength != dbTableLength:
            self.CustomerTable.clearContents()
            self.CustomerTable.setRowCount(0)

            self.populateCustomerIDComboBox()

            customers = dataBase.getAllCustomers()

            for customer in customers:
                rowPos = self.CustomerTable.rowCount()
                self.CustomerTable.insertRow(rowPos)

                customerID = str(customer[0])
                name = customer[1]
                carrier = customer[2]
                phoneNum = customer[3]

                self.CustomerTable.setItem(rowPos, 0, QTableWidgetItem(customerID))
                self.CustomerTable.setItem(rowPos, 1, QTableWidgetItem(name))
                self.CustomerTable.setItem(rowPos, 2, QTableWidgetItem(carrier))
                self.CustomerTable.setItem(rowPos, 3, QTableWidgetItem(phoneNum))

                self.CustomerTable.show()


    def populateProductTable(self):
        self.ProductTable.setColumnWidth(0, 290)
        self.ProductTable.setColumnWidth(1, 90)

        dataBase = Database()

        dbTableLength = dataBase.getProductsLength()
        qtTableLength = self.ProductTable.rowCount()

        if dbTableLength != 0 and qtTableLength != dbTableLength:
            self.ProductTable.clearContents()
            self.ProductTable.setRowCount(0)

            products = dataBase.getAllProducts()

            for product in products:
                rowPos = self.ProductTable.rowCount()
                self.ProductTable.insertRow(rowPos)

                productName = product[0]
                customerID = product[1]

                self.ProductTable.setItem(rowPos, 0, QTableWidgetItem(productName))
                self.ProductTable.setItem(rowPos, 1, QTableWidgetItem(customerID))

                self.ProductTable.show()

    def populateCarrierComboBox(self):
        carriers = {"Verizon", "T-Mobile", "AT&T"}

        # Adds all carriers to combo box
        for carrier in carriers:
            self.CarrierComboBox.addItem(carrier)

    def populateCustomerIDComboBox(self):
        self.ProductCustomerIDComboBox.clear()

        dataBase = Database()
        customerCount = dataBase.getCustomerLength()

        if customerCount == 1:
            self.ProductCustomerIDComboBox.addItem(str(1))

        else:
            # Adds all carriers to combo box
            for num in range(1, customerCount - 1):
                self.ProductCustomerIDComboBox.addItem(str(num))


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())