from UI.MainWindow import Ui_MainWindow
import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtWidgets import QTableWidgetItem
from Display import MainWindow
from Database import Database

def main():
    requestedItems = ("Post Great Grains Cereal!")

    data = Database()

    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()







    sys.exit(app.exec())




    #page = Page()

    #bogoItems = page.getBogoItems()

    #for item in bogoItems:
    #    if requestedItems == item:
    #        print(item)



if __name__ == "__main__":
    main()