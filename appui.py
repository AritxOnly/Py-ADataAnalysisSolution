from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QWidget, QLineEdit, QPushButton, QFileDialog

class WelcomeDialog(QDialog):
    filePath = ''

    def __init__(self, parent: QWidget | None = None, flags: Qt.WindowType = Qt.WindowType.Dialog) -> None:
        super().__init__(parent, flags)
        self.resize(470, 80)
        self.setWindowTitle("Data Analysis")
        self.btnFileChoose = QPushButton(self)
        self.btnFileChoose.setGeometry(350, 20, 100, 30)
        self.btnFileChoose.setText("选择文件...")
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(20, 20, 310, 30)
        self.btnFileChoose.clicked.connect(self.btnPressSlot)
    
    def btnPressSlot(self):
        self.filePath = QFileDialog.getOpenFileName(self, "选择文件...")[0]
        self.lineEdit.setText(self.filePath)