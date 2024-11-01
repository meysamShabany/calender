from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                          QRect, QSize, QUrl, Qt, QTimer)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                         QRadialGradient)
from PyQt5.QtWidgets import *
import sys
import requests as rq
import datetime
import jdatetime

city = [
    {
        "name": "Sabzevar",
        "fa": "سبزوار"
    },
    {
        "name": "Tehran",
        "fa": "تهران"
    },
    {
        "name": "Mashhad",
        "fa": "مشهد"
    },
    {
        "name": "Esfahan",
        "fa": "اصفهان"
    }
]

class ImageFrame(QFrame):
    text = None

    def __init__(self, loc):
        super().__init__()

        response = rq.get(url="http://api.weatherapi.com/v1/current.json",
                          headers={"key": "149367f5894c473db05141715242008"},
                          params={"q": loc})

        if response.status_code == 200:
            ImageFrame.text = response.json().get("current").get("condition").get("text")
            image_data = response.json().get("current").get("condition").get("icon")
            image_url = "http:" + image_data  # ساخت URL کامل

            image_response = rq.get(image_url)
            if image_response.status_code == 200:

                pixmap = QPixmap()
                pixmap.loadFromData(image_response.content)

                label = QLabel(self)
                label.setPixmap(pixmap.scaled(65, 65, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                label.setAlignment(Qt.AlignCenter)

                layout = QVBoxLayout()
                layout.addWidget(label)
                self.setLayout(layout)
            else:
                print("Unable to fetch image. Status code:", image_response.status_code)
        else:
            print("Unable to fetch weather data. Status code:", response.status_code)


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(341, 478)
        palette = Form.palette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("image/mobile.png")))
        Form.setPalette(palette)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(29, 39, 281, 141))
        self.frame.setStyleSheet(u"background-color: rgba(214, 214, 214 , 0.8);\n"
                                 "border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(46, 20, 191, 51))
        self.label.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
                                 "text-align: center;\n"
                                 "border:1px solid gray;\n"
                                 "padding-right:60px;\n"
                                 "padding-top:10px;\n"
                                 "padding-bottom:10px;\n"
                                 "font-size:18px;\n"
                                 "font-weight: bold;")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 80, 51, 31))
        self.label_2.setStyleSheet(u"text-align: center;\n"
                                   "border:none;\n"
                                   "padding-left:15px;\n"
                                   "font-size:18px;\n"
                                   "font-weight: bold;")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 80, 71, 31))
        self.label_3.setStyleSheet(u"text-align: center;\n"
                                   "border:none;\n"
                                   "padding-right:12px;\n"
                                   "font-size:18px;\n"
                                   "font-weight: bold;")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 80, 61, 31))
        self.label_4.setStyleSheet(u"text-align: center;\n"
                                   "border:none;\n"
                                   "padding-left:4px;\n"
                                   "font-size:18px;\n"
                                   "font-weight: bold;")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(170, 80, 16, 16))
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 199, 281, 251))
        self.frame_2.setStyleSheet(u"background-color: rgba(214, 214, 214 , 0.8);\n"
                                   "border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(0)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 20, 191, 41))
        self.label_6.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
                                   "padding-left:41px;\n"
                                   "padding-top:10px;\n"
                                   "padding-bottom:10px;\n"
                                   "font-size:18px;\n"
                                   "font-weight: bold;\n"
                                   "border:1px solid gray;")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(200, 90, 51, 31))
        self.label_8.setStyleSheet(u"text-align: center;\n"
                                   "border:none;\n"
                                   "padding-left:15px;\n"
                                   "font-size:18px;\n"
                                   "font-weight: bold;")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(100, 90, 91, 31))
        self.label_9.setStyleSheet(u"text-align: center;\n"
                                   "border:none;\n"
                                   "padding-left:7px;\n"
                                   "font-size:14px;\n"
                                   "")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 90, 61, 31))
        self.label_10.setStyleSheet(u"text-align: center;\n"
                                    "border:none;\n"
                                    "padding-left:4px;\n"
                                    "font-size:18px;\n"
                                    "font-weight: bold;")
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(180, 90, 16, 16))
        self.get_current_time()
        self.comboBox = QComboBox(self.frame_2)
        for item in city:
            self.comboBox.addItem(f'{item["fa"]}')
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 170, 91, 22))
        self.comboBox.setStyleSheet(u"padding-left:10px;\n"
                                    "font-size:14px;")
        self.comboBox.currentIndexChanged.connect(self.change_loc)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(170, 130, 80, 20))
        self.label_5.setStyleSheet(u"font-size:14px;\n"
                                   "padding-left:5px;"
                                   "background-color: rgb(255, 255, 255,0);")
        self.label_5.setText("بارگزاری...")
        self.get_loc("Sabzevar")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def get_current_time(self):
        fa_time = jdatetime.datetime.now()
        second_fa = fa_time.strftime("%S")
        minute_fa = fa_time.strftime("%M")
        hour_fa = fa_time.strftime("%H")
        week_day_fa = fa_time.strftime("%A")
        day_fa = fa_time.strftime("%d")
        month_fa_number = fa_time.strftime("%m")
        month_fa = jdatetime.date.today().strftime("%B")
        day_en = datetime.datetime.now().strftime("%d")
        month_en_number = datetime.datetime.now().strftime("%m")
        month_en = datetime.datetime.now().strftime("%B")
        year_en = datetime.datetime.now().strftime("%Y")
        if month_fa == "Aban":
            month_fa = "آبان"
        elif month_fa == "Mehr":
            month_fa = "مهر"
        elif month_fa == "Azar":
            month_fa = "آذر"
        elif month_fa == "Dey":
            month_fa = "دی"
        elif month_fa == "Bahman":
            month_fa = "بهمن"
        elif month_fa == "Esfand":
            month_fa = "اسفند"
        elif month_fa == "Farvardin":
            month_fa = "فروردین"
        elif month_fa == "Ordibehesht":
            month_fa = "اردیبهشت"
        elif month_fa == "Khordad":
            month_fa = "خرداد"
        elif month_fa == "Tir":
            month_fa = "تیر"
        elif month_fa == "Mordad":
            month_fa = "مرداد"
        elif month_fa == "Shahrivar":
            month_fa = "شهریور"
        year_fa = fa_time.strftime("%Y")
        week_d = None
        if week_day_fa == 'Saturday':
            week_d = 'شنبه'
        elif week_day_fa == 'Sunday':
            week_d = 'یکشنبه'
        elif week_day_fa == 'Monday':
            week_d = 'دوشنبه'
        elif week_day_fa == 'Tuesday':
            week_d = 'سه شنبه'
        elif week_day_fa == 'Wednesday':
            week_d = 'چهارشنبه'
        elif week_day_fa == 'Thursday':
            week_d = 'پنجشنبه'
        elif week_day_fa == 'Friday':
            week_d = 'جمعه'
        self.label_6.setText(f"{hour_fa} : {minute_fa} : {second_fa}")
        self.label.setText(week_d)
        self.label_2.setText(day_fa)
        self.label_4.setText(year_fa)
        self.label_7.setText(month_fa_number)
        self.label_3.setText(month_fa)
        self.label_8.setText(day_en)
        self.label_9.setText(month_en)
        self.label_10.setText(year_en)
        self.label_11.setText(month_en_number)
        self.timer = QTimer()
        self.timer.timeout.connect(self.get_current_time)
        self.timer.start(1000)

    def get_loc(self, loc: str):
        try:
            image_frame = ImageFrame(loc=loc)
            image_frame.setParent(self.frame_2)
            image_frame.setGeometry(QRect(119, 160, 151, 81))
            image_frame.setFrameShape(QFrame.StyledPanel)
            image_frame.setFrameShadow(QFrame.Raised)
            self.label_5.setText(image_frame.text)
            self.label_5.setStyleSheet(u"font-size:18px;\n"
                                       "padding-left:5px;"
                                       "background-color: rgb(255, 255, 255,0);")
        except:
            reload = True
            pass

    def change_loc(self):
        loc = None
        text1 = self.comboBox.currentText()
        for item in city:
            if item["fa"] == text1:
                loc = item["name"]
        try:
            image_frame = ImageFrame(loc=loc)
            image_frame.setParent(self.frame_2)
            image_frame.setGeometry(QRect(119, 160, 151, 81))
            image_frame.setFrameShape(QFrame.StyledPanel)
            image_frame.setFrameShadow(QFrame.Raised)
            self.label_5.setText(image_frame.text)
            self.label_5.setStyleSheet(u"font-size:18px;\n"
                                       "padding-left:5px;"
                                       "background-color: rgb(255, 255, 255,0);")
        except:
            reload = True
            pass


    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(
            QCoreApplication.translate("Form", u"\u0686\u0647\u0627\u0631\u0634\u0646\u0628\u0647", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"1", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0645\u0647\u0631", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"1403", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"19 : 15 : 11", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"1", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Septamber", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"2024", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"7", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u0633\u0628\u0632\u0648\u0627\u0631", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u062a\u0647\u0631\u0627\u0646", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u0645\u0634\u0647\u062f", None))

        # self.label_5.setText(QCoreApplication.translate("Form", u"Clear", None))
    # retranslateUi


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

