import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap

from PIL import ImageGrab
from PIL.ImageQt import ImageQt

import pytesseract

import pyperclip

from arguments import parse_args
from selectable_window import SelectableWindow

args = parse_args()

app = QApplication(sys.argv)
app.setApplicationName("salut")
app.setApplicationDisplayName("salut")

class Window(SelectableWindow):
    def __init__(self, screenshot):
        SelectableWindow.__init__(self)

        self.screenshot = screenshot
        self.qt_screenshot = ImageQt(screenshot)
        self.setPixmap(QPixmap.fromImage(self.qt_screenshot))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            app.exit()
            return

    def mouseReleaseEvent(self, event):
        selection_area = self.get_selection()
        cropped_screenshot = self.screenshot.crop(selection_area)
        text = pytesseract.image_to_string(cropped_screenshot)

        if not args.quiet:
            print(text)
        if args.clipboard:
            pyperclip.copy(text)

        self.close()
        #  app.exit()

screenshot = ImageGrab.grab()

window = Window(screenshot)
window.showFullScreen()

app.exec_()
