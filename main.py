import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtWidgets import QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.btn = QPushButton('Button test')
        self.btn.setStyleSheet('font-size: 24px;')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        self.setCentralWidget(self.cw)

        self.btn.clicked.connect(self.acao)

    def acao(self):
        print('executando o botao')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
