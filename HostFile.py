from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QSystemTrayIcon, QAction, QMenu, QAbstractButton, QPushButton, QTextEdit, QListWidget, QLineEdit
from PyQt5.QtGui import QIcon
import shutil, os, sys, platform
import pymysql

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
        HostFileChange.resize(450, 500)
        HostFileChange.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.centralwidget = QtWidgets.QWidget(HostFileChange)
        self.centralwidget.setObjectName("centralwidget")

        self.ipText = QTextEdit(self.centralwidget)
        self.ipText.setGeometry(QtCore.QRect(20, 30, 191, 31))
        self.ipText.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ipText.setObjectName("ipText")

        self.ipButton = QPushButton(self.centralwidget)
        self.ipButton.setGeometry(QtCore.QRect(260, 410, 121, 31))
        self.ipButton.setStyleSheet("background-color: rgb(24, 186, 118);")
        self.ipButton.setObjectName("ipButton")

        self.clear = QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(20, 412, 111, 31))
        self.clear.setStyleSheet("background-color: rgb(24, 186, 118);")
        self.clear.setObjectName("clearButton")

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(260, 330, 121, 31))
        self.generateButton.setStyleSheet("background-color: rgb(24, 186, 118);")
        self.generateButton.setObjectName("generateButton")

        self.nameText = QtWidgets.QTextEdit(self.centralwidget)
        self.nameText.setGeometry(QtCore.QRect(20, 90, 191, 31))
        self.nameText.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nameText.setObjectName("nameText")

        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(260, 90, 121, 31))
        self.searchButton.setStyleSheet("background-color: rgb(24, 186, 118);")
        self.searchButton.setObjectName("searchButton")

        self.changeIp = QtWidgets.QPushButton("ipButton")
        self.generate = QtWidgets.QPushButton("generateButton")
        self.search = QtWidgets.QPushButton("searchButton")

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


        self.view = QListWidget(self)
        Functions.listing(self.view)

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

        self.clear.clicked.connect(lambda: Functions.click('', ''))
        self.ipButton.clicked.connect(lambda: Functions.change_click(self, False))

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
        self.clear.setText(_translate("HostFileChange", "Clear the Host File"))
        self.generateButton.setText(_translate("HostFileChange", "Generate Partner"))
        self.searchButton.setText(_translate("HostFileChange", "Search Partner"))
        self.ipLabel.setText(_translate("HostFileChange", "Enter Machine IP:"))
        self.nameLabel.setText(_translate("HostFileChange", "Enter Partner Name:"))
        self.changedLabel.setText(_translate("HostFileChange", "Partners that will be changed"))

    def set_static_api(ip, task_id):

        host = open("hosts", 'a')
        #host.write(ip + " " + task_id + ".static.api.useinsider.com" + "\n\n") UNNECESSARY
        host.close()

    def open_and_write_partner(ip, partner_name):

        host = open("hosts", 'a')
        site_list = [
            partner_name + ".inone.useinsider.com",
            partner_name + ".panel.sociaplus.com",
            partner_name + ".api.sociaplus.com",
            partner_name + ".panel.useinsider.com",
            partner_name + ".api.useinsider.com"
        ]

        for i in site_list:
            host.write(ip + ' ' + i + '\n')

        host.write("\n")
        host.close()


