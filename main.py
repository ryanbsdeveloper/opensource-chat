import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QFrame, QVBoxLayout, QLabel, QDialog, QRadioButton
from PySide2.QtGui import QFont, QIcon
from PySide2.QtCore import *
from widgets.chat import Ui_Chat
from widgets.conf import Ui_Conf
from widgets.login import Ui_Login
from modules.databases import database_aws, database_local

import resources.resources

class Conf(QDialog, Ui_Conf):
    def __init__(self, parent):
        super(Conf, self).__init__(parent)
        self.setupUi(self)
    

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
        radioButtons = [elem for elem in self.boxElements if isinstance(elem, QRadioButton)]
        for rb in radioButtons:
            if rb.isChecked():
                icon1 = QIcon()
                icon1.addFile(f":/icons/{rb.text().lower()}", QSize(), QIcon.Normal, QIcon.Off)
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
        self.developer_log()

        # Others windows
        self.conf = Conf(self)
        self.btn_config.clicked.connect(self.open_conf)
    
    # Developer log
    def developer_log(self):
        nome = database_local.is_user(True).nome
        tecnologia = database_local.is_user(True).tecnologia
        icon1 = QIcon()
        icon1.addFile(f":/icons/{tecnologia.lower()}", QSize(), QIcon.Normal, QIcon.Off)

        self.developer.setText(nome)
        self.developer.setIcon(icon1)       

    # Add mensages
    def add_my_msg(self):
        msg = self.input_msg.text()

        frame = QFrame()
        frame.setObjectName(u"frame_6436")
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Raised)
        frame.setMaximumSize(QSize(16777215, 40))

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

        if msg:
            label.setText(QCoreApplication.translate("MainWindow", f"{msg}", None))
            verticalLayout.addWidget(label)
            self.verticalLayout_7.addWidget(frame)
            self.input_msg.setText('')

    def ResizeScroll(self, min, maxi):
        self.scrollArea.verticalScrollBar().setValue(maxi)

    # Open others windows
    def open_conf(self):
        self.conf.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if database_local.is_user():
        window = Chat()
    else:
        window = Login()
    window.show()
    sys.exit(app.exec_())
