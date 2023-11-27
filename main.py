import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random
import sys
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('circles.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.drawCircle)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircles(qp)
        qp.end()

    def drawCircles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        qp.drawEllipse(x, y, diameter, diameter)

    def drawCircle(self):
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
