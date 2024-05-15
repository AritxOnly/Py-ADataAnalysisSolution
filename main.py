# modules
import sys
from PyQt6.QtWidgets import QApplication

from appui import WelcomeDialog

if __name__ == '__main__':
    # 初始化窗口
    app = QApplication(sys.argv)
    dialog = WelcomeDialog()
    dialog.show()
    sys.exit(app.exec())