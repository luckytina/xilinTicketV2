__author__ = 'Administrator'

from ui_main import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5.Qt import *
from configparser import ConfigParser
from c12306 import C12306
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QByteArray
from PyQt5.QtCore import QTimer


class MainWindow(QMainWindow, Ui_MainWindow):
    _config = ConfigParser()
    _my12306 = C12306()
    _search_running = False

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        #响应事件
        self.loginBtn.clicked.connect(self.login)
        self.lb_auth_img.clicked.connect(self.show_auth_code)
        self.slider.valueChanged.connect(self.query_interval_changed)
        self.searchBtn.clicked.connect(self.search)
        #加载验证码
        self.show_auth_code()
        self.passager_table.create_menu()

        self._config.read("config.ini")
        config_dict = self._config.defaults()

        try:
            username = config_dict['username']
            password = config_dict['password']
            self.edit_username.setText(username)
            self.edit_password.setText(password)
        except:
            pass

    def login(self):
        username = self.edit_username.text()
        password = self.edit_password.text()
        auth_code = self.edit_auth_code.text()
        self._config.set('DEFAULT', 'username', username)
        self._config.set('DEFAULT', 'password', password)
        with open('config.ini', 'w') as configfile:
            self._config.write(configfile)
            configfile.close()

        self._my12306.login(username, password, auth_code)


    def show_auth_code(self):
        img_data = self._my12306.auth_code_img('login')
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(img_data))
        self.lb_auth_img.setPixmap(pixmap)
        self.lb_auth_img.setScaledContents(True)
        self.lb_auth_img.show()

    def query_interval_changed(self, value):
        self.lb_speed_num.setText(str(value) + "s")

    def search(self, start: bool):
        if start:
            self.from_station = self.edit_from_station.text()
            self.to_station = self.edit_to_station.text()
            self.train_date = self.dateControl.date().toString("yyyy-MM-dd")

            #定时执行
            self._timer=QTimer()
            self._timer.timeout.connect(self.interval_search)
            self._timer.start(self.slider.sliderPosition()*1000)
            self.searchBtn.setText('停止')
        else:
            self._timer.stop()
            self.searchBtn.setText('开始')


    def interval_search(self):
        self.memo.append("cc")