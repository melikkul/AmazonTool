# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asinfetcher.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 700)
        MainWindow.setMinimumSize(QSize(600, 700))
        MainWindow.setMaximumSize(QSize(600, 700))
        MainWindow.setStyleSheet(u"background-color:#222831;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 60, 231, 51))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color:#00ADB5;\n"
"color: white;\n"
"border-radius: 10px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 230, 361, 31))
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(11)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"background-color: white;")
        self.lineEdit.setCursorPosition(0)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 310, 361, 31))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"background-color: white;")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(154, 370, 100, 40))
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(10)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background-color:white;\n"
"border-radius:10px;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(330, 370, 100, 40))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"background-color:white;\n"
"border-radius:10px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fi-Asin", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fi-Asin Fetcher", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Giri\u015f Yap", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Kaydol", None))
    # retranslateUi

