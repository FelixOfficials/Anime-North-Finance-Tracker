from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.cur_index = 0
        self.people = []
        
    def setupUI(self, MainWindow):
        
        MainWindow.resize(1920, 1080)
        MainWindow.setWindowTitle("Anime North, Finance Tracker")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.title = QtWidgets.QLabel("Money")

        self.create_person = QtWidgets.QPushButton("Add Person")
        self.create_row = QtWidgets.QPushButton("Add Purchase")
        self.calculate = QtWidgets.QPushButton("Calculate")
        
        QtWidgets.button.clicked.connect(self.Add_person())
        
    def Add_person(self):
        
        self.people.append(Person(name, index))

        # master_layout = QVBoxLayout()

        # row1 = QHBoxLayout()
        # row2 = QHBoxLayout()
        # row3 = QHBoxLayout()

        # row1.addWidget(title, alignment=Qt.AlignCenter)

        # row2.addWidget(name1, alignment=Qt.AlignCenter)
        # row2.addWidget(name2, alignment=Qt.AlignCenter)
        # row2.addWidget(name3, alignment=Qt.AlignCenter)

        # row3.addWidget(button1, alignment=Qt.AlignCenter)
        # row3.addWidget(button2, alignment=Qt.AlignCenter)
        # row3.addWidget(button3, alignment=Qt.AlignCenter)

        # master_layout.addLayout(row1)
        # master_layout.addLayout(row2)
        # master_layout.addLayout(row3)

        # main_window.setLayout(master_layout)

class Person():
    def __init__(self, name, index):
        self.name = name
        self.poster_count = [0 for x in range(index + 1)]
        self.costs = [0 for x in range(index + 1)]
        
    def Add_data(self, posters, cost):
        self.poster_count.append(posters)
        self.costs.append(cost)
        
    def Modify_data(self, index, posters, cost):
        self.poster_count[index] = posters
        self.costs = cost

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())