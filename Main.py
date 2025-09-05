from UI.MainWindow import Ui_MainWindow
import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtWidgets import QTableWidgetItem
from Display import MainWindow
from Database import Database
import requests
import json
from playwright.sync_api import sync_playwright
import re
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

def main():
    data = Database()

    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()


    sys.exit(app.exec())



if __name__ == "__main__":
    main()