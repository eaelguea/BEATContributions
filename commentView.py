import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class CommentView(QWidget):

    def __init__(self):
        super().__init__()
        self.textbox = QLineEdit(self)
        self.save = QPushButton('Save', self)
        self.clear_b = QPushButton('Clear', self)
        self.title = 'Comment View'
        self.left = 10
        self.top = 10
        self.width = 480
        self.height = 250
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.save.move(330, 200)
        self.clear_b.move(400, 200)
        self.save.clicked.connect
        self.clear_b.clicked.connect(self.on_click)

        self.textbox.move(20, 20)
        self.textbox.resize(440, 175)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('button click')
        self.clear_b.clicked.connect(self.textbox.clear)
        self.save.clicked.connect(self.textbox.clear)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CommentView()
    sys.exit(app.exec_())
