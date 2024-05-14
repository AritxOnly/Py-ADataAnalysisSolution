# modules
import sys
from PyQt6.QtWidgets import QDialog, QApplication

if __name__ == '__main__':
    # 初始化窗口
    app = QApplication(sys.argv)
    dialog = QDialog()
    dialog.resize(480, 360)
    dialog.setWindowTitle("Data Analysis")
    dialog.show()
    sys.exit(app.exec())