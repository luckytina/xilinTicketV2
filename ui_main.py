# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\python\xilin_ticket\main.ui'
#
# Created: Wed Apr 23 23:35:23 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(977, 656)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 971, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.edit_username = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.edit_username.setObjectName("edit_username")
        self.horizontalLayout.addWidget(self.edit_username)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.edit_password = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.edit_password.setObjectName("edit_password")
        self.horizontalLayout.addWidget(self.edit_password)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.edit_auth_code = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.edit_auth_code.setMaximumSize(QtCore.QSize(60, 16777215))
        self.edit_auth_code.setObjectName("edit_auth_code")
        self.horizontalLayout.addWidget(self.edit_auth_code)
        self.lb_auth_img = ClickedLabel(self.horizontalLayoutWidget)
        self.lb_auth_img.setMinimumSize(QtCore.QSize(100, 24))
        self.lb_auth_img.setMaximumSize(QtCore.QSize(100, 40))
        self.lb_auth_img.setStyleSheet("background-color:white")
        self.lb_auth_img.setText("")
        self.lb_auth_img.setObjectName("lb_auth_img")
        self.horizontalLayout.addWidget(self.lb_auth_img)
        self.loginBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.loginBtn.setObjectName("loginBtn")
        self.horizontalLayout.addWidget(self.loginBtn)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 50, 971, 581))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox.setMinimumSize(QtCore.QSize(600, 0))
        self.groupBox.setObjectName("groupBox")
        self.memo = QtWidgets.QTextEdit(self.groupBox)
        self.memo.setGeometry(QtCore.QRect(10, 20, 581, 551))
        self.memo.setObjectName("memo")
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lb_speed_num = QtWidgets.QLabel(self.groupBox_2)
        self.lb_speed_num.setGeometry(QtCore.QRect(201, 20, 71, 20))
        self.lb_speed_num.setObjectName("lb_speed_num")
        self.group_query = QtWidgets.QGroupBox(self.groupBox_2)
        self.group_query.setGeometry(QtCore.QRect(10, 50, 341, 91))
        self.group_query.setObjectName("group_query")
        self.edit_from_station = QtWidgets.QLineEdit(self.group_query)
        self.edit_from_station.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.edit_from_station.setObjectName("edit_from_station")
        self.lb_to = QtWidgets.QLabel(self.group_query)
        self.lb_to.setGeometry(QtCore.QRect(100, 20, 21, 16))
        self.lb_to.setObjectName("lb_to")
        self.edit_to_station = QtWidgets.QLineEdit(self.group_query)
        self.edit_to_station.setGeometry(QtCore.QRect(130, 20, 71, 21))
        self.edit_to_station.setObjectName("edit_to_station")
        self.dateControl = QtWidgets.QDateEdit(self.group_query)
        self.dateControl.setGeometry(QtCore.QRect(210, 20, 111, 21))
        self.dateControl.setMinimumDate(QtCore.QDate(2014, 1, 1))
        self.dateControl.setDate(QtCore.QDate(2014, 9, 14))
        self.dateControl.setObjectName("dateControl")
        self.searchBtn = QtWidgets.QToolButton(self.group_query)
        self.searchBtn.setGeometry(QtCore.QRect(130, 50, 71, 31))
        self.searchBtn.setCheckable(True)
        self.searchBtn.setChecked(False)
        self.searchBtn.setAutoRepeat(False)
        self.searchBtn.setObjectName("searchBtn")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 150, 351, 351))
        self.groupBox_4.setObjectName("groupBox_4")
        self.passager_table = TableWidget(self.groupBox_4)
        self.passager_table.setGeometry(QtCore.QRect(10, 20, 331, 251))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.passager_table.setFont(font)
        self.passager_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.passager_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.passager_table.setGridStyle(QtCore.Qt.DashLine)
        self.passager_table.setObjectName("passager_table")
        self.passager_table.setColumnCount(4)
        self.passager_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.passager_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.passager_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.passager_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.passager_table.setHorizontalHeaderItem(3, item)
        self.passager_table.horizontalHeader().setVisible(True)
        self.passager_table.horizontalHeader().setDefaultSectionSize(82)
        self.passager_table.horizontalHeader().setHighlightSections(False)
        self.passager_table.horizontalHeader().setMinimumSectionSize(1)
        self.passager_table.verticalHeader().setVisible(False)
        self.passager_table.verticalHeader().setDefaultSectionSize(30)
        self.passager_table.verticalHeader().setMinimumSectionSize(20)
        self.cb_first_seat = QtWidgets.QCheckBox(self.groupBox_4)
        self.cb_first_seat.setGeometry(QtCore.QRect(20, 280, 91, 19))
        self.cb_first_seat.setObjectName("cb_first_seat")
        self.cb_second_seat = QtWidgets.QCheckBox(self.groupBox_4)
        self.cb_second_seat.setGeometry(QtCore.QRect(120, 280, 91, 19))
        self.cb_second_seat.setChecked(True)
        self.cb_second_seat.setObjectName("cb_second_seat")
        self.cb_soft_bed = QtWidgets.QCheckBox(self.groupBox_4)
        self.cb_soft_bed.setGeometry(QtCore.QRect(20, 300, 91, 19))
        self.cb_soft_bed.setObjectName("cb_soft_bed")
        self.cb_hard_bed = QtWidgets.QCheckBox(self.groupBox_4)
        self.cb_hard_bed.setGeometry(QtCore.QRect(120, 300, 91, 19))
        self.cb_hard_bed.setChecked(True)
        self.cb_hard_bed.setObjectName("cb_hard_bed")
        self.cb_hard_seat = QtWidgets.QCheckBox(self.groupBox_4)
        self.cb_hard_seat.setGeometry(QtCore.QRect(20, 320, 91, 19))
        self.cb_hard_seat.setChecked(True)
        self.cb_hard_seat.setObjectName("cb_hard_seat")
        self.cb_stand = QtWidgets.QCheckBox(self.groupBox_4)
        self.cb_stand.setGeometry(QtCore.QRect(120, 320, 91, 19))
        self.cb_stand.setObjectName("cb_stand")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 520, 261, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.btn_my_blog = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_my_blog.setGeometry(QtCore.QRect(10, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(7)
        self.btn_my_blog.setFont(font)
        self.btn_my_blog.setObjectName("btn_my_blog")
        self.btn_url_12306 = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_url_12306.setGeometry(QtCore.QRect(140, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(7)
        self.btn_url_12306.setFont(font)
        self.btn_url_12306.setObjectName("btn_url_12306")
        self.lb_speed = QtWidgets.QLabel(self.groupBox_2)
        self.lb_speed.setGeometry(QtCore.QRect(12, 22, 72, 16))
        self.lb_speed.setObjectName("lb_speed")
        self.slider = QtWidgets.QSlider(self.groupBox_2)
        self.slider.setGeometry(QtCore.QRect(61, 22, 131, 20))
        self.slider.setMinimum(1)
        self.slider.setMaximum(5)
        self.slider.setSingleStep(1)
        self.slider.setPageStep(1)
        self.slider.setProperty("value", 3)
        self.slider.setTracking(True)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setInvertedAppearance(False)
        self.slider.setInvertedControls(False)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.slider.setTickInterval(1)
        self.slider.setObjectName("slider")
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 977, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "帐号："))
        self.label_2.setText(_translate("MainWindow", "密码："))
        self.label_3.setText(_translate("MainWindow", "验证码："))
        self.loginBtn.setText(_translate("MainWindow", "登录"))
        self.groupBox.setTitle(_translate("MainWindow", "日志"))
        self.groupBox_2.setTitle(_translate("MainWindow", "设置"))
        self.lb_speed_num.setText(_translate("MainWindow", "3s"))
        self.group_query.setTitle(_translate("MainWindow", "查询"))
        self.lb_to.setText(_translate("MainWindow", "到"))
        self.dateControl.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.searchBtn.setText(_translate("MainWindow", "开始"))
        self.groupBox_4.setTitle(_translate("MainWindow", "预定信息"))
        item = self.passager_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "购买"))
        item = self.passager_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.passager_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "手机"))
        item = self.passager_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "身份证"))
        self.cb_first_seat.setText(_translate("MainWindow", "一等座"))
        self.cb_second_seat.setText(_translate("MainWindow", "二等座"))
        self.cb_soft_bed.setText(_translate("MainWindow", "软卧"))
        self.cb_hard_bed.setText(_translate("MainWindow", "硬卧"))
        self.cb_hard_seat.setText(_translate("MainWindow", "硬座"))
        self.cb_stand.setText(_translate("MainWindow", "无座"))
        self.groupBox_5.setTitle(_translate("MainWindow", "帮助"))
        self.btn_my_blog.setText(_translate("MainWindow", "查看更新"))
        self.btn_url_12306.setText(_translate("MainWindow", "打开12036"))
        self.lb_speed.setText(_translate("MainWindow", "间隔："))

from tablewidget import TableWidget
from clickedlabel import ClickedLabel
