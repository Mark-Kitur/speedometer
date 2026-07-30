#draw sticks for speedometer
from PyQt5.QtWidgets import QMainWindow, QApplication,       QWidget
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
import sys, math
from PyQt5.QtCore import Qt


class Sticks(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sticks")
        self.setGeometry(0, 0, 500, 500)
        self.setStyleSheet("background-color: #121214;")


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen = QPen()
        pen.setWidth(10)
        painter.setPen(pen)

        # Draw speedometer arc
        painter.setPen(QPen(QColor(0, 100, 100), 10))
        painter.setBrush(QBrush(QColor(0, 100, 100, 100)))
        painter.drawArc(50, 50, 300, 300, 210*16, -360 * 16)    

        # drwa sticks
        painter.setPen(QPen(QColor(220,220,230), 5))
        font = painter.font()
        font.setPointSize(10)
        font.setBold(True)
        painter.setFont(font)
        
        center_x = 200
        center_y = 200
        radius_outer = 155
        radius_inner = 130
        radius_text = 175   # for numbers
        max_speed = 210

        for i in range(0, max_speed ,10):
            speed_ratio = i/max_speed
            angle = -(212 - (speed_ratio * 257))       
            
            #convert angle to radians
            angle_rad = math.radians(angle)

            if i % 10 == 0:
                painter.setPen(QPen(QColor(220,220,230), 5))
                x2  = center_x + (radius_outer+8) * math.cos(angle_rad)
                y2  = center_y + (radius_outer+8) * math.sin(angle_rad)

                x1 = center_x + radius_inner * math.cos(angle_rad)
                y1 = center_y + radius_inner * math.sin(angle_rad)
                x2 = center_x + radius_outer * math.cos(angle_rad)
                y2 = center_y + radius_outer * math.sin(angle_rad)

                text_x = center_x + radius_text * math.cos(angle_rad)
                text_y = center_y + radius_text * math.sin(angle_rad)

                painter.drawText(int(text_x-10), int(text_y+5), str(i))

                painter.setPen(QPen(QColor(220,220,230), 3))

            else:
                painter.setPen(QPen(QColor(220,220,230), 3))
                
            painter.drawLine(int(x1), int(y1), int(x2), int(y2))

        painter.end()



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Sticks()
#     window.show()
#     sys.exit(app.exec())
