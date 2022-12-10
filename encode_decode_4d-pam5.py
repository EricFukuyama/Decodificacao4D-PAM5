import matplotlib.pyplot as plt
import numpy as np
import contextlib
import struct
import time
import sys, os

from PyQt5 import uic
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

Ui_MainWindow, QtBasesClass = uic.loadUiType("encode_decode.ui")

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent=parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.time = QTimer(self)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout_3.addWidget(self.canvas)

        self.pushButton.clicked.connect(self.texto)

        self.codificacao = []
        self.binario = []

        self.value = 0
        self.start = 0
        self.end = 8

        self.atualizacao()

        self.timer.set.Interval(300)
        self.timer.start()

    def texto(self):
        
        self.binario.clear()
        self.codificacao.clear()
        global escrita
        escrita = self.lineEdit.text()

        entrada = ""

        tamanho = len(escrita)
        for i in range(len(escrita)):
            self.a = ord(escrita[i])
            self.b = bin(self.a)[2:].zfill(8)
            entrada += bin(ord(escrita[i]))[2:].zfill(8)
            print(self.b)

            self.codifica()
            print(self.codificacao)

        self.textBrowser.setText(entrada)
        self.grafica()

    def codifica(self):
        tamanho = len(self.b) - 1
        verifica = 0

        while (verifica != 8):
            par = 10*int(self.b[tamanho-1])
            print(par)
            par = par+int(self.b[tamanho])

            if(par == 0):
                self.codificacao.append(-1)
            if(par == 1):
                self.codificacao.append(-2)
            if(par == 10):
                self.codificacao.append(1)
            if(par == 11):
                self.codificacao.append(2)
            
            tamanho = tamanho - 2
            verifica = verifica + 2
        print(self.codificacao)

    def grafica(self):
        tam = len(escrita) * 4
        j = 0

        self.binario.append(0)

        for i in range(tam-1):
            j = j+2
            self.bianrio.append(j)

    def atualizacao(self):
        self.timer.timeout.connect(self.sequencia)

    def sequencia(self):
        self.imprimeGrafico()
        self.moveSlader()

    def imprimeGrafico(self):
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlim(self.binario, self.condificacao)
        self.canvas.draw()

    def moveSlader(self):
        intervalo = 8
        self.value = (self.binario[-1] - 9*intervalo/10)*self.horizontalSlider.value()/99
        self.start = self.value - intervalo/10
        self.end = self.start + 12*intervalo/10


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())