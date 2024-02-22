import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel, QLineEdit, QVBoxLayout, QPushButton
import mysql.connector as mycon

cx = mycon.connect(
    host = "127.0.0.1",
    port = "6556",
    user = "root",
    password = "123@senac",
    database = "bancocursos"
)

cursor = cx.cursor()

class AtualizarCursos(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.setGeometry(500,300,450,350)
        self.setWindowTitle("Cursos cadastrados")
        
        
        labelId = QLabel("Id Curso: ")
        self.editId = QLineEdit()


        labelNome = QLabel("Nome do Curso: ")
        self.editNome = QLineEdit()

        labelCarga = QLabel("Carga Horária: ")
        self.editCarga = QLineEdit()


        psbCadastro = QPushButton("Cadastrar")
        
        
        layout.addWidget(labelId)
        layout.addWidget(self.editId)


        layout.addWidget(labelNome)
        layout.addWidget(self.editNome)

        layout.addWidget(labelCarga)
        layout.addWidget(self.editCarga)

        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.upCur)


        tbcursos = QTableWidget(self)
        tbcursos.setColumnCount(3)
        tbcursos.setRowCount(70)

        headerLine=["Id","Nome","Carga"]

        tbcursos.setHorizontalHeaderLabels(headerLine)
        cursor.execute("select * from tbcursos")

        lintb = 0
        for linha in cursor:
            tbcursos.setItem(lintb,0,QTableWidgetItem(str(linha[0])))
            tbcursos.setItem(lintb,1,QTableWidgetItem(str(linha[1])))
            tbcursos.setItem(lintb,2,QTableWidgetItem(str(linha[2])))
            lintb+=1

        
        layout.addWidget(tbcursos)
        self.setLayout(layout)

    def upCur (self):
        if (self.editId.text()==""):
            print("Não é possível atualizar sem o Id do curso")
        
        elif(self.editNome.text()=="" and self.editCarga.text()==""):
            print("Não é possível atualizar se não houver dados")

        elif(self.editNome.text()!="" and self.editCarga.text()==""):
            cursor.execute("update tbcursos set nomecurso=%s where cursos_id=%s",
                           (self.editNome.text(), self.editId.text()))
            
        elif(self.editNome.text()=="" and self.editCarga.text()!=""):
            cursor.execute("update tbcursos set cargahoraria=%s where cursos_id=%s",
                           (self.editCarga.text(), self.editId.text()))
            
        else:
            cursor.execute("update tbcursos set nomecurso=%s, cargahoraria=%s where cursos_id=%s",
                           (self.editNome.text(), self.editCarga(), self.editId.text()))
            
        cx.commit()
        print("Todas modificações foram realizadas")
            
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    tela = AtualizarCursos()
    tela.show()
    sys.exit(app.exec_())