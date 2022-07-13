from http.client import FORBIDDEN
import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import QFont, QIcon, QPixmap, QCursor, QPainter
from PySide2.QtCore import *
from sqlalchemy import true
from widgets.chat import Ui_Chat
from widgets.conf import Ui_Conf
from widgets.login import Ui_Login
from modules.databases import database_aws, database_local
from modules.utils import main

import resources.resources


class Conf(QDialog, Ui_Conf):
    def __init__(self, parent):
        super(Conf, self).__init__(parent)
        self.setupUi(self)
        self.btn_apagar_conversas.clicked.connect(self.del_messages)

    def del_messages(self):
        database_local.del_messages()
        self.close()
        while self.parent().verticalLayout_7.count():
            item = self.parent().verticalLayout_7.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clearLayout(item.layout())


class Login(QDialog, Ui_Login):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.boxElements = self.groupBox.children()

        timer = QTimer(self)
        timer.timeout.connect(self.tecnologia)
        timer.start(500)

        # Button
        self.btn_comecar.clicked.connect(self.developer)

    def tecnologia(self):
        radioButtons = [
            elem for elem in self.boxElements if isinstance(elem, QRadioButton)]
        for rb in radioButtons:
            if rb.isChecked():
                icon1 = QIcon()
                icon1.addFile(f":/icons/{rb.text().lower()}",
                              QSize(), QIcon.Normal, QIcon.Off)
                self.tec_escolhida.setIcon(icon1)
                self.tec_escolhida.setText(rb.text())
                return rb.text()

    def developer(self):
        nome = self.input_nome.text()
        users = database_aws.list_users()
        tec_escolhida = self.tecnologia()

        if len(nome) > 15:
            self.erro_nome.setText('Nome muito extenso.')

        elif len(nome) < 4:
            self.erro_nome.setText('Nome muito curto.')

        elif nome in users:
            self.erro_nome.setText('Nome já está em uso.')

        elif not tec_escolhida:
            self.erro_tecnologia.setText('A escolha é obrigatória.')

        else:
            database_local.add_user_local(nome, tec_escolhida)
            database_aws.add_user(nome, tec_escolhida, True, 0, True)
            self.btn_comecar.setDisabled(True)
            self.input_nome.setText('')
            self.close()
            # Chat window
            self.chat = Chat()
            self.chat.show()


