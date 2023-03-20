import sys

from PyQt5.QtWidgets import QApplication

from core.ya_enter import RegW


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_w = RegW()
    main_w.show()
    sys.exit(app.exec())
