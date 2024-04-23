# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asinfetchersettings.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_SettingsWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 700)
        MainWindow.setMinimumSize(QSize(600, 700))
        MainWindow.setMaximumSize(QSize(600, 700))
        MainWindow.setStyleSheet(u"background-color:#EEEEEE;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 600, 100))
        self.widget.setStyleSheet(u"background-color: #00ADB5;")
        self.fiasin_topic = QLabel(self.widget)
        self.fiasin_topic.setObjectName(u"fiasin_topic")
        self.fiasin_topic.setGeometry(QRect(20, 10, 191, 41))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(16)
        font.setBold(True)
        self.fiasin_topic.setFont(font)
        self.fiasin_topic.setStyleSheet(u"backgrond-color: transparent;\n"
"color:white;")
        self.username = QLabel(self.widget)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(400, 70, 191, 20))
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(12)
        self.username.setFont(font1)
        self.username.setStyleSheet(u"color:white;")
        self.username.setAlignment(Qt.AlignCenter)
        self.product_topic = QLabel(self.widget)
        self.product_topic.setObjectName(u"product_topic")
        self.product_topic.setGeometry(QRect(10, 50, 91, 16))
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(10)
        self.product_topic.setFont(font2)
        self.product_topic.setStyleSheet(u"background-color:transparent;\n"
"color: white;")
        self.product_topic.setAlignment(Qt.AlignCenter)
        self.product_limit_topic = QLabel(self.widget)
        self.product_limit_topic.setObjectName(u"product_limit_topic")
        self.product_limit_topic.setGeometry(QRect(120, 50, 91, 16))
        self.product_limit_topic.setFont(font2)
        self.product_limit_topic.setStyleSheet(u"background-color:transparent;\n"
"color: white;")
        self.product_limit_topic.setAlignment(Qt.AlignCenter)
        self.daily_scanner_limit = QLabel(self.widget)
        self.daily_scanner_limit.setObjectName(u"daily_scanner_limit")
        self.daily_scanner_limit.setGeometry(QRect(220, 50, 171, 16))
        self.daily_scanner_limit.setFont(font2)
        self.daily_scanner_limit.setStyleSheet(u"background-color:transparent;\n"
"color: white;")
        self.daily_scanner_limit.setAlignment(Qt.AlignCenter)
        self.product_count = QLabel(self.widget)
        self.product_count.setObjectName(u"product_count")
        self.product_count.setGeometry(QRect(10, 75, 91, 16))
        self.product_count.setFont(font2)
        self.product_count.setStyleSheet(u"background-color:transparent;\n"
"color: white;")
        self.product_count.setAlignment(Qt.AlignCenter)
        self.product_limit_count = QLabel(self.widget)
        self.product_limit_count.setObjectName(u"product_limit_count")
        self.product_limit_count.setGeometry(QRect(120, 75, 91, 16))
        self.product_limit_count.setFont(font2)
        self.product_limit_count.setStyleSheet(u"background-color:transparent;\n"
"color: white;")
        self.product_limit_count.setAlignment(Qt.AlignCenter)
        self.daily_scanner_count = QLabel(self.widget)
        self.daily_scanner_count.setObjectName(u"daily_scanner_count")
        self.daily_scanner_count.setGeometry(QRect(220, 75, 171, 16))
        self.daily_scanner_count.setFont(font2)
        self.daily_scanner_count.setStyleSheet(u"background-color:transparent;\n"
"color: white;")
        self.daily_scanner_count.setAlignment(Qt.AlignCenter)
        self.asin_dosya_konumu = QLineEdit(self.centralwidget)
        self.asin_dosya_konumu.setObjectName(u"asin_dosya_konumu")
        self.asin_dosya_konumu.setGeometry(QRect(30, 130, 411, 40))
        self.asin_dosya_konumu.setFont(font2)
        self.asin_dosya_konumu.setStyleSheet(u"border-radius: 15px;\n"
"background-color:white;")
        self.asin_dosya_konumu.setAlignment(Qt.AlignCenter)
        self.asin_dosya_konumu.setReadOnly(True)
        self.asin_folder_button = QPushButton(self.centralwidget)
        self.asin_folder_button.setObjectName(u"asin_folder_button")
        self.asin_folder_button.setGeometry(QRect(460, 130, 120, 40))
        self.asin_folder_button.setFont(font2)
        self.asin_folder_button.setStyleSheet(u"border-radius:15px;\n"
"background-color: #393E46;\n"
"color:white;")
        self.yukleme_ekrani = QProgressBar(self.centralwidget)
        self.yukleme_ekrani.setObjectName(u"yukleme_ekrani")
        self.yukleme_ekrani.setGeometry(QRect(30, 210, 550, 40))
        self.yukleme_ekrani.setStyleSheet(u"QProgressBar{\n"
"	background-color:white;\n"
"	color:black;\n"
"	border-style: solid;\n"
"	border-radius:15px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius:15px;\n"
"	background-color:#00ADB5;\n"
"}")
        self.yukleme_ekrani.setValue(0)
        self.log_screen = QTextEdit(self.centralwidget)
        self.log_screen.setObjectName(u"log_screen")
        self.log_screen.setGeometry(QRect(30, 280, 550, 350))
        self.log_screen.setFont(font2)
        self.log_screen.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;")
        self.log_screen.setReadOnly(True)
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(70, 640, 150, 50))
        self.start_button.setFont(font2)
        self.start_button.setStyleSheet(u"background-color: #393E46;\n"
"color: white;\n"
"border-radius:10px;")
        self.stop_butto = QPushButton(self.centralwidget)
        self.stop_butto.setObjectName(u"stop_butto")
        self.stop_butto.setGeometry(QRect(360, 640, 150, 50))
        self.stop_butto.setFont(font2)
        self.stop_butto.setStyleSheet(u"background-color: #393E46;\n"
"color:white;\n"
"border-radius: 10px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fi-Asin", None))
        self.fiasin_topic.setText(QCoreApplication.translate("MainWindow", u"Fi-Asin Fetcher", None))
        self.username.setText(QCoreApplication.translate("MainWindow", u"Kullan\u0131c\u0131 Ad\u0131", None))
        self.product_topic.setText(QCoreApplication.translate("MainWindow", u"\u00dcr\u00fcn Say\u0131s\u0131", None))
        self.product_limit_topic.setText(QCoreApplication.translate("MainWindow", u"\u00dcr\u00fcn Limiti", None))
        self.daily_scanner_limit.setText(QCoreApplication.translate("MainWindow", u"G\u00fcnl\u00fck Taranan \u00dcr\u00fcn", None))
        self.product_count.setText(QCoreApplication.translate("MainWindow", u"12000", None))
        self.product_limit_count.setText(QCoreApplication.translate("MainWindow", u"100000", None))
        self.daily_scanner_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.asin_folder_button.setText(QCoreApplication.translate("MainWindow", u"Asin Folder", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Ba\u015flat", None))
        self.stop_butto.setText(QCoreApplication.translate("MainWindow", u"Durdur", None))
    # retranslateUi

