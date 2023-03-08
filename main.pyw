from PyQt5.QtWidgets import QApplication
from classes.PDFMerger import PDFMerger

if __name__ == '__main__':
    app = QApplication([])
    merger = PDFMerger()
    merger.show()
    app.exec_()