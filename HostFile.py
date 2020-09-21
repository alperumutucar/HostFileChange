from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QSystemTrayIcon, QAction, QMenu
from PyQt5.QtGui import QIcon


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

        self.ipText = QtWidgets.QTextEdit(self.centralwidget)
        self.ipText.setGeometry(QtCore.QRect(20, 30, 191, 31))
        self.ipText.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ipText.setObjectName("ipText")

        self.ipButton = QtWidgets.QPushButton(self.centralwidget)
        self.ipButton.setGeometry(QtCore.QRect(260, 410, 121, 31))
        self.ipButton.setStyleSheet("background-color: rgb(24, 186, 118);")
        self.ipButton.setObjectName("ipButton")

        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(20, 412, 111, 31))
        self.clearButton.setStyleSheet("background-color: rgb(24, 186, 118);")
        self.clearButton.setObjectName("clearButton")

        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(260, 330, 121, 31))
        self.generateButton.setStyleSheet("background-color: rgb(24, 186, 118);")
        self.generateButton.setObjectName("generateButton")

        self.nameText = QtWidgets.QTextEdit(self.centralwidget)
        self.nameText.setGeometry(QtCore.QRect(20, 90, 191, 31))
        self.nameText.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nameText.setObjectName("nameText")

        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(260, 90, 121, 31))
        self.searchButton.setStyleSheet("background-color: rgb(24, 186, 118);")
        self.searchButton.setObjectName("searchButton")

        self.ipLabel = QtWidgets.QLabel(self.centralwidget)
        self.ipLabel.setGeometry(QtCore.QRect(20, 10, 101, 16))
        self.ipLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.ipLabel.setObjectName("ipLabel")

        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(20, 70, 101, 16))
        self.nameLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.nameLabel.setObjectName("nameLabel")

        self.changedLabel = QtWidgets.QLabel(self.centralwidget)
        self.changedLabel.setGeometry(QtCore.QRect(260, 140, 141, 16))
        self.changedLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.changedLabel.setObjectName("changedLabel")

        self.mainList = QtWidgets.QTreeView(self.centralwidget)
        self.mainList.setGeometry(QtCore.QRect(20, 150, 191, 231))
        self.mainList.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mainList.setObjectName("mainList")

        self.changeList = QtWidgets.QTreeView(self.centralwidget)
        self.changeList.setGeometry(QtCore.QRect(260, 160, 121, 151))
        self.changeList.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.changeList.setObjectName("changeList")

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
        self.ipButton.setText(_translate("HostFileChange", "Change IP"))
        self.clearButton.setText(_translate("HostFileChange", "Clear the Host File"))
        self.generateButton.setText(_translate("HostFileChange", "Generate Partner"))
        self.searchButton.setText(_translate("HostFileChange", "Search Partner"))
        self.ipLabel.setText(_translate("HostFileChange", "Enter Machine IP:"))
        self.nameLabel.setText(_translate("HostFileChange", "Enter Partner Name:"))
        self.changedLabel.setText(_translate("HostFileChange", "Partners that will be changed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HostFileChange = QtWidgets.QMainWindow()
    ui = Ui_HostFileChange()
    ui.setupui()
    HostFileChange.show()
    sys.exit(app.exec_())
