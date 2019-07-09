import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QLabel
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Filtros-OPenCV'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 250
        self.initUI()
        self.radioButton()

    def initUI(self):
        self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)
        # Create Pixmap
        label = QLabel(self)
        pixmap = QPixmap('openCVLogo01.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())

        #Label
        la= QLabel(self)
        la.setText("Filtros")
        la.move(20,0)
        la.setFont(QtGui.QFont("Arial", 8, QtGui.QFont.Black))

       #Criar Box
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 15)
        self.textbox.resize(170,20)
        # Create a button in the window
        self.button = QPushButton('OK', self)#button.setToolTip('font dialog')
        self.button.move(20,130)
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()


    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        reposta = QMessageBox.question(self, 'Aplicado', "Tipo do Filtro: " + textboxValue, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        self.textbox.setText("")
        if reposta == QMessageBox.Yes:
            print('Yes clicked.')
        else:
            print('No clicked.')



    def onClicked_radioBotton(self):
        from sqlite_tex import Controle as SQL
        from filtros import Controle as fil
        from tesseract import Controle as pysseract
        sql = SQL()
        filt = fil(sql.select_db(20))
        tesseract = pysseract()#Iniciar Tesseract

        radioButton = self.sender()
        if radioButton.isChecked():
            print("Estado: %s" % (radioButton.country))
            filt.Algoritmo_Basico(21)
            tesseract.tesseract_opc(0,"Tesseract.jpg")#tesseract



    def radioButton(self):
        layout = QGridLayout()
        self.setLayout(layout)
        radiobutton = QRadioButton("Algoritmo Basico")
        radiobutton.setChecked(True)
        radiobutton.country = "Algoritmo Basico"
        radiobutton.toggled.connect(self.onClicked_radioBotton)
        layout.addWidget(radiobutton, 0, 0)
        #----------------------------------------------------------
        radiobutton = QRadioButton("Algoritmo Medio")
        radiobutton.setChecked(True)
        radiobutton.country = "Algoritmo Medio"
        radiobutton.toggled.connect(self.onClicked_radioBotton)
        layout.addWidget(radiobutton, 0, 1)
        #------------------------------------------------------
        radiobutton = QRadioButton("Algoritmo Alto")
        radiobutton.setChecked(True)
        radiobutton.country = "Algoritmo Alto"
        radiobutton.toggled.connect(self.onClicked_radioBotton)
        layout.addWidget(radiobutton, 1,0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
