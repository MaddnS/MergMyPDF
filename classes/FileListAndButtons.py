import os
import sys
import PyPDF2
from PyQt5 import QtWidgets

class FileListAndButtons(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Merger")

        # Create widgets
        self.add_button = QtWidgets.QPushButton("Add")
        self.delete_button = QtWidgets.QPushButton("Delete")
        self.merge_button = QtWidgets.QPushButton("Merge")
        self.file_list = QtWidgets.QListWidget()

        # Add layout
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.merge_button)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.file_list)

        self.setLayout(main_layout)