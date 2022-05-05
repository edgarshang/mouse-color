from time import sleep
from mousecolor import Ui_Form
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import Qt
from pyautogui import position, screenshot
import sys
import imgvision as iv
import numpy as np
import os
import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, "plugins", "platforms")
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = plugin_path


class Thread(QThread):
    sig = pyqtSignal(list)

    def __init__(self):
        super(Thread, self).__init__()

    def run(self):
        while True:
            x, y = position()
            color = screenshot().getpixel((x, y))
            color = [x for x in color]
            self.sig.emit(color)
            sleep(0.1)


class MainWindow(Ui_Form, QMainWindow):
    cvtor = iv.cvtcolor()

    def __init__(self) -> None:
        super(Ui_Form, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.window_config()
        self.threadx = Thread()
        self.threadx.sig.connect(self.setColor)
        self.threadx.start()

    def window_config(self):
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint)

    def setColor(self, color):
        self.ui.tbcolor.setStyleSheet(
            f"background-color: rgb({color[0]}, {color[1]}, {color[2]});"
        )
        self.ui.lbl_color_r.setText(f"{color[0]}")
        self.ui.lbl_color_g.setText(f"{color[1]}")
        self.ui.lbl_color_b.setText(f"{color[2]}")

    def rgb2xyz(self, xr=255, xg=255, xb=255):
        img = np.array([[255, 255, 255]])
        z = self.cvtor.rgb2xyz(img)
        c = self.cvtor.rgb2lab(z)
        print(z)
        pass


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    # main_window.rgb2xyz()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
