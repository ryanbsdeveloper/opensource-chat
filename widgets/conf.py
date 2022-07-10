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
        Conf.setAutoFillBackground(True)
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

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color:#5f6368")

        self.horizontalLayout.addWidget(self.label_3, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.label_tec_favorita = QLabel(self.frame_6)
        self.label_tec_favorita.setObjectName(u"label_tec_favorita")
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_tec_favorita.setFont(font4)
        self.label_tec_favorita.setStyleSheet(u"color:white")

        self.horizontalLayout.addWidget(self.label_tec_favorita, 0, Qt.AlignBottom)


        self.verticalLayout_6.addWidget(self.frame_6, 0, Qt.AlignLeft)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 9, 0, 0)
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color:white")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_5)

        self.comboBox_tec = QComboBox(self.frame_7)
        icon1 = QIcon()
        icon1.addFile(u":/icons/python", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_tec.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/icons/java", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_tec.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/icons/js", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_tec.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/icons/kotlin", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_tec.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/icons/node", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_tec.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/icons/php", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_tec.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u":/icons/c#", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_tec.addItem(icon7, "")
        icon8 = QIcon()
        icon8.addFile(u":/icons/c", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_tec.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addFile(u":/icons/angular", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_tec.addItem(icon9, "")
        icon10 = QIcon()
        icon10.addFile(u":/icons/csshtml", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_tec.addItem(icon10, "")
        icon11 = QIcon()
        icon11.addFile(u":/icons/react", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_tec.addItem(icon11, "")
        icon12 = QIcon()
        icon12.addFile(u":/icons/ruby", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_tec.addItem(icon12, "")
        icon13 = QIcon()
        icon13.addFile(u":/icons/swift", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_tec.addItem(icon13, "")
        icon14 = QIcon()
        icon14.addFile(u":/icons/vue", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_tec.addItem(icon14, "")
        icon15 = QIcon()
        icon15.addFile(u":/icons/c++", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_tec.addItem(icon15, "")
        icon16 = QIcon()
        icon16.addFile(u":/icons/nehum", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_tec.addItem(icon16, "")
        self.comboBox_tec.setObjectName(u"comboBox_tec")
        font5 = QFont()
        font5.setPointSize(13)
        self.comboBox_tec.setFont(font5)
        self.comboBox_tec.setStyleSheet(u"outline:0")
        self.comboBox_tec.setMaxVisibleItems(12)

        self.verticalLayout_7.addWidget(self.comboBox_tec)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_salvar = QPushButton(self.frame_8)
        self.btn_salvar.setObjectName(u"btn_salvar")
        self.btn_salvar.setMinimumSize(QSize(150, 0))
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setWeight(75)
        self.btn_salvar.setFont(font6)
        self.btn_salvar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 53, 211);\n"
"border:0;\n"
"padding:10px;\n"
"border-radius:10px;\n"
"outline:0")

        self.horizontalLayout_2.addWidget(self.btn_salvar)


        self.verticalLayout_7.addWidget(self.frame_8, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_7)


        self.verticalLayout_3.addWidget(self.frame_5)


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
        self.label_3.setText(QCoreApplication.translate("Conf", u"Tecnologia favorita atual:", None))
        self.label_tec_favorita.setText(QCoreApplication.translate("Conf", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Conf", u"Mudar de tecnologia", None))
        self.comboBox_tec.setItemText(0, QCoreApplication.translate("Conf", u"Python", None))
        self.comboBox_tec.setItemText(1, QCoreApplication.translate("Conf", u"Java", None))
        self.comboBox_tec.setItemText(2, QCoreApplication.translate("Conf", u"JavaScript", None))
        self.comboBox_tec.setItemText(3, QCoreApplication.translate("Conf", u"Kotlin", None))
        self.comboBox_tec.setItemText(4, QCoreApplication.translate("Conf", u"NodeJS", None))
        self.comboBox_tec.setItemText(5, QCoreApplication.translate("Conf", u"PHP", None))
        self.comboBox_tec.setItemText(6, QCoreApplication.translate("Conf", u"C#", None))
        self.comboBox_tec.setItemText(7, QCoreApplication.translate("Conf", u"C", None))
        self.comboBox_tec.setItemText(8, QCoreApplication.translate("Conf", u"Angular", None))
        self.comboBox_tec.setItemText(9, QCoreApplication.translate("Conf", u"CSS HTML", None))
        self.comboBox_tec.setItemText(10, QCoreApplication.translate("Conf", u"React", None))
        self.comboBox_tec.setItemText(11, QCoreApplication.translate("Conf", u"Ruby", None))
        self.comboBox_tec.setItemText(12, QCoreApplication.translate("Conf", u"Swift", None))
        self.comboBox_tec.setItemText(13, QCoreApplication.translate("Conf", u"Vue", None))
        self.comboBox_tec.setItemText(14, QCoreApplication.translate("Conf", u"C++", None))
        self.comboBox_tec.setItemText(15, QCoreApplication.translate("Conf", u"Nenhuma", None))

        self.btn_salvar.setText(QCoreApplication.translate("Conf", u"Salvar", None))
    # retranslateUi

