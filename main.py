import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QFrame, QVBoxLayout, QLabel
from PySide2.QtGui import QFont
from PySide2.QtCore import *
from widgets.chat import Ui_Chat

import resources.resources

class Chat(QMainWindow, Ui_Chat):
    def __init__(self):
        super(Chat, self).__init__()
        self.setupUi(self)
        self.btn_msg.clicked.connect(self.add_my_msg)
        self.scrollArea.verticalScrollBar().rangeChanged.connect(self.ResizeScroll)
        self.input_msg.returnPressed.connect(self.btn_msg.click)



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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Chat()
    window.show()
    app.exec_()