from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
# from PyQt6.QtWidgets import QDialog, QWidget, QLineEdit, QPushButton, QFileDialog, QVBoxLayout, QMessageBox

import os
import webbrowser
from enum import Enum

import dataanalysis as anly

# 负责存储模块类型的枚举对象
class AnalysisType(Enum):
    Empty = 0
    XRDAnalysis = 1

# 欢迎界面
class WelcomeWidget(QWidget):
    def __init__(self, parent: QWidget | None = None, 
                 flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parent, flags)
        self.setWindowTitle("Data Analysis for Chemists")
        self.setWindowIcon(QIcon("./res/logo.png"))
        self.setupUi()

    def setupUi(self):
        vbox = QVBoxLayout()

        vbox.setSpacing(8)

        btnXRD = QPushButton(self)
        btnXRD.setText("X射线衍射图谱分析")
        btnXRD.setMinimumSize(370, 30)
        btnXRD.clicked.connect(self.onBtnXRDClicked)

        btnAbout = QPushButton(self)
        btnAbout.setText("关于与帮助")
        btnAbout.setMinimumSize(370, 30)
        btnAbout.clicked.connect(self.onBtnAboutClicked)

        vbox.addWidget(btnXRD)

        vbox.addWidget(btnAbout)

        self.setLayout(vbox)
        
    def onBtnXRDClicked(self):
        fileDialog = FileDialog(self, function=AnalysisType.XRDAnalysis)
        fileDialog.show()

    def onBtnAboutClicked(self):
        webbrowser.open(url="https://github.com/AritxOnly/Py-ADataAnalysisSolution")

# 选择文件界面
class FileDialog(QDialog):
    filePath = ''

    def __init__(self, parent: QWidget | None = None, 
                 flags: Qt.WindowType = Qt.WindowType.Dialog, 
                 function = AnalysisType.Empty) -> None:
        super().__init__(parent, flags)

        self.func = function

        # 窗口初始化
        # self.setModal(True)
        self.setupUi()
        self.setWindowTitle("选择文件")
        self.setWindowIcon(QIcon("./res/logo.png"))

    def setupUi(self):
        hbox = QHBoxLayout()

        hbox.setSpacing(8)

        self.btnFileChoose = QPushButton(self)
        self.btnFileChoose.setFixedSize(100, 30)
        self.btnFileChoose.setText("选择文件...")

        self.btnOpen = QPushButton(self)
        self.btnOpen.setFixedSize(100, 30)
        self.btnOpen.setText("开始分析")

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setFixedSize(310, 30)

        self.btnFileChoose.clicked.connect(self.onFileChooseClicked)
        self.btnOpen.clicked.connect(self.onOpenClicked)

        hbox.addWidget(self.lineEdit)
        hbox.addWidget(self.btnFileChoose)
        hbox.addWidget(self.btnOpen)

        self.setLayout(hbox)
    
    def onFileChooseClicked(self):
        self.filePath = QFileDialog.getOpenFileName(self, "选择文件...")[0]
        self.lineEdit.setText(self.filePath)

    def onOpenClicked(self):
        self.filePath = self.lineEdit.text()

        if not os.path.isfile(self.filePath):
            msgBox = QMessageBox(self)
            msgBox.setWindowTitle("错误！")
            msgBox.setText("文件或目录不存在！")
            msgBox.exec()
            return

        match self.func:
            case AnalysisType.XRDAnalysis:
                try:
                    anly.XRDAnalysis(self.filePath)
                except Exception as error:
                    msgBox = QMessageBox(self)
                    msgBox.setWindowTitle("错误！")
                    msgBox.setText("错误信息\n" + str(error))
                    msgBox.exec()
                    return
            