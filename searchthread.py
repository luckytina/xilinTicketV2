__author__ = 'Administrator'
from PyQt5.QtCore import (QThread,pyqtSignal,QSemaphore,QUrl,QEventLoop,QObject)
from PyQt5.QtNetwork import (QNetworkAccessManager,QNetworkRequest,QNetworkReply)
import requests
import xlstr
import time
import urllib.request
import json

mutex=QSemaphore(5)

class SearchThread(QThread):
    domain = 'kyfw.12306.cn' #请求域名（真实连接地址）
    host='kyfw.12306.cn' #请求的域名（host）
    http = requests.session()
    stopSignal=False
    threadId=1


    searchThreadCallback= pyqtSignal(list)

    def __init__(self,from_station,to_station,train_date,threadId,interval=2,domain=''):
        super(SearchThread,self).__init__()
        if domain!='':
            self.domain=domain

        self.threadId=threadId
        self.from_station=from_station
        self.to_station=to_station
        self.train_date=train_date
        self.interval=interval


    def run(self):
        time.sleep(self.threadId)
        self.netWorkManager=QNetworkAccessManager()
        if not self.load_station_code():
            print('加载车站码异常')

        userAgent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"
        headers={'Referer':'',"host":self.host\
            ,'Cache-Control':'no-cache','Pragma':"no-cache","User-Agent":userAgent}

        url='https://' + self.domain + '/otn/leftTicket/query?leftTicketDTO.train_date='+self.train_date\
            +"&leftTicketDTO.from_station="+self.stationCode[self.from_station]+"&leftTicketDTO.to_station="+\
            self.stationCode[self.to_station]+"&purpose_codes=ADULT"

        self.req=QNetworkRequest()
        self.req.setUrl(QUrl(url))
        self.req.setRawHeader("Referer","https://kyfw.12306.cn/otn/leftTicket/init")
        self.req.setRawHeader("host",self.host)
        self.req.setRawHeader("Cache-Control","no-cache")
        self.req.setRawHeader("Pragma","no-cache")
        self.req.setRawHeader("User-Agent",userAgent)

        while not self.stopSignal:
            mutex.acquire(1)
            self.search_ticket(self.from_station,self.to_station,self.train_date)
            mutex.release(1)
            time.sleep(self.interval)


    def search_ticket(self, fromStation, toStation, date):
        try:
            self.reply=self.netWorkManager.get(self.req)
            self.reply.ignoreSslErrors()
            self.reply.finished.connect(self.search_finished)
            self.exec()

        except Exception as e:
            print("ip:"+self.domain+"查询发生错误："+e.__str__())
            return False

    def search_finished(self):
        ret=self.reply.readAll()
        ret=str(ret,'utf8')
        ticketInfo=json.loads(ret)
        self.reply=None
        self.exit()
        if ticketInfo['status']!=True or ticketInfo['messages']!=[] :
            return False

        if len(ticketInfo['data'])<=0:
            return False

        data=ticketInfo['data']
        ret=None
        ticketInfo=None

        self.searchThreadCallback.emit(data)

    def load_station_code(self):
        """Load station telcode from 12306.cn

        加载车站电报码，各个请求中会用到
        :raise C12306Error:
        """
        header={"host":self.host}
        res = self.http.get('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js', verify=False,headers=header)
        if res.status_code != 200:
            return False

        stationStrs = xlstr.substr(res.text, "'", "'")
        stationList = stationStrs.split('@')
        stationDict = {}

        for stationStr in stationList:
            station = stationStr.split("|")
            if len(station) > 3:
                stationDict[station[1]] = station[2]

        self.stationCode = stationDict
        return True

    def stop(self):
        self.stopSignal=True