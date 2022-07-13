# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'conf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_Conf(object):
    def setupUi(self, Conf):
        if not Conf.objectName():
            Conf.setObjectName(u"Conf")
        Conf.setWindowModality(Qt.WindowModal)
        Conf.resize(479, 200)
        Conf.setMinimumSize(QSize(479, 200))
        Conf.setMaximumSize(QSize(479, 304))
        icon = QIcon()
        icon.addFile(u":/icons/gear-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        Conf.setWindowIcon(icon)
        Conf.setAutoFillBackground(False)
        Conf.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        Conf.setInputMethodHints(Qt.ImhNone)
        Conf.setModal(True)
        self.verticalLayout = QVBoxLayout(Conf)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.frame = QFrame(Conf)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(461, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:white")

        self.verticalLayout_4.addWidget(self.label_2)

        self.btn_apagar_conversas = QPushButton(self.frame_3)
        self.btn_apagar_conversas.setObjectName(u"btn_apagar_conversas")
        self.btn_apagar_conversas.setMinimumSize(QSize(0, 37))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_apagar_conversas.setFont(font2)
        self.btn_apagar_conversas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_apagar_conversas.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"background-color:#5f6368;\n"
"border:1px solid rgb(237, 51, 59);\n"
"border-radius:10px;\n"
"outline:0\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(237, 51, 59);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_apagar_conversas)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 30))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.checkBox_notificacoes = QCheckBox(self.frame_4)
        self.checkBox_notificacoes.setObjectName(u"checkBox_notificacoes")
        self.checkBox_notificacoes.setFont(font1)
        self.checkBox_notificacoes.setStyleSheet(u"\n"
"QCheckBox{\n"
"color:white;outline:0\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_notificacoes)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Conf)

        QMetaObject.connectSlotsByName(Conf)
    # setupUi

    def retranslateUi(self, Conf):
        Conf.setWindowTitle(QCoreApplication.translate("Conf", u"Configura\u00e7\u00e3o", None))
        self.label.setText(QCoreApplication.translate("Conf", u"Configura\u00e7\u00f5es", None))
        self.label_2.setText(QCoreApplication.translate("Conf", u"Apagar todas a mensagens?", None))
        self.btn_apagar_conversas.setText(QCoreApplication.translate("Conf", u"Apagar mensagens", None))
        self.checkBox_notificacoes.setText(QCoreApplication.translate("Conf", u"Desativar notifica\u00e7\u00f5es", None))
    # retranslateUi

