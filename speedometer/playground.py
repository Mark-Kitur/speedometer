"""
this lab file for testing code before I add to main file
"""

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt, QTimer
import sys
import random



from speedometer.arduino_data import SerialReader
from speedometer.stick_display import Sticks
from speedometer.display_symbols import DISP_ICON
from speedometer.fuel_tmp import Fuel_Temp




class TestArc(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.setGeometry(0,0,1700,700)
        self.num=0
        self.setStyleSheet("background-color: #121214;")

        self.timer = QTimer()
        self.timer.timeout.connect(self.updatearc)
        self.timer.start(1000)

        self.label = QLabel(self)
        self.label.setGeometry(150,150,200,200)
        self.label.setStyleSheet("font-size: 20px; color: #000000;") 

        self.timer = QTimer()
        self.timer.timeout.connect(self.updatearc)
        self.timer.start(1000) 

        self.icons = DISP_ICON(self)
        self.icons.setGeometry(500,50,600,500)

        self.fuel = Fuel_Temp(self)
        self.fuel.setGeometry(1100,50, 600,500)

        self.sticks = Sticks(self)
        self.sticks.setGeometry(0,0,500,500)




    def paintEvent(self,event):
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen =   QPen()
        pen.setWidth(10)

        paint.setPen(QPen(QColor(0,100,100),10))
        paint.setBrush(QBrush(QColor(0,100,100,100)))
        paint.drawArc(50,50,300,300, 210*16, -240*16)

        #variable arc
        pen.setBrush(QColor(56,213,105))
        paint.setPen(pen)
        paint.setBrush(Qt.BrushStyle.NoBrush)
        paint.drawArc(70,70,260,260, 210*16, -int(self.num*16))

        paint.end()

    def updatearc(self):
        #number = random.randint(0,240)
        self.num =random.randint(200,241)
        self.label.setText(f"spedd:{self.num:.0f}")
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win= TestArc()
    win.show()
    sys.exit(app.exec())



