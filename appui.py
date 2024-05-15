from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QWidget, QLineEdit, QPushButton, QFileDialog, QVBoxLayout

import dataanalysis as anly

# 欢迎界面
class WelcomeDialog(QDialog):
    def __init__(self, parent: QWidget | None = None, flags: Qt.WindowType = Qt.WindowType.Dialog) -> None:
        super().__init__(parent, flags)
        self.setWindowTitle("Data Analysis")
        self.setWindowIcon(QIcon("./res/logo.png"))
        self.setupUi()

    def setupUi(self):
        vbox = QVBoxLayout()
        btnXRD = QPushButton(self)
        btnXRD.setText("X射线衍射图谱分析")
        btnXRD.clicked.connect(self.onBtnXRDClicked)

        vbox.addWidget(btnXRD)

        self.setLayout(vbox)
        
    def onBtnXRDClicked(self):
        fileDialog = FileDialog(self)
        fileDialog.show()

# 选择文件界面
class FileDialog(QDialog):
    filePath = ''

    def __init__(self, parent: QWidget | None = None, flags: Qt.WindowType = Qt.WindowType.Dialog) -> None:
        super().__init__(parent, flags)
        self.setFixedSize(590, 80)
        self.setWindowTitle("选择文件")
        self.setWindowIcon(QIcon("./res/logo.png"))
        self.setupUi()

    def setupUi(self):
        self.btnFileChoose = QPushButton(self)
        self.btnFileChoose.setGeometry(350, 20, 100, 30)
        self.btnFileChoose.setText("选择文件...")

        self.btnOpen = QPushButton(self)
        self.btnOpen.setGeometry(470, 20, 100, 30)
        self.btnOpen.setText("开始分析")

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(20, 20, 310, 30)

        self.btnFileChoose.clicked.connect(self.onFileChooseClicked)
        self.btnOpen.clicked.connect(self.onOpenClicked)
    
    def onFileChooseClicked(self):
        self.filePath = QFileDialog.getOpenFileName(self, "选择文件...")[0]
        self.lineEdit.setText(self.filePath)

    def onOpenClicked(self):
        anly.XRDAnalysis(self.filePath)