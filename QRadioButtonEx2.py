import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('First Button')
                
        self.rbtn1 = QRadioButton('First Button', self)
        self.rbtn1.move(50, 50)
        self.rbtn1.setChecked(True)
        self.rbtn1.resize(200,40)
        self.rbtn1.clicked.connect(self.rbtnClicked)

        self.rbtn2 = QRadioButton(self)
        self.rbtn2.move(50, 70)
        self.rbtn2.setText('Second Button')
        self.rbtn2.resize(200,40)
        self.rbtn2.clicked.connect(self.rbtnClicked)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QRadioButton')
        self.show()

    def rbtnClicked(self): 
        if self.rbtn1.isChecked():
            self.statusBar().showMessage('First Button')
        else:
            self.statusBar().showMessage('Second Button')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
