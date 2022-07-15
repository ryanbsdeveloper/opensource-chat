# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"background-color: rgb(43, 43, 43);	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 120, 661, 61))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 180, 661, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color:#5f6368")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 280, 561, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgb(45, 53, 211)\n"
", stop:1 rgb(17, 36, 95)\n"
"\n"
");\n"
"}")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(99)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 320, 661, 21))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.dropShadowFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 41, 80, 80))
        self.label.setPixmap(QPixmap(u":/icons/logo_chat.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.dropShadowFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(502, 349, 25, 25))
        self.label_2.setMinimumSize(QSize(25, 25))
        self.label_2.setMaximumSize(QSize(25, 25))
        self.label_2.setPixmap(QPixmap(u":/icons/github-brands.svg"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.dropShadowFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(530, 352, 120, 17))
        self.label_3.setStyleSheet(u"color:#5f6368")
        self.label_4 = QLabel(self.dropShadowFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(421, 353, 80, 17))
        self.label_4.setStyleSheet(u"color:#5f6368")

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:600;\">Chat</span> developers</p></body></html>", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p>Chat para desenvolvedores</p></body></html>", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"Carregando...", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("SplashScreen", u"ryanbsdeveloper", None))
        self.label_4.setText(QCoreApplication.translate("SplashScreen", u"Created by:", None))
    # retranslateUi

