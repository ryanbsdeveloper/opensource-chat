from re import X
import sys, json, os, threading
from time import sleep
from PySide2.QtWidgets import *
from PySide2.QtGui import QFont, QIcon, QPixmap, QColor
from PySide2 import Qt
from PySide2.QtCore import *
from sqlalchemy import true
from widgets.chat import Ui_Chat
from widgets.conf import Ui_Conf
from widgets.login import Ui_Login
from widgets.carregamento import Ui_SplashScreen
from modules.databases import database_aws, database_local
from modules.chat import dev, servidor
from modules.utils import main

import resources.resources

class Conf(QDialog, Ui_Conf):
    def __init__(self, parent):
        super(Conf, self).__init__(parent)
        self.setupUi(self)
        self.btn_apagar_conversas.clicked.connect(self.del_messages)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.setGraphicsEffect(self.shadow)

        # buttons
        self.btn_feedback.clicked.connect(self.send_feedback)

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

    def send_feedback(self):
        texto = self.texto_feedback.toPlainText()
        user = database_local.is_user(True)
        if len(texto) > 1999 or len(texto) == 0 :
            self.saida.setStyleSheet('color:rgb(246, 97, 81);')
            self.saida.setText('Escreva entre 1 e 2000 caracteres.')
            return
        try:
            database_aws.add_feedback(user.nome, texto)
        except:
            self.saida.setStyleSheet('color:rgb(246, 97, 81);')
            self.saida.setText('Erro ao enviar feedback.')
        else:
            self.saida.setText('Feedback enviado com sucesso.')
            self.texto_feedback.setPlainText('')


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


class ThreadMessages(QThread):
    sig = Signal()
    def __init__(self, mw=None, parent=None):
        super().__init__(parent)

    def run(self):
        try:
            t1 = threading.Thread(target=servidor.Servidor().consuming)
            t1.start()
        except:
            assert 'Erro inesperado ao tentar se conectar ao servidor, reinicie o aplicativo.'
        while True:
            BASE_DIR = os.path.dirname(__file__)
            with open(f'{BASE_DIR}/modules/chat/mensagens.txt', 'r+') as file:
                linha = file.readline()
            if linha:
                self.sig.emit()
                #time.sleep(1)
                QThread.msleep(1000)


