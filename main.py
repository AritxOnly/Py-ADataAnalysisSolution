# modules
import sys
from PyQt6.QtWidgets import QApplication

from appui import WelcomeWidget

if __name__ == '__main__':
    # 初始化窗口
    app = QApplication(sys.argv)
    dialog = WelcomeWidget()
    dialog.show()
    sys.exit(app.exec())