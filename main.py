import sys
from PySide6 import QtCore
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QStyle, QMenu
from PySide6 import QtGui
from design import Ui_MainWindow



class Sticker(QMainWindow):
    tray_icon = None
    # tr_ic = QIcon()
    # tr_ic.addFile('icons/Pictogrammers-Material-Sticker-text-outline.512.png')
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.tray_icon = QSystemTrayIcon(self)
        # self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
        self.tray_icon.setIcon(QtGui.QIcon('icons/Pictogrammers-Material-Sticker-text-outline.512.png'))



        show_action = QAction("Развернуть", self)
        hide_action = QAction("Свернуть", self)
        quit_action = QAction("Выход", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        self.tray_icon.activated.connect(self.show)
        #QSystemTrayIcon.Information

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        # self.tray_icon.showMessage(
        #     "Стикер спрятан в трей!",
        #     "Меню по ПКМ",
        #     QSystemTrayIcon.Information,
        #     3,
        # )

    # def restore_window(self, reason):
    #     if reason == QSystemTrayIcon.Trigger:  # ЛКМ
    #         self.tray_icon.show()
    #         self.showNormal()
    #     elif reason == QSystemTrayIcon.MiddleClick:
    #         self.tray_icon.show()
    #         self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')                                  #Задаем стиль окна
    window = Sticker()
    window.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)    #Окно поверх других окон
    window.setWindowOpacity(0.6)                            #Устанавливаем прозрачность окна на 0.6
    window.show()
    sys.exit(app.exec())