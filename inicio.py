from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout,
    QMessageBox, QListView
)
from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import QApplication, QFileDialog
from modules.conversor import *


def inicio(self):
    self.btn_select = self.window.findChild(QPushButton, "btn_select")
    self.btn_select.clicked.connect(lambda: select_file(self))
    

    self.btn_convert = self.window.findChild(QPushButton, "btn_convert")
    self.btn_convert.clicked.connect(lambda: mostrar_seleccion(self))

    self.list = self.window.findChild(QListView, "listView")
    items = [".ogg", ".mp3", ".wav"]
    self.model = QStringListModel(items)   # Modelo con los datos
    self.list.setModel(self.model)  
    self.list.setEditTriggers(QListView.NoEditTriggers)
    






def mostrar_seleccion(self):
    indexes = self.list.selectedIndexes()  # Devuelve lista de índices seleccionados
    if indexes:
        valor = self.model.data(indexes[0])  # Obtenemos el texto
        convertt=convert(self.archivo,valor)
        if convertt==True:
            msg = QMessageBox()
            msg.setWindowTitle("Correcto")            # Título de la ventana del mensaje
            msg.setText("Formato exitoso") # Texto principal
            msg.setIcon(QMessageBox.Information)        # Icono: Information, Warning, Critical, Question
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
           
    else:
        print("No hay nada seleccionado")

def select_file(self):
    self.archivo, _ = QFileDialog.getOpenFileName(
    None,                   # parent (ventana principal, None si no hay)
    "Selecciona un archivo",# título de la ventana
    "",                     # carpeta inicial
    "Archivos de audio (*.mp3 *.wav *.m4a *.ogg *.flac *.aac)"  # filtro de tipos
    )
    
