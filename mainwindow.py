from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt

import pyperclip

from selectablewindow import SelectableWindow
from arguments import parse_args

class MainWindow(SelectableWindow):
    """Create a new MainWindow

    Args:
        screenshot (PIL.Image): A screenshot.
        ocr ((PIL.Image) -> str): A function returning the recognized text of
            the input image.

    Returns:
        MainWindow: The newly created Window
    """
    def __init__(self, screenshot, ocr):
        SelectableWindow.__init__(self)

        self.screenshot = screenshot
        self.qt_screenshot = ImageQt(screenshot)
        self.setPixmap(QPixmap.fromImage(self.qt_screenshot))

        self.ocr = ocr

        self.args = parse_args()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
            return

    def mouseReleaseEvent(self, event):
        selection_area = self.get_selection()
        cropped_screenshot = self.screenshot.crop(selection_area)
        text = self.ocr(cropped_screenshot)

        if not self.args.quiet:
            print(text)
        if self.args.clipboard:
            pyperclip.copy(text)

        self.close()