class Chat(QMainWindow, Ui_Chat):
    def __init__(self, parent=None):
        super(Chat, self).__init__(parent)
        self.setupUi(self)
        self.btn_msg.clicked.connect(self.add_my_msg)
        self.scrollArea.verticalScrollBar().rangeChanged.connect(self.ResizeScroll)
        self.input_msg.returnPressed.connect(self.btn_msg.click)

        # notifications
        global window_obj
        window_obj = self
        action_hide.triggered.connect(lambda: self.hide())
        action_show.triggered.connect(lambda: self.showNormal())

        # Initial
        self.ss15 = 10
        scroll = self.scrollArea.horizontalScrollBar()
        scroll.setDisabled(True)
        self.check_net()
        self.list_members()
        self.developer_log()
        self.messages()

        # Time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_net)
        self.timer.start(1500)

        # Server rabbit
        try:
            self.t = ThreadMessages(self)
            self.t.start()
            self.t.sig.connect(self.chat_messages) 
        except:  
            self.animation_net(True)
            self.animation_members(True)

            self.btn_msg.setDisabled(True)
            self.btn_ocultar_mostrar.setDisabled(True)
            self.sem_internet.setText('Erro inesperado ao tentar se conectar ao servidor, reinicie o aplicativo.')
            self.input_msg.setDisabled(True)
            self.timer.stop()

         # Others windows
        self.conf = Conf(self)
        self.btn_config.clicked.connect(self.open_conf)
        
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.hide_segundos)

        # Hide members
        self.btn_ocultar_mostrar.clicked.connect(self.animation_members)

    # users community
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

    # developer logged
    def developer_log(self):
        nome = database_local.is_user(True).nome
        tecnologia = database_local.is_user(True).tecnologia
        icon1 = QIcon()
        icon1.addFile(f":/icons/{tecnologia.lower()}",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.developer.setText(nome)
        self.developer.setIcon(icon1)

    # add my mensages
    def add_my_msg(self):
        self.ss15 = 10
        msg = self.input_msg.text()

        frame_21 = QFrame()
        frame_21.setObjectName(u"frame_21")
        frame_21.setFrameShape(QFrame.NoFrame)
        frame_21.setFrameShadow(QFrame.Raised)
        horizontalLayout_14 = QHBoxLayout(frame_21)
        horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        frame_22 = QFrame(frame_21)
        frame_22.setObjectName(u"frame_22")
        frame_22.setFrameShape(QFrame.NoFrame)
        frame_22.setFrameShadow(QFrame.Raised)
        verticalLayout = QVBoxLayout(frame_22)
        verticalLayout.setSpacing(0)
        verticalLayout.setObjectName(u"verticalLayout_9")
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        label_1 = QLabel(frame_22)
        label_1.setObjectName(u"label_15")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label_1.sizePolicy().hasHeightForWidth())
        label_1.setSizePolicy(sizePolicy)
        
        # width label
        width = main.width_label(msg)
        label_1.setMaximumSize(QSize(width, 16777215))
        font9 = QFont()
        font9.setFamily(u"Sans Serif")
        font9.setPointSize(14)
        label_1.setFont(font9)
        label_1.setLayoutDirection(Qt.RightToLeft)
        label_1.setStyleSheet(u"\n"
                    "background-color: rgb(23, 22, 93);color:white")
        label_1.setAlignment(Qt.AlignLeft)
        label_1.setWordWrap(True)
        label_1.setMargin(5)
        label_1.setText(msg)


        label_2 = QLabel(frame_22)
        label_2.setObjectName(u"label_13")
        label_2.setMinimumSize(QSize(0, 0))
        label_2.setStyleSheet(u"color:#5f6368")
        label_2.setText(main.hour())
        label_2.setAlignment(Qt.AlignRight)



        horizontalLayout_14.addWidget(frame_22)

        if msg:
            if len(msg) < 300:

                label_1.setText(msg)
                verticalLayout.addWidget(label_1)
                verticalLayout.addWidget(label_2)

                self.verticalLayout_7.addWidget(frame_21)
                self.input_msg.setText('')

                # add db and send
                user = database_local.is_user(True)
                database_local.add_messages(
                    msg, main.hour(), user.nome, user.tecnologia)
                
                self.developer_send(user.nome, user.tecnologia, msg, main.hour())
                
                # next msg
                self.hide_segundos()
            else:
                self.saida_msg.setText('Mensagem muito grande, maximo de 300 caracteres.')
                self.saida_msg.setStyleSheet('color:rgb(246, 97, 81);')

    # time next message
    def hide_segundos(self):
        self.timer2.start(1000)
        self.saida_msg.setText(f'{self.ss15} segundos para proxima mensagem.')
        self.saida_msg.setStyleSheet('color:#5f6368')

        if self.ss15 == 0:
            self.timer2.stop()
            self.input_msg.setDisabled(False)
            self.btn_msg.setDisabled(False)     
            self.iconsaida.setPixmap(QPixmap(u":/icons/angles-d.svg"))
            self.saida_msg.setText('')
            self.ss15 = 10
        else:
            self.input_msg.setDisabled(True)
            self.iconsaida.setPixmap(QPixmap(u":/icons/angles-right-solid.svg"))
            self.btn_msg.setDisabled(True)
            self.developer.click()

        self.ss15 = self.ss15 - 1

    # saved messages
    def messages(self):
        messages = database_local.list_messages()
        user = database_local.is_user(True)

        for message in messages:
            if user.nome == message.nome:
                frame_21 = QFrame()
                frame_21.setObjectName(u"frame_21")
                frame_21.setFrameShape(QFrame.NoFrame)
                frame_21.setFrameShadow(QFrame.Raised)
                horizontalLayout_14 = QHBoxLayout(frame_21)
                horizontalLayout_14.setObjectName(u"horizontalLayout_14")
                frame_22 = QFrame(frame_21)
                frame_22.setObjectName(u"frame_22")
                frame_22.setFrameShape(QFrame.NoFrame)
                frame_22.setFrameShadow(QFrame.Raised)
                verticalLayout_9 = QVBoxLayout(frame_22)
                verticalLayout_9.setSpacing(0)
                verticalLayout_9.setObjectName(u"verticalLayout_9")
                verticalLayout_9.setContentsMargins(0, 0, 0, 0)
                label_15 = QLabel(frame_22)
                label_15.setObjectName(u"label_15")
                sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(label_15.sizePolicy().hasHeightForWidth())
                label_15.setSizePolicy(sizePolicy)
                
                # width label
                width = main.width_label(message.texto)
                label_15.setMaximumSize(QSize(width, 16777215))
                font9 = QFont()
                font9.setFamily(u"Sans Serif")
                font9.setPointSize(14)
                label_15.setFont(font9)
                label_15.setLayoutDirection(Qt.RightToLeft)
                label_15.setStyleSheet(u"\n"
                            "background-color: rgb(23, 22, 93);color:white")
                label_15.setAlignment(Qt.AlignLeft)
                label_15.setWordWrap(True)
                label_15.setMargin(5)
                label_15.setText(message.texto)

                verticalLayout_9.addWidget(label_15)

                label_13 = QLabel(frame_22)
                label_13.setObjectName(u"label_13")
                label_13.setMinimumSize(QSize(0, 0))
                label_13.setStyleSheet(u"color:#5f6368")
                label_13.setText(message.hora)
                label_13.setAlignment(Qt.AlignRight)

                verticalLayout_9.addWidget(label_13)


                horizontalLayout_14.addWidget(frame_22)

                self.verticalLayout_7.addWidget(frame_21)

            elif message.nome == 'sistema':
                frame_20 = QFrame()
                frame_20.setObjectName(u"frame_20")
                frame_20.setFrameShape(QFrame.NoFrame)
                frame_20.setFrameShadow(QFrame.Raised)
                verticalLayout_9 = QVBoxLayout(frame_20)
                verticalLayout_9.setSpacing(0)
                verticalLayout_9.setObjectName(u"verticalLayout_9")
                verticalLayout_9.setContentsMargins(-1, 0, -1, 0)

                label_21 = QLabel(frame_20)
                # width label
                width = main.width_label(message.texto)
                label_21.setObjectName(u"label_21")
                label_21.setMaximumSize(QSize(width, 1000))
                font10 = QFont()
                font10.setFamily(u"Sans Serif")
                font10.setPointSize(14)
                font10.setBold(False)
                font10.setWeight(50)
                label_21.setFont(font10)
                label_21.setStyleSheet(
        "color: white;\n"
        "background-color: #34449e;")
                label_21.setScaledContents(True)
                label_21.setWordWrap(False)
                label_21.setMargin(5)
                label_21.setText(message.texto)

                verticalLayout_9.addWidget(label_21, 0, Qt.AlignHCenter)
                self.verticalLayout_7.addWidget(frame_20)
                
            elif message.nome == 'ryanbs':
                frame_11 = QFrame()
                frame_11.setObjectName(u"frame_11")
                frame_11.setMaximumSize(QSize(16777215, 1000))
                frame_11.setFrameShape(QFrame.NoFrame)
                frame_11.setFrameShadow(QFrame.Raised)
                verticalLayout_5 = QVBoxLayout(frame_11)
                verticalLayout_5.setSpacing(2)
                verticalLayout_5.setObjectName(u"verticalLayout_5")
                verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
                frame_14 = QFrame(frame_11)
                frame_14.setObjectName(u"frame_14")
                frame_14.setMaximumSize(QSize(16777215, 1000))
                frame_14.setFrameShape(QFrame.NoFrame)
                frame_14.setFrameShadow(QFrame.Raised)
                horizontalLayout_10 = QHBoxLayout(frame_14)
                horizontalLayout_10.setSpacing(2)
                horizontalLayout_10.setObjectName(u"horizontalLayout_10")
                horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

                verticalLayout_5.addWidget(frame_14)
                font4 = QFont()
                font4.setPointSize(16)
                font4.setBold(True)
                nome_msg = QPushButton(frame_11)
                nome_msg.setObjectName(u"nome_msg")
                nome_msg.setFont(font4)
                nome_msg.setLayoutDirection(Qt.RightToLeft)
                nome_msg.setStyleSheet(u"color: rgb(206, 153, 25);;border:0;outline:0")
                icon4 = QIcon()
                icon4.addFile(f":/icons/{message.tecnologia.lower()}", QSize(), QIcon.Normal, QIcon.Off)
                nome_msg.setIcon(icon4)
                nome_msg.setIconSize(QSize(28, 24))
                nome_msg.setText(f"{message.nome}")

                verticalLayout_5.addWidget(nome_msg, 0, Qt.AlignRight)

                label_13 = QLabel(frame_11)

                # width label
                width = main.width_label(message.texto)
                label_13.setObjectName(u"label_13")
                label_13.setMinimumSize(QSize(0, 0))
                label_13.setMaximumSize(QSize(width, 1000))
                font11 = QFont()
                font11.setFamily(u"Sans Serif")
                font11.setPointSize(14)
                label_13.setFont(font11)
                label_13.setStyleSheet(
        "color:white;\n"
        "background-color: rgb(60, 60, 60);")
                label_13.setScaledContents(True)
                label_13.setWordWrap(True)
                label_13.setMargin(5)

                label_13.setText(message.texto)

                verticalLayout_5.addWidget(label_13)

                label_10 = QLabel(frame_11)
                label_10.setObjectName(u"label_10")
                label_10.setStyleSheet(u"color:#5f6368")
                label_10.setText(message.hora)

                verticalLayout_5.addWidget(label_10)

                self.verticalLayout_7.addWidget(frame_11)

            else:
                frame_11 = QFrame()
                frame_11.setObjectName(u"frame_11")
                frame_11.setMaximumSize(QSize(16777215, 1000))
                frame_11.setFrameShape(QFrame.NoFrame)
                frame_11.setFrameShadow(QFrame.Raised)
                verticalLayout_5 = QVBoxLayout(frame_11)
                verticalLayout_5.setSpacing(2)
                verticalLayout_5.setObjectName(u"verticalLayout_5")
                verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
                frame_14 = QFrame(frame_11)
                frame_14.setObjectName(u"frame_14")
                frame_14.setMaximumSize(QSize(16777215, 1000))
                frame_14.setFrameShape(QFrame.NoFrame)
                frame_14.setFrameShadow(QFrame.Raised)
                horizontalLayout_10 = QHBoxLayout(frame_14)
                horizontalLayout_10.setSpacing(2)
                horizontalLayout_10.setObjectName(u"horizontalLayout_10")
                horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

                verticalLayout_5.addWidget(frame_14)
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

                # width label
                width = main.width_label(message.texto)
                label_13.setMaximumSize(QSize(width, 1000))
                font11 = QFont()
                font11.setFamily(u"Sans Serif")
                font11.setPointSize(14)
                label_13.setFont(font11)
                label_13.setStyleSheet(
        "color:white;\n"
        "background-color: rgb(60, 60, 60);")
                label_13.setScaledContents(True)
                label_13.setWordWrap(True)
                label_13.setMargin(5)
                label_13.setText(message.texto)

                verticalLayout_5.addWidget(label_13)

                label_10 = QLabel(frame_11)
                label_10.setObjectName(u"label_10")
                label_10.setStyleSheet(u"color:#5f6368")
                label_10.setText(message.hora)

                verticalLayout_5.addWidget(label_10)

                self.verticalLayout_7.addWidget(frame_11)

    # scroll intelligent
    def ResizeScroll(self, min, maxi):
        self.scrollArea.verticalScrollBar().setValue(maxi)

    # Open others windows
    def open_conf(self):
        self.conf.show()

    # animation view members
    def animation_members(self, fechado=False):
        width = self.frame_12.width()

        if width == 350 or fechado:
            extend_width = 0
            icon3 = QIcon()
            icon3.addFile(u":/icons/eye-solid.svg",
                          QSize(), QIcon.Normal, QIcon.Off)
            self.btn_ocultar_mostrar.setIcon(icon3)
            self.btn_ocultar_mostrar.setText('Mostrar membros')
        else:
            extend_width = 350
            icon3 = QIcon()
            icon3.addFile(u":/icons/eye-slash-solid.svg",
                          QSize(), QIcon.Normal, QIcon.Off)
            self.btn_ocultar_mostrar.setIcon(icon3)
            self.btn_ocultar_mostrar.setText('Ocultar membros')

        self.animation = QPropertyAnimation(self.frame_12, b'maximumWidth')
        self.animation.setDuration(150)
        self.animation.setStartValue(width)
        self.animation.setEndValue(extend_width)
        self.animation.start()

    # animation view net
    def animation_net(self, acesso):
        if acesso:
            self.sem_internet.setStyleSheet(u"background-color: rgb(246, 97, 81);\n"
    "color:white;\n"
    "border-radius:5px")        
        else:
            self.sem_internet.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
            "color:rgba(0, 0, 0, 0);\n"
            "border-radius:5px")
    
    # check net
    def check_net(self):
        if not main.access_internet():
            self.animation_net(True)
            self.animation_members(True)

            self.btn_msg.setDisabled(True)
            self.btn_ocultar_mostrar.setDisabled(True)
            self.input_msg.setDisabled(True)
        else:
            self.animation_net(False)
            self.btn_ocultar_mostrar.setDisabled(False)
            self.btn_msg.setDisabled(False)
            self.input_msg.setDisabled(False)

    # members of community 
    def list_members(self):
        if main.access_internet():
            self.users()
        else:
            font2 = QFont()
            font2.setPointSize(10)
            font2.setBold(True)
            font2.setWeight(75)
            self.label_4.hide()
            self.label_2.setFont(font2)
            self.label_2.setStyleSheet('color: rgb(246, 97, 81)')
            self.label_2.setText('Para mostrar membros, reinicie o aplicativo.')
    
    # messages received
    def chat_messages(self):
        BASE_DIR = os.path.dirname(__file__)
        with open(f'{BASE_DIR}/modules/chat/mensagens.txt', 'r+') as file:
            linha = file.readline()
            if linha:
                dados = eval(linha)
                user = database_local.is_user(True)
                if dados['nome'] != user.nome:
                    if dados['nome'] == 'ryanbs':
                        frame_11 = QFrame()
                        frame_11.setObjectName(u"frame_11")
                        frame_11.setMaximumSize(QSize(16777215, 1000))
                        frame_11.setFrameShape(QFrame.NoFrame)
                        frame_11.setFrameShadow(QFrame.Raised)
                        verticalLayout_5 = QVBoxLayout(frame_11)
                        verticalLayout_5.setSpacing(2)
                        verticalLayout_5.setObjectName(u"verticalLayout_5")
                        verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
                        frame_14 = QFrame(frame_11)
                        frame_14.setObjectName(u"frame_14")
                        frame_14.setMaximumSize(QSize(16777215, 1000))
                        frame_14.setFrameShape(QFrame.NoFrame)
                        frame_14.setFrameShadow(QFrame.Raised)
                        horizontalLayout_10 = QHBoxLayout(frame_14)
                        horizontalLayout_10.setSpacing(2)
                        horizontalLayout_10.setObjectName(u"horizontalLayout_10")
                        horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

                        verticalLayout_5.addWidget(frame_14)
                        font4 = QFont()
                        font4.setPointSize(16)
                        font4.setBold(True)
                        nome_msg = QPushButton(frame_11)
                        nome_msg.setObjectName(u"nome_msg")
                        nome_msg.setFont(font4)
                        nome_msg.setLayoutDirection(Qt.RightToLeft)
                        nome_msg.setStyleSheet(u"color: rgb(206, 153, 25);;border:0;outline:0")
                        icon4 = QIcon()
                        icon4.addFile(f":/icons/{dados['logo'].lower()}", QSize(), QIcon.Normal, QIcon.Off)
                        nome_msg.setIcon(icon4)
                        nome_msg.setIconSize(QSize(28, 24))
                        nome_msg.setText(f"{dados['nome']}")

                        verticalLayout_5.addWidget(nome_msg, 0, Qt.AlignRight)

                        label_13 = QLabel(frame_11)

                        # width label
                        width = main.width_label(dados['mensagem'])
                        label_13.setObjectName(u"label_13")
                        label_13.setMinimumSize(QSize(0, 0))
                        label_13.setMaximumSize(QSize(width, 1000))
                        font11 = QFont()
                        font11.setFamily(u"Sans Serif")
                        font11.setPointSize(14)
                        label_13.setFont(font11)
                        label_13.setStyleSheet(
                "color:white;\n"
                "background-color: rgb(60, 60, 60);")
                        label_13.setScaledContents(True)
                        label_13.setWordWrap(True)
                        label_13.setMargin(5)

                        label_13.setText(dados['mensagem'])

                        verticalLayout_5.addWidget(label_13)

                        label_10 = QLabel(frame_11)
                        label_10.setObjectName(u"label_10")
                        label_10.setStyleSheet(u"color:#5f6368")
                        label_10.setText(dados['hora'])

                        verticalLayout_5.addWidget(label_10)

                        self.verticalLayout_7.addWidget(frame_11)
                        file.truncate(0)
                        database_local.add_messages(dados['mensagem'], dados['hora'], dados['nome'], dados['logo'].lower())

                    else:
                        frame_11 = QFrame()
                        frame_11.setObjectName(u"frame_11")
                        frame_11.setMaximumSize(QSize(16777215, 1000))
                        frame_11.setFrameShape(QFrame.NoFrame)
                        frame_11.setFrameShadow(QFrame.Raised)
                        verticalLayout_5 = QVBoxLayout(frame_11)
                        verticalLayout_5.setSpacing(2)
                        verticalLayout_5.setObjectName(u"verticalLayout_5")
                        verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
                        frame_14 = QFrame(frame_11)
                        frame_14.setObjectName(u"frame_14")
                        frame_14.setMaximumSize(QSize(16777215, 1000))
                        frame_14.setFrameShape(QFrame.NoFrame)
                        frame_14.setFrameShadow(QFrame.Raised)
                        horizontalLayout_10 = QHBoxLayout(frame_14)
                        horizontalLayout_10.setSpacing(2)
                        horizontalLayout_10.setObjectName(u"horizontalLayout_10")
                        horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

                        verticalLayout_5.addWidget(frame_14)
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
                        icon4.addFile(f":/icons/{dados['logo'].lower()}", QSize(), QIcon.Normal, QIcon.Off)
                        nome_msg.setIcon(icon4)
                        nome_msg.setIconSize(QSize(28, 24))
                        nome_msg.setText(f"{dados['nome']}")

                        verticalLayout_5.addWidget(nome_msg, 0, Qt.AlignRight)

                        label_13 = QLabel(frame_11)
                        label_13.setObjectName(u"label_13")

                        # width label
                        width = main.width_label(dados['mensagem'])
                        label_13.setMaximumSize(QSize(width, 1000))
                        font11 = QFont()
                        font11.setFamily(u"Sans Serif")
                        font11.setPointSize(14)
                        label_13.setFont(font11)
                        label_13.setStyleSheet(
                "color:white;\n"
                "background-color: rgb(60, 60, 60);")
                        label_13.setScaledContents(True)
                        label_13.setWordWrap(True)
                        label_13.setMargin(5)
                        label_13.setText(dados['mensagem'])

                        verticalLayout_5.addWidget(label_13)

                        label_10 = QLabel(frame_11)
                        label_10.setObjectName(u"label_10")
                        label_10.setStyleSheet(u"color:#5f6368")
                        label_10.setText(dados['hora'])

                        verticalLayout_5.addWidget(label_10)

                        self.verticalLayout_7.addWidget(frame_11)
                        file.truncate(0)
                        database_local.add_messages(dados['mensagem'], dados['hora'], dados['nome'], dados['logo'].lower())

                    t1 = threading.Thread(target=notification, args=[self, tray])
                    t1.start()

    # send message rabbit 
    def developer_send(self, nome, tecnologia, mensagem, hora):
        try:
            developer = dev.Dev()
            developer.send(nome=nome, logo=tecnologia, message=mensagem, hora=hora)
        except:
            self.animation_net(True)
            self.btn_msg.setDisabled(True)
            self.btn_ocultar_mostrar.setDisabled(True)
            self.input_msg.setDisabled(True)
            self.sem_internet.setStyleSheet(u"background-color: rgb(246, 97, 81);\n"
    "color:white;\n"
    "border-radius:5px")     
            self.sem_internet.setText('Erro inesperado ao enviar sua mensagem, reinicie o aplicativo.')


