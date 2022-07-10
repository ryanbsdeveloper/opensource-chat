# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Chat(object):
    def setupUi(self, Chat):
        if not Chat.objectName():
            Chat.setObjectName(u"Chat")
        Chat.resize(1157, 728)
        icon = QIcon()
        icon.addFile(u":/icons/logo_chat.png", QSize(), QIcon.Normal, QIcon.Off)
        Chat.setWindowIcon(icon)
        self.centralwidget = QWidget(Chat)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 131))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background:rgb(43,43,43)")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 120))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setSpacing(9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_10)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(70, 70))
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setPixmap(QPixmap(u":/icons/logo_chat.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)

        self.horizontalLayout_8.addWidget(self.label)

        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(500, 16777215))
        font1 = QFont()
        font1.setFamily(u"Ubuntu")
        font1.setPointSize(36)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_3.setFont(font1)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"color:#5f6368")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_3)

        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color:#00923d")

        self.horizontalLayout_8.addWidget(self.label_6)


        self.horizontalLayout_2.addWidget(self.frame_10, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.frame_7)
        self.frame_2.setObjectName(u"frame_2")
        font3 = QFont()
        font3.setPointSize(2)
        self.frame_2.setFont(font3)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(60)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color:#5f6368")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.developer = QPushButton(self.frame_8)
        self.developer.setObjectName(u"developer")
        font5 = QFont()
        font5.setPointSize(17)
        font5.setBold(True)
        font5.setWeight(75)
        self.developer.setFont(font5)
        self.developer.setLayoutDirection(Qt.RightToLeft)
        self.developer.setStyleSheet(u"border:0; color:white")
        icon1 = QIcon()
        icon1.addFile(u":/icons/python", QSize(), QIcon.Normal, QIcon.Off)
        self.developer.setIcon(icon1)
        self.developer.setIconSize(QSize(32, 32))
        self.developer.setAutoDefault(False)

        self.horizontalLayout_6.addWidget(self.developer)


        self.horizontalLayout_5.addWidget(self.frame_8, 0, Qt.AlignHCenter)

        self.btn_config = QPushButton(self.frame_2)
        self.btn_config.setObjectName(u"btn_config")
        self.btn_config.setMaximumSize(QSize(35, 16777215))
        self.btn_config.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_config.setStyleSheet(u"border:0;outline:0")
        icon2 = QIcon()
        icon2.addFile(u":/icons/gear-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_config.setIcon(icon2)
        self.btn_config.setIconSize(QSize(33, 30))

        self.horizontalLayout_5.addWidget(self.btn_config)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, -1, 9)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        font6 = QFont()
        font6.setBold(False)
        font6.setWeight(50)
        self.frame_4.setFont(font6)
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 680, 495))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_13 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 0))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_11 = QFrame(self.frame_13)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 80))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 30))
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")
        font7 = QFont()
        font7.setPointSize(15)
        font7.setBold(True)
        font7.setItalic(False)
        font7.setWeight(75)
        font7.setStrikeOut(False)
        self.label_11.setFont(font7)
        self.label_11.setStyleSheet(u"color:#5f6368")

        self.horizontalLayout_10.addWidget(self.label_11, 0, Qt.AlignRight)

        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(25, 25))
        self.label_12.setPixmap(QPixmap(u":/icons/python"))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_12)


        self.verticalLayout_5.addWidget(self.frame_14, 0, Qt.AlignLeft)

        self.label_13 = QLabel(self.frame_11)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 40))
        font8 = QFont()
        font8.setPointSize(15)
        self.label_13.setFont(font8)
        self.label_13.setStyleSheet(u"padding:5px;\n"
"color:white;\n"
"background-color: rgb(60, 60, 60);")
        self.label_13.setScaledContents(True)
        self.label_13.setWordWrap(False)
        self.label_13.setMargin(0)

        self.verticalLayout_5.addWidget(self.label_13, 0, Qt.AlignLeft)


        self.verticalLayout_7.addWidget(self.frame_11)


        self.verticalLayout_6.addWidget(self.frame_13, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setStyleSheet(u"background:rgb(43,43,43)")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_msg = QPushButton(self.frame_5)
        self.btn_msg.setObjectName(u"btn_msg")
        self.btn_msg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_msg.setStyleSheet(u"border:0;outline:0")
        icon3 = QIcon()
        icon3.addFile(u":/icons/paper-plane-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_msg.setIcon(icon3)
        self.btn_msg.setIconSize(QSize(27, 27))

        self.horizontalLayout_4.addWidget(self.btn_msg)

        self.input_msg = QLineEdit(self.frame_5)
        self.input_msg.setObjectName(u"input_msg")
        font9 = QFont()
        font9.setPointSize(12)
        self.input_msg.setFont(font9)
        self.input_msg.setStyleSheet(u"\n"
"QLineEdit{\n"
"padding:10px;color:white;\n"
"border-radius:5px;border:1px solid white\n"
"}\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(32, 47, 177)\n"
"}")

        self.horizontalLayout_4.addWidget(self.input_msg)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 20))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color:#5f6368")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(20, 20))
        self.label_8.setStyleSheet(u"color:#5f6368")
        self.label_8.setPixmap(QPixmap(u":/icons/github-brands.svg"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color:#5f6368")

        self.horizontalLayout_7.addWidget(self.label_9)


        self.verticalLayout_2.addWidget(self.frame_9, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(100, 0))
        self.frame_12.setMaximumSize(QSize(435, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.frame_15)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(30, 22))
        self.label_4.setPixmap(QPixmap(u":/icons/users-solid.svg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_4)

        self.label_2 = QLabel(self.frame_15)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color:#5f6368")

        self.horizontalLayout_9.addWidget(self.label_2, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.frame_15, 0, Qt.AlignHCenter)

        self.scrollArea_2 = QScrollArea(self.frame_12)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 415, 86))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.scrollAreaWidgetContents)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"border-bottom:1px solid #5f6368;")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, -1, 0)
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_19 = QLabel(self.frame_17)
        self.label_19.setObjectName(u"label_19")
        font10 = QFont()
        font10.setPointSize(12)
        font10.setBold(False)
        font10.setWeight(50)
        self.label_19.setFont(font10)
        self.label_19.setStyleSheet(u"border:0;\n"
"color: rgb(37, 135, 29);")

        self.horizontalLayout_12.addWidget(self.label_19)

        self.label_15 = QLabel(self.frame_17)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font9)
        self.label_15.setStyleSheet(u"border:0; color:white")

        self.horizontalLayout_12.addWidget(self.label_15)

        self.label_10 = QLabel(self.frame_17)
        self.label_10.setObjectName(u"label_10")
        font11 = QFont()
        font11.setPointSize(13)
        font11.setBold(True)
        font11.setWeight(75)
        self.label_10.setFont(font11)
        self.label_10.setStyleSheet(u"color:#5f6368; border:0")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.label_14 = QLabel(self.frame_17)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(25, 25))
        self.label_14.setStyleSheet(u"border:0")
        self.label_14.setPixmap(QPixmap(u":/icons/java"))
        self.label_14.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_14)


        self.horizontalLayout_11.addWidget(self.frame_17, 0, Qt.AlignLeft)

        self.pushButton = QPushButton(self.frame_16)
        self.pushButton.setObjectName(u"pushButton")
        font12 = QFont()
        font12.setPointSize(8)
        self.pushButton.setFont(font12)
        self.pushButton.setStyleSheet(u"border:0")
        icon4 = QIcon()
        icon4.addFile(u":/icons/flag-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(17, 20))

        self.horizontalLayout_11.addWidget(self.pushButton, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame_16)

        self.frame_18 = QFrame(self.scrollAreaWidgetContents)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"border-bottom:1px solid #5f6368;")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, -1, 0)
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_20 = QLabel(self.frame_19)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"border:0;\n"
"color: rgb(37, 135, 29);")

        self.horizontalLayout_14.addWidget(self.label_20)

        self.label_16 = QLabel(self.frame_19)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font9)
        self.label_16.setStyleSheet(u"border:0; color:white")

        self.horizontalLayout_14.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_19)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font11)
        self.label_17.setStyleSheet(u"color:#5f6368; border:0")

        self.horizontalLayout_14.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_19)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(25, 25))
        self.label_18.setStyleSheet(u"border:0")
        self.label_18.setPixmap(QPixmap(u":/icons/python"))
        self.label_18.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.label_18)


        self.horizontalLayout_13.addWidget(self.frame_19, 0, Qt.AlignLeft)

        self.pushButton_2 = QPushButton(self.frame_18)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font12)
        self.pushButton_2.setStyleSheet(u"border:0")
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QSize(17, 20))

        self.horizontalLayout_13.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame_18)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea_2)


        self.horizontalLayout.addWidget(self.frame_12, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame)

        Chat.setCentralWidget(self.centralwidget)

        self.retranslateUi(Chat)

        QMetaObject.connectSlotsByName(Chat)
    # setupUi

    def retranslateUi(self, Chat):
        Chat.setWindowTitle(QCoreApplication.translate("Chat", u"MainWindow", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("Chat", u"Chat developers", None))
        self.label_6.setText(QCoreApplication.translate("Chat", u"Brasil", None))
        self.label_5.setText(QCoreApplication.translate("Chat", u"Developer:", None))
        self.developer.setText(QCoreApplication.translate("Chat", u"ryanl", None))
        self.btn_config.setText("")
        self.label_11.setText(QCoreApplication.translate("Chat", u"<fred>", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Chat", u"Boa noite galera, Tudo bem?", None))
        self.btn_msg.setText("")
        self.input_msg.setPlaceholderText(QCoreApplication.translate("Chat", u"Nova mensagem", None))
        self.label_7.setText(QCoreApplication.translate("Chat", u"Create by:", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("Chat", u"ryanbsdeveloper", None))
        self.label_4.setText("")
        self.label_2.setText(QCoreApplication.translate("Chat", u"Membros da comunidade", None))
        self.label_19.setText(QCoreApplication.translate("Chat", u"\u25c9", None))
        self.label_15.setText(QCoreApplication.translate("Chat", u"Developer:", None))
        self.label_10.setText(QCoreApplication.translate("Chat", u"fred", None))
        self.label_14.setText("")
        self.pushButton.setText("")
        self.label_20.setText(QCoreApplication.translate("Chat", u"\u25c9", None))
        self.label_16.setText(QCoreApplication.translate("Chat", u"Developer:", None))
        self.label_17.setText(QCoreApplication.translate("Chat", u"clebinhojr", None))
        self.label_18.setText("")
        self.pushButton_2.setText("")
    # retranslateUi

