import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QSlider
from pyqtgraph import (
    mkBrush,
    mkPen,
    GraphicsObject,
    QtGui,
    PlotWidget,
)


class SquareItem(GraphicsObject):
    def paint(self, p, *args):
        p.setBrush(mkBrush('r'))
        p.setPen(mkPen(None))
        p.drawRect(self.boundingRect())

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 1, 1)

    def update_position(self, x):
        self.setPos(x, 0)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Micromouse maze simulator')
        self.resize(600, 600)

        frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout(frame)

        self.graphics = PlotWidget()
        self.graphics.setAspectLocked()
        self.item = SquareItem()
        self.graphics.addItem(self.item)

        self.graphics.setRange(rect=QtCore.QRectF(-10, -10, 20, 20))

        self.slider = QSlider(QtCore.Qt.Horizontal)
        self.slider.setSingleStep(1)
        self.slider.setPageStep(10)
        self.slider.setRange(0, 10)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.valueChanged.connect(self.slider_value_changed)
        self.slider.setValue(1)

        layout.addWidget(self.graphics)
        layout.addWidget(self.slider)

        self.setCentralWidget(frame)

    def slider_value_changed(self, value):
        self.item.update_position(value)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
