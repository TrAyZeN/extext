import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel, QRubberBand
from PyQt5.QtGui import QPixmap, QPainter, QBrush
from PyQt5.QtCore import Qt, QRect, QPoint, QSize

from PIL import ImageGrab
from PIL.ImageQt import ImageQt

import pytesseract

import pyperclip

from arguments import parse_args

args = parse_args()

app = QApplication(sys.argv)
app.setApplicationName("salut")
app.setApplicationDisplayName("salut")

screenshot = ImageGrab.grab()
qt_screenshot = ImageQt(screenshot)

class Window(QLabel):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.origin = QPoint()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            app.exit()
            return

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.origin = QPoint(event.pos())
            self.rubberBand.setGeometry(QRect(self.origin, QSize()))
            self.rubberBand.show()

    def mouseMoveEvent(self, event):
        if not self.origin.isNull():
            self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        selection_area = self.rubberBand.geometry().getCoords()
        cropped_screenshot = screenshot.crop(selection_area)
        text = pytesseract.image_to_string(cropped_screenshot)
        if not args.quiet:
            print(text)
        if args.clipboard:
            pyperclip.copy(text)
        self.close()
        #  app.exit()

window = Window()
window.setPixmap(QPixmap.fromImage(qt_screenshot))
window.showFullScreen()

app.exec_()
