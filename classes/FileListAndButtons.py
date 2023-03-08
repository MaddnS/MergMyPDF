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

        # Connect signals and slots
        self.add_button.clicked.connect(self.add_files)
        self.delete_button.clicked.connect(self.delete_file)
        self.merge_button.clicked.connect(self.merge_files)

    def add_files(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_names, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Select PDF Files", "",
                                                               "PDF Files (*.pdf)", options=options)
        if file_names:
            for file_name in file_names:
                self.file_list.addItem(file_name)

    def delete_file(self):
        selected_items = self.file_list.selectedItems()
        for item in selected_items:
            self.file_list.takeItem(self.file_list.row(item))

    def merge_files(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        save_file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Merged PDF", "",
                                                                   "PDF Files (*.pdf)", options=options)
        if save_file_name:
            merger = PyPDF2.PdfMerger()
            for row in range(self.file_list.count()):
                file_name = self.file_list.item(row).text()
                if os.path.exists(file_name):
                    merger.append(file_name)
                else:
                    QtWidgets.QMessageBox.warning(self, "File Not Found", f"{file_name} not found.")
            with open(save_file_name, "wb") as f:
                merger.write(f)
            QtWidgets.QMessageBox.information(self, "Merge Complete", f"PDF files merged and saved to {save_file_name}.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FileListAndButtons()
    window.show()
    sys.exit(app.exec_())
