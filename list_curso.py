import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import mysql.connector as mycon

cx = mycon.connect(
    host = "127.0.0.1",
    port = "6556",
    user = "root",
    password = "123@senac",
    database = "bancocursos"
)

cursor = cx.cursor()

class ExibirCursos(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(500,300,450,350)
        self.setWindowTitle("Cursos cadastrados")

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

        layout = QVBoxLayout()
        layout.addWidget(tbcursos)
        self.setLayout(layout)

if __name__=="__main__":
    app = QApplication(sys.argv)
    tela = ExibirCursos()
    tela.show()
    sys.exit(app.exec_())