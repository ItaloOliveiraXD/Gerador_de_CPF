import sys
from gerar_cpf import gera_cpf
from validar_cpf import valida_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow

import design

class App(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
    
        self.btn_gerar.clicked.connect(self.gera_cpf)
        self.btn_validar.clicked.connect(self.valida_cpf)
    
    def gera_cpf(self):
        self.input_msg.setText(
            gera_cpf()
        )

    def valida_cpf(self):
        cpf = self.input_msg.text()
        self.input_msg.setText(
            valida_cpf(cpf)
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
