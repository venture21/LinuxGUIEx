import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap


class MyApp(QWidget):

    def __init__(self):
        super(MyApp, self).__init__()

        self.initUI()

    def initUI(self):

        self.btn1 = QPushButton('&Button1', self)
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(self.textChange)

        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def textChange(self):
        if self.btn1.isChecked():
            self.btn1.setText('Button ON')
        else:
            self.btn1.setText('Button OFF')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
