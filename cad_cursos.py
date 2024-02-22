import sys

import mysql.connector as mc

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton


con = mc.connect(
    host = "127.0.0.1",
    port = "6556",
    user = "root",
    password = "123@senac",
    database = "bancocursos"
)

cursor = con.cursor()


class CadCurso(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30,40,600,250)
        self.setWindowTitle("Cadastro de Cursos")

        labelNome = QLabel("Nome do Curso: ")
        self.editNome = QLineEdit()

        labelCarga = QLabel("Carga Horária: ")
        self.editCarga = QLineEdit()

        psbCadastro = QPushButton("Cadastrar")

        self.labelMsg = QLabel("|")

        layout = QVBoxLayout()

        layout.addWidget(labelNome)
        layout.addWidget(self.editNome)
 
        layout.addWidget(labelCarga)
        layout.addWidget(self.editCarga)
 
        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.cadCur)

    
        layout.addWidget(self.labelMsg)

        self.setLayout(layout)

    def cadCur(self):
        cursor.execute("insert into tbcursos(nomecurso,cargahoraria)values(%s,%s)",
                       (self.editNome.text(), self.editCarga.text()))
        con.commit()
        self.labelMsg.setText("Curso cadastrado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = CadCurso()
    tela.show()
    sys.exit(app.exec_())