from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt


class DropZone(QLabel):
    def __init__(self, fileListAndButtons):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setText("Drop files here")
        self.setAcceptDrops(True)
        self.fileListAndButtons = fileListAndButtons
        self.file_list = fileListAndButtons.file_list

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        for file in files:
            if file.endswith(".pdf"):
                self.file_list.addItem(file)
                print(f"Added {file} to merge list")
            else:
                print(f"File {file} is not a PDF and cannot be merged")