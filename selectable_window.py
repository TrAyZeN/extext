from PyQt5.QtWidgets import QLabel, QRubberBand
from PyQt5.QtCore import Qt, QRect, QPoint, QSize

class SelectableWindow(QLabel):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)

        self.selection_area = QRubberBand(QRubberBand.Rectangle, self)
        self.origin = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.origin = QPoint(event.pos())
            self.selection_area.setGeometry(QRect(self.origin, QSize()))
            self.selection_area.show()

    def mouseMoveEvent(self, event):
        if not self.origin.isNull():
            new_geometry = QRect(self.origin, event.pos()).normalized()
            self.selection_area.setGeometry(new_geometry)

    def mouseReleaseEvent(self, event):
        self.selection_area.hide()

    def get_selection(self):
        return self.selection_area.geometry().getCoords()
