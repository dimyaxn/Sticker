import sys
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from design import Ui_MainWindow



class Sticker(QMainWindow):
    def __init__(self):
        super(Sticker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = Sticker()
    window.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
    window.setWindowOpacity(0.6)
    window.show()
    sys.exit(app.exec())