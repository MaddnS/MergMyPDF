import PyPDF2
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QFileDialog
from classes.FileListAndButtons import FileListAndButtons

from classes.DropZone import DropZone

class PDFMerger(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDF Merger")

        self.fileListAndButtons = FileListAndButtons()
        self.dropzone = DropZone(self.fileListAndButtons)
        

        layout = QVBoxLayout()
        layout.addWidget(self.dropzone)
    
        layout.addWidget(self.fileListAndButtons)

        self.setLayout(layout)

    def merge_pdfs(self):
        if len(self.dropzone.file_list) == 0:
            print("No files to merge")
            return

        # Initialize PDF writer
        pdf_writer = PyPDF2.PdfWriter()

        # Merge PDFs
        for pdf in self.dropzone.file_list:
            pdf_reader = PyPDF2.PdfReader(pdf)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))

        # Write merged PDF to file
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Merged PDF", "", "PDF Files (*.pdf)")
        if file_path:
            with open(file_path, "wb") as output_file:
                pdf_writer.write(output_file)

            print(f"Merged PDF saved to {file_path}")
