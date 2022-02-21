from PyQt5.QtWidgets import QApplication
from PIL import ImageGrab
import sys
import pytesseract
from extext.mainwindow import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("extext")
    app.setApplicationDisplayName("extext")

    screenshot = ImageGrab.grab()
    window = MainWindow(screenshot, pytesseract.image_to_string)
    window.showFullScreen()

    app.exec_()

main()
