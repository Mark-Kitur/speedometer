import sys
import random,math
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel 
from PyQt5.QtGui import QConicalGradient, QPainter, QColor, QPen, QBrush, QGradient, QPalette
from PyQt5.QtCore  import QTimer, Qt


from speedometer.arduino_data import SerialReader
from speedometer.stick_display import Sticks
from speedometer.display_symbols import DISP_ICON
from speedometer.fuel_tmp import Fuel_Temp



class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.speed = 0

        self.setWindowTitle("Speedometer Dashboard")
        self.setGeometry(0, 0, 1700, 700)
        # set background colour
        palette =self.palette()
        palette.setColor(self.palette().Window, QColor(30,30,30))
        self.setPalette(palette)
        self.setAutoFillBackground(True)
                
       

        # display cureent speed 
        self.speed_label = QLabel(self)
        self.speed_label.setGeometry(150, 150, 200, 200)
        self.speed_label.setStyleSheet("font-size: 20px; color: #00f0ff;") 

        # start serial reader
        # self.serial_reader = SerialReader()
        # self.serial_reader.speed_received.connect(self.update_speed)

        #====== I will begin random visualization before including arduino
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_speed)
        self.timer.start(1000) 

        self.icons = DISP_ICON(self)
        self.icons.setGeometry(500,50,600,500)

        self.fuel = Fuel_Temp(self)
        self.fuel.setGeometry(1100,50, 600,500)

        self.sticks = Sticks(self)
        self.sticks.setGeometry(0,0,500,500)




    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen =QPen()
        pen.setWidth(10)

        # Draw speedometer arc
        # color for outer arc
        painter.setPen(QPen(QColor(0, 100, 100), 10))
        painter.setBrush(QBrush(QColor(0, 100, 100, 100)))
        painter.drawArc(50, 50, 300, 300, 210*16, -240 * 16)

        # set up gradient for speed display
        center_x = 200
        center_y = 200
        gradient = QConicalGradient(center_x, center_y, 270)  # Start angle matches arc
        gradient.setColorAt(0.90, QColor(0, 255, 100))      # Green
        gradient.setColorAt(0.7, QColor(255, 220, 0))      # Yellow
        gradient.setColorAt(0.4, QColor(255, 80, 0))       # Orange
        gradient.setColorAt(0.15, QColor(255, 0, 0))        # Red

        # speed display arc    
        angle = map_speed_to_angle(self.speed)
        pen.setBrush(gradient)
        painter.setPen(pen)
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawArc(70, 70, 260, 260, 210 * 16, -int(angle *16))
        painter.end()

        # draw sticks



    def update_speed(self): # add arg speed later
        rand_speed = random.randint(180,200)
        self.speed =rand_speed
        self.speed_label.setText(f"Speed: {self.speed:.0f}")
        self.update()  # Trigger repaint to update the speedometer


def map_speed_to_angle(speed: float):
    """Map speed to angle in degrees (0 to 240)"""
    min_speed = 0
    max_speed = 200  # adjust to your max speed
    max_angle = 240
    
    if speed < min_speed:
        return 0
    if speed > max_speed:
        return max_angle
    
    see = (speed - min_speed) / (max_speed - min_speed) * max_angle


    return see

app = QApplication(sys.argv)
window = Dashboard()
window.show()
sys.exit(app.exec())