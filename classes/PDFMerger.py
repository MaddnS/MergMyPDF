import PyPDF2
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtWidgets
from classes.FileListAndButtons import FileListAndButtons

from classes.DropZone import DropZone


class PDFMerger(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MergeMyPDF")

        self.fileListAndButtons = FileListAndButtons()
        self.dropzone = DropZone(self.fileListAndButtons)

        layout = QVBoxLayout()
        layout.addWidget(self.dropzone)

        layout.addWidget(self.fileListAndButtons)

        self.setLayout(layout)

        # Connect signals and slots
        self.fileListAndButtons.add_button.clicked.connect(self.add_files)
        self.fileListAndButtons.delete_button.clicked.connect(self.delete_file)
        self.fileListAndButtons.merge_button.clicked.connect(self.merge_pdfs)

    def add_files(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_names, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Select PDF Files", "",
                                                               "PDF Files (*.pdf)", options=options)
        if file_names:
            for file_name in file_names:
                self.dropzone.file_list.addItem(file_name)

    def delete_file(self):
        selected_items = self.dropzone.file_list.selectedItems()
        for item in selected_items:
            self.dropzone.file_list.takeItem(self.dropzone.file_list.row(item))

    def merge_pdfs(self):
        if len(self.dropzone.file_list) == 0:
            print("No files to merge")
            msg = QMessageBox()
            msg.setWindowTitle("Uups!")
            msg.setText("No files to merge!")
            msg.exec()
            return

        # Initialize PDF writer
        pdf_writer = PyPDF2.PdfWriter()

        # Merge PDFs
        for pdf in self.dropzone.file_list:
            pdf_reader = PyPDF2.PdfReader(pdf)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))

        # Write merged PDF to file
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Merged PDF", "", "PDF Files (*.pdf)")
        if file_path:
            with open(file_path, "wb") as output_file:
                pdf_writer.write(output_file)

            print(f"Merged PDF saved to {file_path}")
