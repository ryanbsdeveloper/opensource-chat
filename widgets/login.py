# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(618, 508)
        Login.setMinimumSize(QSize(618, 500))
        Login.setMaximumSize(QSize(618, 508))
        icon = QIcon()
        icon.addFile(u":/icons/logo_chat.png", QSize(), QIcon.Normal, QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.verticalLayout = QVBoxLayout(Login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:white")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 11, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 117))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 3, 0, 0)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setPointSize(15)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:white")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setPointSize(11)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color:#5f6368")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_8)

        self.input_nome = QLineEdit(self.frame_3)
        self.input_nome.setObjectName(u"input_nome")
        self.input_nome.setMinimumSize(QSize(300, 0))
        font3 = QFont()
        font3.setPointSize(13)
        self.input_nome.setFont(font3)
        self.input_nome.setStyleSheet(u"padding:10px;color:white")

        self.verticalLayout_3.addWidget(self.input_nome, 0, Qt.AlignHCenter)

        self.erro_nome = QLabel(self.frame_3)
        self.erro_nome.setObjectName(u"erro_nome")
        font4 = QFont()
        font4.setPointSize(12)
        self.erro_nome.setFont(font4)
        self.erro_nome.setStyleSheet(u"color: rgb(237, 51, 59);")
        self.erro_nome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.erro_nome)


        self.verticalLayout_4.addWidget(self.frame_3, 0, Qt.AlignVCenter)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 6, -1, 0)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 24))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color:white")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3, 0, Qt.AlignVCenter)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.frame_5.setFont(font5)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButton_nodejs = QRadioButton(self.frame_5)
        self.radioButton_nodejs.setObjectName(u"radioButton_nodejs")
        self.radioButton_nodejs.setFont(font5)
        self.radioButton_nodejs.setStyleSheet(u"color:white")
        icon1 = QIcon()
        icon1.addFile(u":/icons/node", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_nodejs.setIcon(icon1)
        self.radioButton_nodejs.setIconSize(QSize(22, 24))

        self.gridLayout.addWidget(self.radioButton_nodejs, 3, 0, 1, 1)

        self.radioButton_web = QRadioButton(self.frame_5)
        self.radioButton_web.setObjectName(u"radioButton_web")
        self.radioButton_web.setFont(font5)
        self.radioButton_web.setStyleSheet(u"color:white")
        icon2 = QIcon()
        icon2.addFile(u":/icons/csshtml", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_web.setIcon(icon2)
        self.radioButton_web.setIconSize(QSize(29, 24))

        self.gridLayout.addWidget(self.radioButton_web, 4, 3, 1, 1)

        self.radioButton_kotlin = QRadioButton(self.frame_5)
        self.radioButton_kotlin.setObjectName(u"radioButton_kotlin")
        self.radioButton_kotlin.setFont(font5)
        self.radioButton_kotlin.setStyleSheet(u"color:white")
        icon3 = QIcon()
        icon3.addFile(u":/icons/kotlin", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_kotlin.setIcon(icon3)
        self.radioButton_kotlin.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.radioButton_kotlin, 0, 7, 1, 1)

        self.radioButton_argular = QRadioButton(self.frame_5)
        self.radioButton_argular.setObjectName(u"radioButton_argular")
        self.radioButton_argular.setFont(font5)
        self.radioButton_argular.setStyleSheet(u"color:white")
        icon4 = QIcon()
        icon4.addFile(u":/icons/angular", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_argular.setIcon(icon4)
        self.radioButton_argular.setIconSize(QSize(23, 26))

        self.gridLayout.addWidget(self.radioButton_argular, 4, 0, 1, 1)

        self.radioButton_nenhum = QRadioButton(self.frame_5)
        self.radioButton_nenhum.setObjectName(u"radioButton_nenhum")
        self.radioButton_nenhum.setFont(font5)
        self.radioButton_nenhum.setStyleSheet(u"color:white")
        icon5 = QIcon()
        icon5.addFile(u":/icons/nehum", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_nenhum.setIcon(icon5)
        self.radioButton_nenhum.setIconSize(QSize(27, 28))

        self.gridLayout.addWidget(self.radioButton_nenhum, 6, 7, 1, 1)

        self.radioButton_c = QRadioButton(self.frame_5)
        self.radioButton_c.setObjectName(u"radioButton_c")
        self.radioButton_c.setFont(font5)
        self.radioButton_c.setStyleSheet(u"color:white")
        icon6 = QIcon()
        icon6.addFile(u":/icons/c", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_c.setIcon(icon6)
        self.radioButton_c.setIconSize(QSize(23, 26))

        self.gridLayout.addWidget(self.radioButton_c, 3, 7, 1, 1)

        self.radioButton_java = QRadioButton(self.frame_5)
        self.radioButton_java.setObjectName(u"radioButton_java")
        self.radioButton_java.setFont(font5)
        self.radioButton_java.setStyleSheet(u"color:white")
        icon7 = QIcon()
        icon7.addFile(u":/icons/java", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_java.setIcon(icon7)
        self.radioButton_java.setIconSize(QSize(20, 26))

        self.gridLayout.addWidget(self.radioButton_java, 0, 3, 1, 1)

        self.radioButton_swift = QRadioButton(self.frame_5)
        self.radioButton_swift.setObjectName(u"radioButton_swift")
        self.radioButton_swift.setFont(font5)
        self.radioButton_swift.setStyleSheet(u"color:white")
        icon8 = QIcon()
        icon8.addFile(u":/icons/swift", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_swift.setIcon(icon8)
        self.radioButton_swift.setIconSize(QSize(23, 26))

        self.gridLayout.addWidget(self.radioButton_swift, 6, 0, 1, 1)

        self.radioButton_vue = QRadioButton(self.frame_5)
        self.radioButton_vue.setObjectName(u"radioButton_vue")
        self.radioButton_vue.setFont(font5)
        self.radioButton_vue.setStyleSheet(u"color:white")
        icon9 = QIcon()
        icon9.addFile(u":/icons/vue", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_vue.setIcon(icon9)
        self.radioButton_vue.setIconSize(QSize(23, 23))

        self.gridLayout.addWidget(self.radioButton_vue, 6, 3, 1, 1)

        self.radioButton_react = QRadioButton(self.frame_5)
        self.radioButton_react.setObjectName(u"radioButton_react")
        self.radioButton_react.setFont(font5)
        self.radioButton_react.setStyleSheet(u"color:white")
        icon10 = QIcon()
        icon10.addFile(u":/icons/react", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_react.setIcon(icon10)
        self.radioButton_react.setIconSize(QSize(23, 26))

        self.gridLayout.addWidget(self.radioButton_react, 4, 4, 1, 1)

        self.radioButton_python = QRadioButton(self.frame_5)
        self.radioButton_python.setObjectName(u"radioButton_python")
        self.radioButton_python.setFont(font5)
        self.radioButton_python.setStyleSheet(u"color:white")
        icon11 = QIcon()
        icon11.addFile(u":/icons/python", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_python.setIcon(icon11)
        self.radioButton_python.setIconSize(QSize(22, 22))

        self.gridLayout.addWidget(self.radioButton_python, 0, 0, 1, 1)

        self.radioButton_csharp = QRadioButton(self.frame_5)
        self.radioButton_csharp.setObjectName(u"radioButton_csharp")
        self.radioButton_csharp.setFont(font5)
        self.radioButton_csharp.setStyleSheet(u"color:white")
        icon12 = QIcon()
        icon12.addFile(u":/icons/c#", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_csharp.setIcon(icon12)
        self.radioButton_csharp.setIconSize(QSize(23, 26))

        self.gridLayout.addWidget(self.radioButton_csharp, 3, 4, 1, 1)

        self.radioButton_javascript = QRadioButton(self.frame_5)
        self.radioButton_javascript.setObjectName(u"radioButton_javascript")
        self.radioButton_javascript.setFont(font5)
        self.radioButton_javascript.setStyleSheet(u"color:white")
        icon13 = QIcon()
        icon13.addFile(u":/icons/js", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_javascript.setIcon(icon13)
        self.radioButton_javascript.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.radioButton_javascript, 0, 4, 1, 1)

        self.radioButton_php = QRadioButton(self.frame_5)
        self.radioButton_php.setObjectName(u"radioButton_php")
        self.radioButton_php.setFont(font5)
        self.radioButton_php.setStyleSheet(u"color:white")
        icon14 = QIcon()
        icon14.addFile(u":/icons/php", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_php.setIcon(icon14)
        self.radioButton_php.setIconSize(QSize(35, 30))

        self.gridLayout.addWidget(self.radioButton_php, 3, 3, 1, 1)

        self.radioButton_ruby = QRadioButton(self.frame_5)
        self.radioButton_ruby.setObjectName(u"radioButton_ruby")
        self.radioButton_ruby.setFont(font5)
        self.radioButton_ruby.setStyleSheet(u"color:white")
        icon15 = QIcon()
        icon15.addFile(u":/icons/ruby", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_ruby.setIcon(icon15)
        self.radioButton_ruby.setIconSize(QSize(22, 23))

        self.gridLayout.addWidget(self.radioButton_ruby, 4, 7, 1, 1)

        self.radioButton_cmais = QRadioButton(self.frame_5)
        self.radioButton_cmais.setObjectName(u"radioButton_cmais")
        self.radioButton_cmais.setFont(font5)
        self.radioButton_cmais.setStyleSheet(u"color:white")
        icon16 = QIcon()
        icon16.addFile(u":/icons/c++", QSize(), QIcon.Normal, QIcon.Off)
        self.radioButton_cmais.setIcon(icon16)
        self.radioButton_cmais.setIconSize(QSize(23, 29))

        self.gridLayout.addWidget(self.radioButton_cmais, 6, 4, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setWeight(50)
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"color:#5f6368")

        self.horizontalLayout.addWidget(self.label_6, 0, Qt.AlignLeft)

        self.tec_escolhida = QLabel(self.frame_7)
        self.tec_escolhida.setObjectName(u"tec_escolhida")
        self.tec_escolhida.setFont(font)
        self.tec_escolhida.setStyleSheet(u"color:white")

        self.horizontalLayout.addWidget(self.tec_escolhida)


        self.verticalLayout_5.addWidget(self.frame_7, 0, Qt.AlignLeft)

        self.erro_tecnologia = QLabel(self.frame_4)
        self.erro_tecnologia.setObjectName(u"erro_tecnologia")
        self.erro_tecnologia.setFont(font4)
        self.erro_tecnologia.setStyleSheet(u"color: rgb(237, 51, 59);")
        self.erro_tecnologia.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.erro_tecnologia)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_comecar = QPushButton(self.frame_6)
        self.btn_comecar.setObjectName(u"btn_comecar")
        self.btn_comecar.setMinimumSize(QSize(150, 0))
        self.btn_comecar.setFont(font)
        self.btn_comecar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_comecar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 53, 211);\n"
"border:0;\n"
"padding:10px;\n"
"border-radius:10px")

        self.verticalLayout_6.addWidget(self.btn_comecar)


        self.verticalLayout_2.addWidget(self.frame_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.label.setText(QCoreApplication.translate("Login", u"Configura\u00e7\u00e3o inicial", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Nome de desenvolvedor", None))
        self.label_8.setText(QCoreApplication.translate("Login", u"Esse nome n\u00e3o poder\u00e1 ser atualizado posteriormente", None))
        self.erro_nome.setText(QCoreApplication.translate("Login", u"Nome em uso", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"Tecnologia favorita", None))
        self.radioButton_nodejs.setText(QCoreApplication.translate("Login", u"NodeJS", None))
        self.radioButton_web.setText(QCoreApplication.translate("Login", u"CSS HTML", None))
        self.radioButton_kotlin.setText(QCoreApplication.translate("Login", u"Kotlin", None))
        self.radioButton_argular.setText(QCoreApplication.translate("Login", u"Angular", None))
        self.radioButton_nenhum.setText(QCoreApplication.translate("Login", u"Nenhuma", None))
        self.radioButton_c.setText(QCoreApplication.translate("Login", u"C", None))
        self.radioButton_java.setText(QCoreApplication.translate("Login", u"Java", None))
        self.radioButton_swift.setText(QCoreApplication.translate("Login", u"Swift", None))
        self.radioButton_vue.setText(QCoreApplication.translate("Login", u"Vue", None))
        self.radioButton_react.setText(QCoreApplication.translate("Login", u"React", None))
        self.radioButton_python.setText(QCoreApplication.translate("Login", u"Python", None))
        self.radioButton_csharp.setText(QCoreApplication.translate("Login", u"C#", None))
        self.radioButton_javascript.setText(QCoreApplication.translate("Login", u"JavaScript", None))
        self.radioButton_php.setText(QCoreApplication.translate("Login", u"PHP", None))
        self.radioButton_ruby.setText(QCoreApplication.translate("Login", u"Ruby", None))
        self.radioButton_cmais.setText(QCoreApplication.translate("Login", u"C++", None))
        self.label_6.setText(QCoreApplication.translate("Login", u"Tecnologia escolhida:", None))
        self.tec_escolhida.setText(QCoreApplication.translate("Login", u"TextLabel", None))
        self.erro_tecnologia.setText(QCoreApplication.translate("Login", u"A escolha \u00e9 obrigat\u00f3ria", None))
        self.btn_comecar.setText(QCoreApplication.translate("Login", u"Come\u00e7ar", None))
    # retranslateUi

