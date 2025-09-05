# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(511, 880)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 511, 861))
        self.tabWidget.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 20, 511, 20))
        font = QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 80, 511, 20))
        font1 = QFont()
        font1.setPointSize(15)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setMargin(0)
        self.label_2.setIndent(110)
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 120, 511, 20))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setMargin(0)
        self.label_3.setIndent(110)
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 160, 511, 20))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setMargin(0)
        self.label_4.setIndent(110)
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 200, 511, 20))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setMargin(0)
        self.label_5.setIndent(110)
        self.CustomerFirstNameInputBox = QLineEdit(self.tab)
        self.CustomerFirstNameInputBox.setObjectName(u"CustomerFirstNameInputBox")
        self.CustomerFirstNameInputBox.setGeometry(QRect(270, 80, 161, 26))
        self.CustomerFirstNameInputBox.setStyleSheet(u"border-style: solid;\n"
"border-color: dimgrey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"")
        self.CustomerLastNameInputBox = QLineEdit(self.tab)
        self.CustomerLastNameInputBox.setObjectName(u"CustomerLastNameInputBox")
        self.CustomerLastNameInputBox.setGeometry(QRect(270, 120, 161, 26))
        self.CustomerLastNameInputBox.setStyleSheet(u"border-style: solid;\n"
"border-color: dimgrey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"")
        self.CustomerPhoneNumberInputBox = QLineEdit(self.tab)
        self.CustomerPhoneNumberInputBox.setObjectName(u"CustomerPhoneNumberInputBox")
        self.CustomerPhoneNumberInputBox.setGeometry(QRect(270, 200, 161, 26))
        self.CustomerPhoneNumberInputBox.setStyleSheet(u"border-style: solid;\n"
"border-color: dimgrey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"")
        self.CustomerCarrierComboBox = QComboBox(self.tab)
        self.CustomerCarrierComboBox.setObjectName(u"CustomerCarrierComboBox")
        self.CustomerCarrierComboBox.setGeometry(QRect(270, 160, 161, 26))
        self.CustomerCarrierComboBox.setStyleSheet(u"border-style: solid;\n"
"border-color: dimgrey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"")
        self.AddNewCustomerButton = QPushButton(self.tab)
        self.AddNewCustomerButton.setObjectName(u"AddNewCustomerButton")
        self.AddNewCustomerButton.setGeometry(QRect(280, 240, 141, 26))
        font2 = QFont()
        font2.setPointSize(13)
        self.AddNewCustomerButton.setFont(font2)
        self.AddNewCustomerButton.setStyleSheet(u"border-style: solid;\n"
"border-color: dimgrey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 300, 511, 20))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.CustomerTableView = QTableWidget(self.tab)
        if (self.CustomerTableView.columnCount() < 4):
            self.CustomerTableView.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.CustomerTableView.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.CustomerTableView.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.CustomerTableView.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.CustomerTableView.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.CustomerTableView.setObjectName(u"CustomerTableView")
        self.CustomerTableView.setGeometry(QRect(0, 330, 511, 461))
        self.CustomerTableView.setStyleSheet(u"")
        self.DeleteCustomerButton = QPushButton(self.tab)
        self.DeleteCustomerButton.setObjectName(u"DeleteCustomerButton")
        self.DeleteCustomerButton.setGeometry(QRect(170, 800, 171, 26))
        self.DeleteCustomerButton.setFont(font2)
        self.DeleteCustomerButton.setStyleSheet(u"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 dimgrey, stop: 1 dimgrey);\n"
"border-style: solid;\n"
"border-color: dimgrey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 170, 511, 20))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.DesiredProductTableView = QTableWidget(self.tab_2)
        if (self.DesiredProductTableView.columnCount() < 2):
            self.DesiredProductTableView.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.DesiredProductTableView.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.DesiredProductTableView.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.DesiredProductTableView.setObjectName(u"DesiredProductTableView")
        self.DesiredProductTableView.setGeometry(QRect(0, 200, 511, 591))
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 20, 511, 20))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.AddDesiredProductCustomerIDComboBox = QComboBox(self.tab_2)
        self.AddDesiredProductCustomerIDComboBox.setObjectName(u"AddDesiredProductCustomerIDComboBox")
        self.AddDesiredProductCustomerIDComboBox.setGeometry(QRect(160, 110, 111, 26))
        self.AddDesiredProductCustomerIDComboBox.setStyleSheet(u"border-style: solid;\n"
"border-color: dimgrey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"")
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 70, 511, 20))
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_9.setMargin(0)
        self.label_9.setIndent(20)
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 110, 161, 20))
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_10.setMargin(0)
        self.label_10.setIndent(20)
        self.AddDesiredProductInputBox = QLineEdit(self.tab_2)
        self.AddDesiredProductInputBox.setObjectName(u"AddDesiredProductInputBox")
        self.AddDesiredProductInputBox.setGeometry(QRect(160, 70, 321, 26))
        self.AddDesiredProductInputBox.setStyleSheet(u"border-style: solid;\n"
"border-color: dimgrey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"")
        self.AddDesiredProductButton = QPushButton(self.tab_2)
        self.AddDesiredProductButton.setObjectName(u"AddDesiredProductButton")
        self.AddDesiredProductButton.setGeometry(QRect(340, 110, 141, 26))
        self.AddDesiredProductButton.setFont(font2)
        self.AddDesiredProductButton.setStyleSheet(u"border-style: solid;\n"
"border-color: dimgrey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"")
        self.DeleteDesiredProductButton = QPushButton(self.tab_2)
        self.DeleteDesiredProductButton.setObjectName(u"DeleteDesiredProductButton")
        self.DeleteDesiredProductButton.setGeometry(QRect(170, 800, 171, 26))
        self.DeleteDesiredProductButton.setFont(font2)
        self.DeleteDesiredProductButton.setStyleSheet(u"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 dimgrey, stop: 1 dimgrey);\n"
"border-style: solid;\n"
"border-color: dimgrey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.ProductTableView = QTableWidget(self.tab_3)
        if (self.ProductTableView.columnCount() < 1):
            self.ProductTableView.setColumnCount(1)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.ProductTableView.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        self.ProductTableView.setObjectName(u"ProductTableView")
        self.ProductTableView.setGeometry(QRect(0, 50, 511, 771))
        self.lineEdit = QLineEdit(self.tab_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 491, 26))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_11 = QLabel(self.tab_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 30, 511, 20))
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ClearDesiredProductsTableButton = QPushButton(self.tab_4)
        self.ClearDesiredProductsTableButton.setObjectName(u"ClearDesiredProductsTableButton")
        self.ClearDesiredProductsTableButton.setGeometry(QRect(140, 90, 241, 26))
        self.ClearDesiredProductsTableButton.setFont(font2)
        self.ClearDesiredProductsTableButton.setStyleSheet(u"border-style: solid;\n"
"border-color: dimgrey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"")
        self.ClearCustomerTableButton = QPushButton(self.tab_4)
        self.ClearCustomerTableButton.setObjectName(u"ClearCustomerTableButton")
        self.ClearCustomerTableButton.setGeometry(QRect(160, 140, 201, 26))
        self.ClearCustomerTableButton.setFont(font2)
        self.ClearCustomerTableButton.setStyleSheet(u"border-style: solid;\n"
"border-color: dimgrey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"")
        self.FindPublixBogoItemsButton = QPushButton(self.tab_4)
        self.FindPublixBogoItemsButton.setObjectName(u"FindPublixBogoItemsButton")
        self.FindPublixBogoItemsButton.setGeometry(QRect(160, 190, 201, 26))
        self.FindPublixBogoItemsButton.setFont(font2)
        self.FindPublixBogoItemsButton.setStyleSheet(u"border-style: solid;\n"
"border-color: dimgrey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"")
        self.FindCustomerItemsButton = QPushButton(self.tab_4)
        self.FindCustomerItemsButton.setObjectName(u"FindCustomerItemsButton")
        self.FindCustomerItemsButton.setGeometry(QRect(160, 290, 201, 26))
        self.FindCustomerItemsButton.setFont(font2)
        self.FindCustomerItemsButton.setStyleSheet(u"border-style: solid;\n"
"border-color: dimgrey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"")
        self.FindChewDealsButton = QPushButton(self.tab_4)
        self.FindChewDealsButton.setObjectName(u"FindChewDealsButton")
        self.FindChewDealsButton.setGeometry(QRect(160, 240, 201, 26))
        self.FindChewDealsButton.setFont(font2)
        self.FindChewDealsButton.setStyleSheet(u"border-style: solid;\n"
"border-color: dimgrey;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Customer Information", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Carrier", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.AddNewCustomerButton.setText(QCoreApplication.translate("MainWindow", u"Add Customer", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Customer Information", None))
        ___qtablewidgetitem = self.CustomerTableView.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.CustomerTableView.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.CustomerTableView.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Carrier", None));
        ___qtablewidgetitem3 = self.CustomerTableView.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Phone #", None));
        self.DeleteCustomerButton.setText(QCoreApplication.translate("MainWindow", u"Delete Customer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Add Customer", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Product List", None))
        ___qtablewidgetitem4 = self.DesiredProductTableView.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Product Name", None));
        ___qtablewidgetitem5 = self.DesiredProductTableView.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Customer ID", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Desired Products", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Customer ID", None))
        self.AddDesiredProductButton.setText(QCoreApplication.translate("MainWindow", u"Add Product", None))
        self.DeleteDesiredProductButton.setText(QCoreApplication.translate("MainWindow", u"Delete Product", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Desired Products", None))
        ___qtablewidgetitem6 = self.ProductTableView.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Product Name", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"All Products", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"App Controls", None))
        self.ClearDesiredProductsTableButton.setText(QCoreApplication.translate("MainWindow", u"Clear Desired Products Table", None))
        self.ClearCustomerTableButton.setText(QCoreApplication.translate("MainWindow", u"Clear Customer Table", None))
        self.FindPublixBogoItemsButton.setText(QCoreApplication.translate("MainWindow", u"Find Publix BOGO Items", None))
        self.FindCustomerItemsButton.setText(QCoreApplication.translate("MainWindow", u"Find Customer Items", None))
        self.FindChewDealsButton.setText(QCoreApplication.translate("MainWindow", u"Find Chewy Deals", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Controls", None))
    # retranslateUi

