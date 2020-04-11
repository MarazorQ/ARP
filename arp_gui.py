# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arp_gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 624)
        MainWindow.setMinimumSize(1000, 630)
        MainWindow.setMaximumSize(1920, 1080)
        MainWindow.move(450, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ip_label = QtWidgets.QLabel(self.centralwidget)
        self.ip_label.setObjectName("ip_label")
        self.horizontalLayout.addWidget(self.ip_label)
        self.ip_line = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_line.setFrame(True)
        self.ip_line.setReadOnly(True)
        self.ip_line.setObjectName("ip_line")
        self.horizontalLayout.addWidget(self.ip_line)
        self.mask_label = QtWidgets.QLabel(self.centralwidget)
        self.mask_label.setObjectName("mask_label")
        self.horizontalLayout.addWidget(self.mask_label)
        self.mask_line = QtWidgets.QLineEdit(self.centralwidget)
        self.mask_line.setEnabled(True)
        self.mask_line.setReadOnly(True)
        self.mask_line.setObjectName("mask_line")
        self.horizontalLayout.addWidget(self.mask_line)
        self.interface_box = QtWidgets.QComboBox(self.centralwidget)
        self.interface_box.setObjectName("interface_box")
        self.interface_box.addItem("")
        self.horizontalLayout.addWidget(self.interface_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setTabKeyNavigation(False)
        self.table.setProperty("showDropIndicator", False)
        self.table.setDragDropOverwriteMode(False)
        self.table.setTextElideMode(QtCore.Qt.ElideLeft)
        self.table.setShowGrid(True)
        self.table.setWordWrap(True)
        self.table.setCornerButtonEnabled(True)
        self.table.setObjectName("table")
        self.table.setColumnCount(2)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setDefaultSectionSize(170)
        self.table.horizontalHeader().setHighlightSections(False)
        self.table.horizontalHeader().setMinimumSectionSize(100)
        self.table.horizontalHeader().setSortIndicatorShown(False)
        self.table.horizontalHeader().setStretchLastSection(False)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setCascadingSectionResizes(True)
        self.table.verticalHeader().setSortIndicatorShown(False)
        self.table.verticalHeader().setStretchLastSection(False)
        resize_header = self.table.horizontalHeader()
        resize_header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        resize_header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.verticalLayout.addWidget(self.table)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scan_btn = QtWidgets.QPushButton(self.centralwidget)
        self.scan_btn.setMinimumSize(QtCore.QSize(0, 45))
        self.scan_btn.setObjectName("scan_btn")
        self.horizontalLayout_2.addWidget(self.scan_btn)
        self.find_network_btn = QtWidgets.QPushButton(self.centralwidget)
        self.find_network_btn.setMinimumSize(QtCore.QSize(0, 45))
        self.find_network_btn.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.find_network_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NETWORK SCAN"))
        MainWindow.setWindowIcon(QtGui.QIcon('images/icon.png'))
        self.ip_label.setText(_translate("MainWindow", "IP"))
        self.mask_label.setText(_translate("MainWindow", "MASK"))
        self.interface_box.setItemText(0, _translate("MainWindow", "CHOOSE A NETWORK..."))
        self.table.setSortingEnabled(False)
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "IP ADDRESS"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MAC ADDRESS"))
        self.scan_btn.setText(_translate("MainWindow", "SCAN NETWORK"))
        self.find_network_btn.setText(_translate("MainWindow", "FIND NEW NETWORKS"))

    @staticmethod
    def print_message(title, text):
        msg = QtWidgets.QMessageBox()
        msg.setStyleSheet("QLabel{font-size:13px; }")

        msg.setText(text)
        msg.setWindowTitle(title)
        msg.setStandardButtons(
            QtWidgets.QMessageBox().Ok | QtWidgets.QMessageBox().Cancel
        )

        msg.exec_()

    def add_table_item(self, ip, mac):
        table = self.table
        table.setRowCount(table.rowCount() + 1)

        table.setItem(table.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(ip))
        table.setItem(table.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(mac))