class Functions():

    def __init__(self):
        pass

    def click(ip, sites):
        "Working directory is needed for moving command in order to move the newly created host file"
        project_direct = os.path.join(os.getcwd(), "hosts")

        "Check the OS for host file destination directory and command"
        if platform.system() == "Linux":
            "For linux host file directory is constant"
            host_direct = '/etc/hosts'
            command = 'mv'
            prefix = 'pkexec '

        elif platform.system() == "Windows":
            host_direct = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
            command = 'move'
            prefix = ''

        else:
            return "OS cannot be identified. This program only runs at Linux and Windows"

        print("alper")

        "If the ip is given then the rest of the change function executes. Otherwise host file will be empty"
        if (ip != ''):

            Functions.new_write_file(5)
            "Check if the ip is in right format"
            dot = ip.count('.')
            if (dot != 3):
                return "Ip is not in right format"

            "Check if the partner list is not empty"
            if (sites != []):

                "for every site in sites list the ip is added"
                #for site in sites:
                    #Functions.open_and_write_partner(ip, site)

            "Ip will always prepended to all constant links"
            print("aaaaaa")
            Functions.add_sabit_links(ip)

        else:
            "This part executes when the user did not enter ip or pressed clear button on UI"
            "If the ip is not given then the user wants to clear their host file"
            Functions.new_write_file(5)

        "Host file is fully created with the user requests. Move command is executed"
        #os.system(prefix + command + ' ' + project_direct + ' ' + host_direct)
        #shutil.move(host_direct)


    def listing(view):

        "Check if the sites.txt file exists"
        if os.path.isfile("sites.txt"):
            a = 0
            file = open("sites.txt", "r")

            for i in file:
                "removes '\n' from the end of the strings"
                text = i[:-1]
                view.insertItem(a, text)
                a += 1

    def add_partner(view, new_partner):

        new_part = new_partner.text()
        file = open("sites.txt", "a")
        file.write(new_part + "\n")

        size = len(view)
        view.insertItem(size, new_part)
        new_partner = ""

    def update_partners(partners):
        """
        :type partners: list <QListWidgetItem>
        """
        file = open("sites.txt", "w")

        "write partners one by one"
        for i in range(len(partners)):
            file.write(partners[i].text() + '\n')

    def new_write_file(self):

        if platform.system() == "Linux":
            host = open("hosts", "w")
            print("Linux")
            sites = [
                "127.0.0.1	localhost",
                "127.0.1.1	insider",
                "::1     ip6-localhost ip6-loopback",
                "fe00::0 ip6-localnet",
                "ff00::0 ip6-mcastprefix",
                "ff02::1 ip6-allnodes",
                "ff02::2 ip6-allrouters"
            ]
        elif platform.system() == "Windows":
            host = open("hosts", "a")
            host.truncate(0)
            print("Windows")
            sites = [
                "127.0.0.1	localhost",
                "127.0.1.1	insider",
                "::1     ip6-localhost ip6-loopback",
                "fe00::0 ip6-localnet",
                "ff00::0 ip6-mcastprefix",
                "ff02::1 ip6-allnodes",
                "ff02::2 ip6-allrouters"
            ]

        for s in sites:
            host.write(s + '\n')
        host.write("\n")
        host.close()

    def change_click(self, local):
        if not local:
            ip = self.ipText.toPlainText()
            sites = []
            for i in range(self.view.count()): #hata burada
                print("alper")
                sites.append(str(self.view.item(i).text())) #instead of text I should have my list from the database
        elif local:
            ip = "127.0.0.1"
            sites = []
            for i in range(self.view.count()):
                sites.append(str(self.view.item(i).text()))
        Functions.click(ip, sites)

    def add_sabit_links(ip):
        print("alper")
        host = open("hosts", "a")
        site_list = Functions.get_static_list()
        if ip == '127.0.0.1':
            site_list.append("local.static.api.useinsider.com")

        for i in site_list:
            host.write(ip + ' ' + i + '\n')

        host.write("\n")
        host.close()

    def get_static_list():
        db = pymysql.connect(host="qa-insider-rds.cdu0cfttyttl.eu-west-1.rds.amazonaws.com",
                             user="",
                             password="",
                             port=3306,
                             db="spPanel",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM hosts_static_url")
        url = cursor.fetchall()
        site_list = []
        for i in url:
            site_list.append(i["url"])
        return site_list


if __name__ == "__main__":
    import sys
    Functions.get_static_list()
    app = QtWidgets.QApplication(sys.argv)
    HostFileChange = QtWidgets.QMainWindow()
    ui = Ui_HostFileChange()
    HostFileChange.show()
    sys.exit(app.exec_())