counter = 0
class SplashScreen(QMainWindow, Ui_SplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.label_description.setText("<strong>Bem vindo</strong> a comunidade")

        QTimer.singleShot(1000, lambda: self.label_description.setText("<strong>Verificando</strong> internet"))
        QTimer.singleShot(2000, lambda: self.label_description.setText("<strong>Carregando</strong> mensagens"))

        self.show()

    def progress(self):
        global counter
        self.progressBar.setValue(counter)

        if counter >= 100:
            # STOP TIMER
            self.label_description.setText("<strong>Abrindo o aplicativo</strong>")
            self.timer.stop()

            self.close()
            self.main = Chat()
            self.main.show()

        counter += 1


def notification(self, tray: QSystemTrayIcon):
    notificationTitle = 'Chat developers'
    notificationMessage = 'Nova mensagem'
    icon = QIcon(u":/icons/logo_chat.png")
    duration = 3 * 1000 #3 seconds

    tray.showMessage(notificationTitle, notificationMessage, icon, duration)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if database_local.is_user():
        window = SplashScreen()
    else:
        window = Login()

    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "Notificações", "Não foi possível enviar notificações.")
        sys.exit(0)

    app.setQuitOnLastWindowClosed(False)
    tray = QSystemTrayIcon(QIcon(u":/icons/logo_chat.png"), app)

    menu = QMenu()
    action_hide = QAction("Ocultar Janela")
    action_hide.setIcon(QIcon(QPixmap('resources/hide.svg')))
    menu.addAction(action_hide)

    action_show = QAction("Mostrar janela")
    action_show.setIcon(QIcon(QPixmap('resources/show.svg')))
    menu.addAction(action_show)

    action_exit = QAction("Sair")
    action_exit.setIcon(QIcon(QPixmap('resources/close.svg')))

    def close():
        sys.exit()

    action_exit.triggered.connect(close)

    menu.addAction(action_exit)
    
    tray.setContextMenu(menu)
    
    tray.show()

    window.show()
    sys.exit(app.exec_())

