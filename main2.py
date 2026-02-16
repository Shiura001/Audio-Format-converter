
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QPushButton
from inicio import inicio
from PySide6.QtGui import QIcon

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.loader = QUiLoader()
        self.file = QFile("interfaz.ui")
        self.file.open(QFile.ReadOnly)
        self.window = self.loader.load(self.file)
        self.file.close()
        self.window.setWindowTitle("Format hoo")
        self.window.setWindowIcon(QIcon("icono_converter.ico"))


        
        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.window.show()
    inicio(widget)

    sys.exit(app.exec())