class Chat(QMainWindow, Ui_Chat):
    def __init__(self, parent=None):
        super(Chat, self).__init__(parent)
        self.setupUi(self)
        self.btn_msg.clicked.connect(self.add_my_msg)
        self.scrollArea.verticalScrollBar().rangeChanged.connect(self.ResizeScroll)
        self.input_msg.returnPressed.connect(self.btn_msg.click)
        # Initial
        scroll = self.scrollArea.horizontalScrollBar()
        scroll.setDisabled(True)
        self.check_net()
        self.developer_log()
        self.messages()

        # Others windows
        self.conf = Conf(self)
        self.btn_config.clicked.connect(self.open_conf)

        # Hide members
        self.btn_ocultar_mostrar.clicked.connect(self.animation_members)

    # Users community
    def users(self):
        users = database_aws.list_users(True)

        for user in users:
            if user.nome not in database_local.list_users():
                database_local.add_users(user.nome, user.tecnologia)
                frame = QFrame(self.scrollAreaWidgetContents)
                frame.setObjectName(u"frame_16")
                frame.setStyleSheet(u"border-bottom:1px solid #5f6368;")
                frame.setFrameShape(QFrame.NoFrame)
                frame.setFrameShadow(QFrame.Raised)
                horizontalLayout = QHBoxLayout(frame)
                horizontalLayout.setSpacing(0)
                horizontalLayout.setObjectName(u"horizontalLayout_11")
                horizontalLayout.setContentsMargins(0, 0, -1, 0)
                frame_2 = QFrame(frame)
                frame_2.setObjectName(u"frame_17")
                frame_2.setFrameShape(QFrame.NoFrame)
                frame_2.setFrameShadow(QFrame.Raised)

                horizontalLayout_12 = QHBoxLayout(frame_2)
                horizontalLayout_12.setObjectName(u"horizontalLayout_12")

                font10 = QFont()
                font10.setPointSize(13)
                font10.setBold(True)
                label_15 = QLabel(frame_2)
                label_15.setObjectName(u"label_15")
                label_15.setFont(font10)
                label_15.setStyleSheet(u"border:0; color:white")
                label_15.setText('Developer:')
                horizontalLayout_12.addWidget(label_15)

                label_10 = QLabel(frame_2)
                label_10.setObjectName(u"label_10")
                font12 = QFont()
                font12.setPointSize(14)
                font12.setBold(True)
                font12.setWeight(75)
                label_10.setFont(font12)
                label_10.setStyleSheet(u"color:#5f6368; border:0")
                label_10.setText(f'{user.nome}')

                horizontalLayout_12.addWidget(label_10)

                label_14 = QLabel(frame_2)
                label_14.setObjectName(u"label_14")
                label_14.setMaximumSize(QSize(25, 22))
                label_14.setStyleSheet(u"border:0")
                label_14.setPixmap(
                    QPixmap(f":/icons/{user.tecnologia.lower()}"))
                label_14.setScaledContents(True)

                horizontalLayout_12.addWidget(label_14)
                horizontalLayout.addWidget(frame_2, 0, Qt.AlignLeft)
                self.verticalLayout_8.addWidget(frame)
            else:
                frame = QFrame(self.scrollAreaWidgetContents)
                frame.setObjectName(u"frame_16")
                frame.setStyleSheet(u"border-bottom:1px solid #5f6368;")
                frame.setFrameShape(QFrame.NoFrame)
                frame.setFrameShadow(QFrame.Raised)
                horizontalLayout = QHBoxLayout(frame)
                horizontalLayout.setSpacing(0)
                horizontalLayout.setObjectName(u"horizontalLayout_11")
                horizontalLayout.setContentsMargins(0, 0, -1, 0)
                frame_2 = QFrame(frame)
                frame_2.setObjectName(u"frame_17")
                frame_2.setFrameShape(QFrame.NoFrame)
                frame_2.setFrameShadow(QFrame.Raised)

                horizontalLayout_12 = QHBoxLayout(frame_2)
                horizontalLayout_12.setObjectName(u"horizontalLayout_12")

                font10 = QFont()
                font10.setPointSize(13)
                font10.setBold(True)
                label_15 = QLabel(frame_2)
                label_15.setObjectName(u"label_15")
                label_15.setFont(font10)
                label_15.setStyleSheet(u"border:0; color:white")
                label_15.setText('Developer:')
                horizontalLayout_12.addWidget(label_15)

                label_10 = QLabel(frame_2)
                label_10.setObjectName(u"label_10")
                font12 = QFont()
                font12.setPointSize(14)
                font12.setBold(True)
                font12.setWeight(75)
                label_10.setFont(font12)
                label_10.setStyleSheet(u"color:#5f6368; border:0")
                label_10.setText(f'{user.nome}')

                horizontalLayout_12.addWidget(label_10)

                label_14 = QLabel(frame_2)
                label_14.setObjectName(u"label_14")
                label_14.setMaximumSize(QSize(25, 22))
                label_14.setStyleSheet(u"border:0")
                label_14.setPixmap(
                    QPixmap(f":/icons/{user.tecnologia.lower()}"))
                label_14.setScaledContents(True)

                horizontalLayout_12.addWidget(label_14)
                horizontalLayout.addWidget(frame_2, 0, Qt.AlignLeft)
                self.verticalLayout_8.addWidget(frame)

    # Developer log
    def developer_log(self):
        nome = database_local.is_user(True).nome
        tecnologia = database_local.is_user(True).tecnologia
        icon1 = QIcon()
        icon1.addFile(f":/icons/{tecnologia.lower()}",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.developer.setText(nome)
        self.developer.setIcon(icon1)

    # Add mensages
    def add_my_msg(self):
        msg = self.input_msg.text()

        frame = QFrame()
        frame.setObjectName(u"frame_6436")
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Raised)
        frame.setMaximumSize(QSize(16777215, 70))

        verticalLayout = QVBoxLayout(frame)
        verticalLayout.setSpacing(0)
        verticalLayout.setObjectName(u"verticalLayout_42313")
        verticalLayout.setContentsMargins(-1, 0, -1, 0)
        verticalLayout.setAlignment(Qt.AlignRight)

        font8 = QFont()
        font8.setPointSize(15)
        label = QLabel()
        label.setObjectName(u"label_981")
        label.setMaximumSize(QSize(16777215, 40))
        label.setFont(font8)
        label.setStyleSheet(u"padding:5px;\n"
                            "background:#34449e;color:white")
        label.setScaledContents(True)
        label.setWordWrap(False)
        label.setMargin(0)

        font8 = QFont()
        font8.setPointSize(11)
        label2 = QLabel()
        label2.setObjectName(u"label_981")
        label2.setMaximumSize(QSize(16777215, 40))
        label2.setFont(font8)
        label2.setStyleSheet(u"color:#5f6368")
        label2.setScaledContents(True)
        label2.setWordWrap(True)
        label2.setMargin(0)
        label2.setText(main.hour())
        label2.setAlignment(Qt.AlignRight)

        if msg:
            label.setText(QCoreApplication.translate(
                "MainWindow", f"{msg}", None))
            verticalLayout.addWidget(label)
            verticalLayout.addWidget(label2)

            self.verticalLayout_7.addWidget(frame)
            self.input_msg.setText('')

            # add db
            user = database_local.is_user(True)
            database_local.add_messages(
                msg, main.hour(), user.nome, user.tecnologia)

    # saved messages
    def messages(self):
        messages = database_local.list_messages()
        user = database_local.is_user(True)

        for message in messages:
            if user.nome == message.nome:
                frame = QFrame()
                frame.setObjectName(u"frame_6436")
                frame.setFrameShape(QFrame.NoFrame)
                frame.setFrameShadow(QFrame.Raised)
                frame.setMaximumSize(QSize(16777215, 70))

                verticalLayout = QVBoxLayout(frame)
                verticalLayout.setSpacing(0)
                verticalLayout.setObjectName(u"verticalLayout_42313")
                verticalLayout.setContentsMargins(-1, 0, -1, 0)
                verticalLayout.setAlignment(Qt.AlignRight)

                font8 = QFont()
                font8.setPointSize(15)

                label = QLabel()
                label.setObjectName(u"label_981")
                label.setMaximumSize(QSize(16777215, 40))
                label.setFont(font8)
                label.setStyleSheet(u"padding:5px;\n"
                                    "background:#34449e;color:white")
                label.setScaledContents(True)
                label.setWordWrap(True)
                label.setMargin(0)
                label.setText(QCoreApplication.translate(
                    "MainWindow", f"{message.texto}", None))

                verticalLayout.addWidget(label)

                font8 = QFont()
                font8.setPointSize(11)

                label2 = QLabel()
                label2.setObjectName(u"label_981")
                label2.setMaximumSize(QSize(16777215, 40))
                label2.setFont(font8)
                label2.setStyleSheet(u"color:#5f6368")
                label2.setScaledContents(True)
                label2.setWordWrap(True)
                label2.setMargin(0)
                label2.setText(message.hora)
                label2.setAlignment(Qt.AlignRight)

                verticalLayout.addWidget(label2)
                self.verticalLayout_7.addWidget(frame)
            else:
                frame_11 = QFrame()
                frame_11.setObjectName(u"frame_11")
                frame_11.setMaximumSize(QSize(16777215, 80))
                frame_11.setFrameShape(QFrame.NoFrame)
                frame_11.setFrameShadow(QFrame.Raised)
                verticalLayout_5 = QVBoxLayout(frame_11)
                verticalLayout_5.setSpacing(2)
                verticalLayout_5.setObjectName(u"verticalLayout_5")
                verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
                frame_14 = QFrame(frame_11)
                frame_14.setObjectName(u"frame_14")
                frame_14.setMaximumSize(QSize(16777215, 30))
                frame_14.setFrameShape(QFrame.NoFrame)
                frame_14.setFrameShadow(QFrame.Raised)
                horizontalLayout_10 = QHBoxLayout(frame_14)
                horizontalLayout_10.setSpacing(2)
                horizontalLayout_10.setObjectName(u"horizontalLayout_10")
                horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

                verticalLayout_5.addWidget(frame_14, 0, Qt.AlignLeft)
                font4 = QFont()
                font4.setPointSize(16)
                font4.setBold(False)
                font4.setWeight(50)
                nome_msg = QPushButton(frame_11)
                nome_msg.setObjectName(u"nome_msg")
                nome_msg.setFont(font4)
                nome_msg.setLayoutDirection(Qt.RightToLeft)
                nome_msg.setStyleSheet(u"color:#5f6368;border:0;outline:0")
                icon4 = QIcon()
                icon4.addFile(f":/icons/{message.tecnologia.lower()}", QSize(), QIcon.Normal, QIcon.Off)
                nome_msg.setIcon(icon4)
                nome_msg.setIconSize(QSize(28, 24))
                nome_msg.setText(f"{message.nome}")

                verticalLayout_5.addWidget(nome_msg, 0, Qt.AlignRight)

                label_13 = QLabel(frame_11)
                label_13.setObjectName(u"label_13")
                label_13.setMinimumSize(QSize(0, 0))
                label_13.setMaximumSize(QSize(16777215, 40))
                font11 = QFont()
                font11.setPointSize(15)
                label_13.setFont(font11)
                label_13.setStyleSheet(u"padding:5px;\n"
        "color:white;\n"
        "background-color: rgb(60, 60, 60);")
                label_13.setScaledContents(True)
                label_13.setWordWrap(False)
                label_13.setMargin(0)
                label_13.setText(message.texto)

                verticalLayout_5.addWidget(label_13, 0, Qt.AlignLeft)

                label_10 = QLabel(frame_11)
                label_10.setObjectName(u"label_10")
                label_10.setStyleSheet(u"color:#5f6368")
                label_10.setText(message.hora)

                verticalLayout_5.addWidget(label_10)

                self.verticalLayout_7.addWidget(frame_11)

    def ResizeScroll(self, min, maxi):
        self.scrollArea.verticalScrollBar().setValue(maxi)

    # Open others windows
    def open_conf(self):
        self.conf.exec_()

    # Animation view members
    def animation_members(self):
        width = self.frame_12.width()

        if width < 200:
            extend_width = 390
            icon3 = QIcon()
            icon3.addFile(u":/icons/eye-slash-solid.svg",
                          QSize(), QIcon.Normal, QIcon.Off)
            self.btn_ocultar_mostrar.setIcon(icon3)
            self.btn_ocultar_mostrar.setText('Ocultar membros')

        else:
            extend_width = 0
            icon3 = QIcon()
            icon3.addFile(u":/icons/eye-solid.svg",
                          QSize(), QIcon.Normal, QIcon.Off)
            self.btn_ocultar_mostrar.setIcon(icon3)
            self.btn_ocultar_mostrar.setText('Mostrar membros')

        self.animation = QPropertyAnimation(self.frame_12, b'maximumWidth')
        self.animation.setDuration(200)
        self.animation.setStartValue(width)
        self.animation.setEndValue(extend_width)
        self.animation.start()

    # check net
    def check_net(self):
        if not main.access_internet():
            self.sem_internet.show()
            self.btn_msg.setDisabled(True)
            self.input_msg.setDisabled(True)
        else:
            self.users()
            self.sem_internet.hide()
            self.btn_msg.setDisabled(False)
            self.input_msg.setDisabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if database_local.is_user():
        window = Chat()
    else:
        window = Login()
    window.show()
    sys.exit(app.exec_())
