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
        Conf.resize(479, 304)
        Conf.setMinimumSize(QSize(479, 304))
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
        self.verticalLayout_2.setSpacing(10)
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
        self.verticalLayout_3.setSpacing(21)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:white")

        self.verticalLayout_4.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.btn_apagar_conversas = QPushButton(self.frame_3)
        self.btn_apagar_conversas.setObjectName(u"btn_apagar_conversas")
        self.btn_apagar_conversas.setMinimumSize(QSize(0, 37))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(False)
        font2.setWeight(50)
        self.btn_apagar_conversas.setFont(font2)
        self.btn_apagar_conversas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_apagar_conversas.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"background-color:#5f6368;\n"
"border:1px solid ;\n"
"border-radius:10px;\n"
"outline:0\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(237, 51, 59);\n"
"border:1px solid rgb(237, 51, 59);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_apagar_conversas)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 1100))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color:white")

        self.verticalLayout_5.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.texto_feedback = QTextEdit(self.frame_4)
        self.texto_feedback.setObjectName(u"texto_feedback")
        self.texto_feedback.setStyleSheet(u"\n"
"QTextEdit{\n"
"padding:3px;color:white;\n"
"border-radius:5px;border:1px solid gray;\n"
"outline:0\n"
"}\n"
"QTextEdit:focus{\n"
"border:1px solid rgb(32, 47, 177)\n"
"}")
        self.texto_feedback.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_5.addWidget(self.texto_feedback)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.saida = QLabel(self.frame_5)
        self.saida.setObjectName(u"saida")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.saida.setFont(font3)
        self.saida.setStyleSheet(u"color: rgb(11, 166, 15);")

        self.horizontalLayout.addWidget(self.saida)

        self.btn_feedback = QPushButton(self.frame_5)
        self.btn_feedback.setObjectName(u"btn_feedback")
        self.btn_feedback.setFont(font2)
        self.btn_feedback.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_feedback.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"padding:8px;\n"
"outline:0;\n"
"color:white\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/paper-plane-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_feedback.setIcon(icon1)
        self.btn_feedback.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_feedback, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_5)


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
#if QT_CONFIG(tooltip)
        self.btn_apagar_conversas.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_apagar_conversas.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_apagar_conversas.setText(QCoreApplication.translate("Conf", u"Apagar mensagens", None))
        self.label_3.setText(QCoreApplication.translate("Conf", u"Enviar feedback do aplicativo ao desenvolvedor.", None))
        self.saida.setText("")
        self.btn_feedback.setText(QCoreApplication.translate("Conf", u"Enviar feedback", None))
    # retranslateUi

