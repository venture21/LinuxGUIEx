import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('First Button')
                
        rbtn1 = QRadioButton('First Button', self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True)
        rbtn1.clicked.connect(self.rbtnClicked)

        rbtn2 = QRadioButton(self)
        rbtn2.move(50, 70)
        rbtn2.setText('Second Button')
        rbtn2.resize(200,40)
        rbtn2.clicked.connect(self.rbtnClicked)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QRadioButton')
        self.show()

    def rbtnClicked(self): 
        sender = self.sender()
        if sender.text=='rbtn1':
            self.statusBar().showMessage('First Button')
        else:
            self.statusBar().showMessage('Second Button')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
