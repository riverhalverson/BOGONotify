# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerZuPjWS.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 584)
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.tabWidget = QTabWidget(MainWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 461, 581))
        self.AddCustomer = QWidget()
        self.AddCustomer.setObjectName(u"AddCustomer")
        self.CarrierComboBox = QComboBox(self.AddCustomer)
        self.CarrierComboBox.setObjectName(u"CarrierComboBox")
        self.CarrierComboBox.setGeometry(QRect(230, 130, 141, 26))
        self.CarrierComboBox.setAutoFillBackground(False)
        self.PhoneNumberInputBox = QLineEdit(self.AddCustomer)
        self.PhoneNumberInputBox.setObjectName(u"PhoneNumberInputBox")
        self.PhoneNumberInputBox.setGeometry(QRect(230, 170, 142, 26))
        self.label = QLabel(self.AddCustomer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 10, 201, 18))
        font = QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.FirstNameInputBox = QLineEdit(self.AddCustomer)
        self.FirstNameInputBox.setObjectName(u"FirstNameInputBox")
        self.FirstNameInputBox.setGeometry(QRect(230, 50, 142, 26))
        self.LastNameInputBox = QLineEdit(self.AddCustomer)
        self.LastNameInputBox.setObjectName(u"LastNameInputBox")
        self.LastNameInputBox.setGeometry(QRect(230, 90, 142, 26))
        self.label_2 = QLabel(self.AddCustomer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 50, 101, 21))
        font1 = QFont()
        font1.setPointSize(13)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.AddCustomer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 90, 101, 21))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.AddCustomer)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 130, 101, 21))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.AddCustomer)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 170, 121, 21))
        self.label_5.setFont(font1)
        self.CustomerTable = QTableWidget(self.AddCustomer)
        if (self.CustomerTable.columnCount() < 4):
            self.CustomerTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.CustomerTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.CustomerTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.CustomerTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.CustomerTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.CustomerTable.setObjectName(u"CustomerTable")
        self.CustomerTable.setGeometry(QRect(30, 311, 401, 231))
        self.label_6 = QLabel(self.AddCustomer)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 280, 201, 18))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.AddCustomerButton = QPushButton(self.AddCustomer)
        self.AddCustomerButton.setObjectName(u"AddCustomerButton")
        self.AddCustomerButton.setGeometry(QRect(170, 220, 121, 26))
        self.tabWidget.addTab(self.AddCustomer, "")
        self.Products = QWidget()
        self.Products.setObjectName(u"Products")
        self.ProductTable = QTableWidget(self.Products)
        if (self.ProductTable.columnCount() < 2):
            self.ProductTable.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ProductTable.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ProductTable.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.ProductTable.setObjectName(u"ProductTable")
        self.ProductTable.setGeometry(QRect(30, 151, 401, 391))
        self.label_7 = QLabel(self.Products)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(130, 10, 201, 18))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.Products)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 50, 111, 21))
        self.label_8.setFont(font1)
        self.ProductNameInputBox = QLineEdit(self.Products)
        self.ProductNameInputBox.setObjectName(u"ProductNameInputBox")
        self.ProductNameInputBox.setGeometry(QRect(151, 50, 281, 26))
        self.ProductCustomerIDComboBox = QComboBox(self.Products)
        self.ProductCustomerIDComboBox.setObjectName(u"ProductCustomerIDComboBox")
        self.ProductCustomerIDComboBox.setGeometry(QRect(150, 90, 86, 26))
        self.label_9 = QLabel(self.Products)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 90, 111, 21))
        self.label_9.setFont(font1)
        self.AddProductButton = QPushButton(self.Products)
        self.AddProductButton.setObjectName(u"AddProductButton")
        self.AddProductButton.setGeometry(QRect(340, 90, 94, 26))
        self.tabWidget.addTab(self.Products, "")
        self.Controls = QWidget()
        self.Controls.setObjectName(u"Controls")
        self.ClearProductTableButton = QPushButton(self.Controls)
        self.ClearProductTableButton.setObjectName(u"ClearProductTableButton")
        self.ClearProductTableButton.setGeometry(QRect(150, 70, 171, 26))
        self.label_10 = QLabel(self.Controls)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(130, 20, 201, 18))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ClearCustomerTableButton = QPushButton(self.Controls)
        self.ClearCustomerTableButton.setObjectName(u"ClearCustomerTableButton")
        self.ClearCustomerTableButton.setGeometry(QRect(150, 120, 171, 26))
        self.FindItemsButton = QPushButton(self.Controls)
        self.FindItemsButton.setObjectName(u"FindItemsButton")
        self.FindItemsButton.setGeometry(QRect(150, 170, 171, 26))
        self.tabWidget.addTab(self.Controls, "")

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BOGO Notify", None))
        self.CarrierComboBox.setCurrentText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Customer Information", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Carrier", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        ___qtablewidgetitem = self.CustomerTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.CustomerTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.CustomerTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Carrier", None));
        ___qtablewidgetitem3 = self.CustomerTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Phone #", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Current Customers", None))
        self.AddCustomerButton.setText(QCoreApplication.translate("MainWindow", u"Add Customer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AddCustomer), QCoreApplication.translate("MainWindow", u"Add Customer", None))
        ___qtablewidgetitem4 = self.ProductTable.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Item Name", None));
        ___qtablewidgetitem5 = self.ProductTable.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Customer ID", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Add New Product", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Customer ID", None))
        self.AddProductButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Products), QCoreApplication.translate("MainWindow", u"Products", None))
        self.ClearProductTableButton.setText(QCoreApplication.translate("MainWindow", u"Clear Product Table", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"App Controls", None))
        self.ClearCustomerTableButton.setText(QCoreApplication.translate("MainWindow", u"Clear Customer Table", None))
        self.FindItemsButton.setText(QCoreApplication.translate("MainWindow", u"Find BOGO Items", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Controls), QCoreApplication.translate("MainWindow", u"Controls", None))
    # retranslateUi

