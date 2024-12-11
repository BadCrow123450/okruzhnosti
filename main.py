from PyQt6 import QtWidgets, uic
import io
import sys
import random
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPointF


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>507</width>
    <height>435</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>370</x>
     <y>400</y>
     <width>131</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>push to create circle</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MainW(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.random_circle)
        self.need_draw = False

    def random_circle(self):
        self.update()

    def paintEvent(self, a0):
        if self.need_draw:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QColor(255, 255, 0))
            radius = random.randint(20, 200)
            painter.drawEllipse(QPointF(250, 250), radius, radius)
            painter.end()
        else:
            self.need_draw = True



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MainW()
    ex.show()
    sys.exit(app.exec())
