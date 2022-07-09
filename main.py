import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from widgets.chat import Ui_MainWindow

import resources.resources

class Chat(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Chat, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Chat()
    window.show()
    app.exec_()