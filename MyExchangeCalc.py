import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QDialog):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        tabs = QTabWidget()
        tabs.addTab(FirstTab(), 'LENGTH')
        tabs.addTab(SecondTab(), 'WEIGHT')

        #buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        #buttonbox.accepted.connect(self.accept)
        #buttonbox.rejected.connect(self.reject)

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        #vbox.addWidget(buttonbox)

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 300, 200)
        self.show()


class FirstTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # QLineEdit widget
        self.value = QLineEdit('')
        self.value.setAlignment(Qt.AlignHCenter)
        self.value.setPlaceholderText('value')
        #self.value.setValidator(QIntValidator(0, 999999))
        self.unit='mm'
        # QComboBox widget
        self.cb = QComboBox(self)
        self.cb.setCurrentIndex(0)
        self.cb.addItem('mm')
        self.cb.addItem('cm')
        self.cb.addItem('m')
        self.cb.addItem('km')

        # QLable Widget
        self.label1 = QLabel('', self)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label2 = QLabel('', self)
        self.label2.setAlignment(Qt.AlignHCenter)
        self.label3 = QLabel('', self)
        self.label3.setAlignment(Qt.AlignHCenter)
        self.label4 = QLabel('', self)
        self.label4.setAlignment(Qt.AlignHCenter)

        # display Unit
        self.label5 = QLabel('mm', self)
        self.label5.setAlignment(Qt.AlignHCenter)
        self.label6 = QLabel('cm', self)
        self.label6.setAlignment(Qt.AlignHCenter)
        self.label7 = QLabel('m', self)
        self.label7.setAlignment(Qt.AlignHCenter)
        self.label8 = QLabel('km', self)
        self.label8.setAlignment(Qt.AlignHCenter)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.value, 0,0,1,1)
        grid.addWidget(self.cb, 0,2,1,1)
        grid.addWidget(self.label1, 1,0,1,1)
        grid.addWidget(self.label2, 2,0,1,1)
        grid.addWidget(self.label3, 3,0,1,1)
        grid.addWidget(self.label4, 4,0,1,1)
        grid.addWidget(self.label5, 1,2,1,1)
        grid.addWidget(self.label6, 2,2,1,1)
        grid.addWidget(self.label7, 3,2,1,1)
        grid.addWidget(self.label8, 4,2,1,1)
        
        self.setLayout(grid)
        
        self.value.textChanged[str].connect(self.onChanged)
        self.cb.activated[str].connect(self.onActivated)

    def onActivated(self, text):
        self.unit=text
        self.value.setText('')

    def onChanged(self, text):
        if self.unit=='mm':
            self.label1.setText(text)
            self.label2.setText(str(int(text)/10))
            self.label3.setText(str(int(text)/1000))
            self.label4.setText(str(int(text)/10000000))

        if self.unit=='cm':   
            self.label1.setText(str(int(text)*10))
            self.label2.setText(text)
            self.label3.setText(str(int(text)/100))
            self.label4.setText(str(int(text)/100000))

        if self.unit=='m':   
            self.label1.setText(str(int(text)*100))
            self.label2.setText(str(int(text)*10))
            self.label3.setText(str(int(text)/1000))
            self.label4.setText(str(int(text)/1000000))

        if self.unit=='km':   
            self.label1.setText(str(int(text)*1000))
            self.label2.setText(str(int(text)*100))
            self.label3.setText(str(int(text)/10000))
            self.label4.setText(str(int(text)/10000000))


class SecondTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # QLineEdit widget
        self.value = QLineEdit('')
        self.value.setAlignment(Qt.AlignHCenter)
        self.value.setPlaceholderText('value')
        #self.value.setValidator(QIntValidator(0, 999999))
        self.unit='mm'
        # QComboBox widget
        self.cb = QComboBox(self)
        self.cb.setCurrentIndex(0)
        self.cb.addItem('mg')
        self.cb.addItem('g')
        self.cb.addItem('kg')
        self.cb.addItem('t')

        # QLable Widget
        self.label1 = QLabel('', self)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label2 = QLabel('', self)
        self.label2.setAlignment(Qt.AlignHCenter)
        self.label3 = QLabel('', self)
        self.label3.setAlignment(Qt.AlignHCenter)
        self.label4 = QLabel('', self)
        self.label4.setAlignment(Qt.AlignHCenter)

        # display Unit
        self.label5 = QLabel('mm', self)
        self.label5.setAlignment(Qt.AlignHCenter)
        self.label6 = QLabel('cm', self)
        self.label6.setAlignment(Qt.AlignHCenter)
        self.label7 = QLabel('m', self)
        self.label7.setAlignment(Qt.AlignHCenter)
        self.label8 = QLabel('km', self)
        self.label8.setAlignment(Qt.AlignHCenter)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.value, 0,0,1,1)
        grid.addWidget(self.cb, 0,2,1,1)
        grid.addWidget(self.label1, 1,0,1,1)
        grid.addWidget(self.label2, 2,0,1,1)
        grid.addWidget(self.label3, 3,0,1,1)
        grid.addWidget(self.label4, 4,0,1,1)
        grid.addWidget(self.label5, 1,2,1,1)
        grid.addWidget(self.label6, 2,2,1,1)
        grid.addWidget(self.label7, 3,2,1,1)
        grid.addWidget(self.label8, 4,2,1,1)

        self.setLayout(grid)

        self.value.textChanged[str].connect(self.onChanged)
        self.cb.activated[str].connect(self.onActivated)

    def onActivated(self, text):
        self.unit=text
        self.value.setText('')

    def onChanged(self, text):
        if self.unit=='mg':
            self.label1.setText(text)
            self.label2.setText(str(int(text)/1000))
            self.label3.setText(str(int(text)/1000000))
            self.label4.setText(str(int(text)/1000000000))

        if self.unit=='g':
            self.label1.setText(str(int(text)*1000))
            self.label2.setText(text)
            self.label3.setText(str(int(text)/1000))
            self.label4.setText(str(int(text)/1000000))

        if self.unit=='kg':
            self.label1.setText(str(int(text)*1000000))
            self.label2.setText(str(int(text)*1000))
            self.label3.setText(text)
            self.label4.setText(str(int(text)/1000))

        if self.unit=='t':
            self.label1.setText(str(int(text)*1000000000))
            self.label2.setText(str(int(text)*1000000))
            self.label3.setText(str(int(text)/1000))
            self.label4.setText(text)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
