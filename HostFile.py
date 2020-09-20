from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, \
    QListWidget, QSystemTrayIcon, QStyle, QAction, qApp, QMenu, QSpacerItem, QScrollArea, QCompleter, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui


class Ui_HostFileChange(QWidget):

    def __init__(self):
        super().__init__()
        self.setupui()

    def setupui(self):

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("logo.png"))
        self.tray_menu = QMenu()
        self.menu = self.tray_menu.addMenu("Hosts File")
        self.generate = self.tray_menu.addMenu("Generate")
        self.tray_menu.addAction(QAction("Exit", self))
        self.tray_icon.setContextMenu(self.tray_menu)

        HostFileChange.setObjectName("HostFileChange")
        HostFileChange.resize(433, 498)
        HostFileChange.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.centralwidget = QtWidgets.QWidget(HostFileChange)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 30, 191, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 410, 121, 31))
        self.pushButton.setStyleSheet("background-color: rgb(24, 186, 118);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 412, 111, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(24, 186, 118);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 330, 121, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(24, 186, 118);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 90, 191, 31))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 90, 121, 31))
        self.pushButton_4.setStyleSheet("background-color: rgb(24, 186, 118);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 101, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 101, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 140, 141, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(20, 150, 191, 231))
        self.treeView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.treeView.setObjectName("treeView")

        self.treeView_2 = QtWidgets.QTreeView(self.centralwidget)
        self.treeView_2.setGeometry(QtCore.QRect(260, 160, 121, 151))
        self.treeView_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.treeView_2.setObjectName("treeView_2")

        HostFileChange.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HostFileChange)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 433, 20))
        self.menubar.setObjectName("menubar")

        HostFileChange.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HostFileChange)
        self.statusbar.setObjectName("statusbar")

        HostFileChange.setStatusBar(self.statusbar)
        self.retranslateUi(HostFileChange)
        QtCore.QMetaObject.connectSlotsByName(HostFileChange)
        self.tray_icon.show()

    def update_display(self, text):

        for widget in self.widgets:
            if text.lower() in widget.name.lower():
                widget.show()
            else:
                widget.hide()

    def retranslateUi(self, HostFileChange):
        _translate = QtCore.QCoreApplication.translate
        HostFileChange.setWindowTitle(_translate("HostFileChange", "MainWindow"))
        self.pushButton.setText(_translate("HostFileChange", "Change IP"))
        self.pushButton_2.setText(_translate("HostFileChange", "Clear the Host File"))
        self.pushButton_3.setText(_translate("HostFileChange", "Generate Partner"))
        self.pushButton_4.setText(_translate("HostFileChange", "Search Partner"))
        self.label.setText(_translate("HostFileChange", "Enter Machine IP:"))
        self.label_2.setText(_translate("HostFileChange", "Enter Partner Name:"))
        self.label_3.setText(_translate("HostFileChange", "Partners that will be changed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HostFileChange = QtWidgets.QMainWindow()
    ui = Ui_HostFileChange()
    ui.setupui()
    HostFileChange.show()
    sys.exit(app.exec_())
