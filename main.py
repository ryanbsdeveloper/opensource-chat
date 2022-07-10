import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QFrame, QVBoxLayout, QLabel, QDialog
from PySide2.QtGui import QFont
from PySide2.QtCore import *
from widgets.chat import Ui_Chat
from widgets.conf import Ui_Conf
from widgets.login import Ui_Login

import resources.resources

class Conf(QDialog, Ui_Conf):
    def __init__(self, parent):
        super(Conf, self).__init__(parent)
        self.setupUi(self)


class Login(QDialog, Ui_Login):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)

    def name_developer(self):
        nome = self.input_nome.text()
        users = []

        if nome > 15:
            self.erro_nome.setText('Nome muito extenso.')

        elif nome < 4:
            self.erro_nome.setText('Nome muito curto.')
        
        elif nome in users:
            self.erro_nome.setText('Nome já está em uso.')
        else:
            # add db
            pass

class Chat(QMainWindow, Ui_Chat):
    def __init__(self, parent=None):
        super(Chat, self).__init__(parent)
        self.setupUi(self)
        self.btn_msg.clicked.connect(self.add_my_msg)
        self.scrollArea.verticalScrollBar().rangeChanged.connect(self.ResizeScroll)
        self.input_msg.returnPressed.connect(self.btn_msg.click)

        # Others windows
        self.conf = Conf(self)
        self.btn_config.clicked.connect(self.open_conf)

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
    window = Login()
    window.show()
    sys.exit(app.exec_())
