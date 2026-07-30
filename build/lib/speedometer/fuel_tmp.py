import sys
import math
import random
import time
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QProgressBar, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QFont
from PyQt5.QtCore import QPoint, QTimer, Qt

class Fuel_Temp(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(0, 0, 600, 500)
        self.temp = 25
        
        # Premium dark background style
        self.setStyleSheet("background-color: #121214;")

        # start to simulate timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_state)
        self.timer.start(4000)

        # Progress bar styled with modern flat design
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(10)
        self.progress_bar.setFixedHeight(14)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: #1E1E22;
                border: 1px solid #2D2D35;
                border-radius: 7px;
            }
            QProgressBar::chunk {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00E5FF, stop:1 #0088FF);
                border-radius: 6px;
            }
        """)

        # Labels for the Fuel row
        self.fuel_title_label = QLabel("FUEL:")
        self.fuel_title_label.setStyleSheet("color: #8E9297; font-weight: bold; font-family: 'Segoe UI', Arial; font-size: 14px;")
        
        self.fuel_val_label = QLabel("0/10")
        self.fuel_val_label.setStyleSheet("color: #00E5FF; font-weight: bold; font-family: 'Segoe UI', Arial; font-size: 14px;")
        self.fuel_val_label.setFixedWidth(50)
        self.fuel_val_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Fuel Horizontal Layout
        fuel_layout = QHBoxLayout()
        fuel_layout.addWidget(self.fuel_title_label)
        fuel_layout.addWidget(self.progress_bar)
        fuel_layout.addWidget(self.fuel_val_label)

        # Main Vertical Layout to contain spacing and the lower fuel components cleanly
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 50, 40)
        main_layout.addSpacing(320) # Pushes layout down below the custom painted gauge area
        main_layout.addLayout(fuel_layout)
        
        self.setLayout(main_layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen = QPen()
        pen.setWidth(10) # Set to a clean, highly visible stroke width
        pen.setCapStyle(Qt.PenCapStyle.RoundCap) # Round caps blend adjacent arcs cleanly

        # Precise arc renderings using original coordinates and angular boundaries
        pen.setColor(QColor("#FF3366")) # Deep tech Red
        painter.setPen(pen)
        painter.drawArc(50, 50, 200, 200, 345 * 16, 60 * 16)
        
        pen.setColor(QColor("#FFCC00")) # Vivid tech Yellow
        painter.setPen(pen)
        painter.drawArc(50, 50, 200, 200, 55 * 16, 65 * 16)
        
        pen.setColor(QColor("#00E676")) # Electric tech Green
        painter.setPen(pen)
        painter.drawArc(50, 50, 200, 200, 135 * 16, 60 * 16)

        # Draw text labels for the Temperature gauge bounds
        painter.setPen(QPen(QColor("#8E9297")))
        painter.setFont(QFont("Segoe UI", 11, QFont.Weight.DemiBold))
        painter.drawText(30, 155, "C")  # Cold marker near Green segment
        painter.drawText(260, 155, "H") # Hot marker near Red segment

        # # Draw live numerical Temp value inside/below the cluster hub
        # painter.setPen(QPen(QColor("#FFFFFF")))
        # painter.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        # painter.drawText(115, 290, f"TEMP: {self.temp}°")

        # draw needle pointer using original math formulations
        angle = math.radians(self.temp)
        length = 90
        cf = 150
        x = cf + length * math.cos(angle)
        y = cf - length * math.sin(angle)
        
        # High contrast white pointer needle with safe round styling caps
        needle_pen = QPen(QColor("#FFFFFF"), 5)
        needle_pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(needle_pen)
        painter.drawLine(QPoint(cf, cf), QPoint(int(x), int(y)))

        # Needle hub (center circle) - modern multi-tone circular layered style
        painter.setBrush(QBrush(QColor("#1E1E22")))
        painter.setPen(QPen(QColor("#00E5FF"), 3))
        painter.drawEllipse(cf - 12, cf - 12, 24, 24)

        painter.end()

    def update_state(self):
        value_int = random.randint(0, 195)
        self.temp = 195 - value_int
        fuel = random.randint(0, 10)
        
        self.progress_bar.setValue(fuel)
        self.fuel_val_label.setText(f"{fuel}/10") # Dynamic string label update
        
        print(value_int, self.temp)
        self.update()

# app = QApplication(sys.argv)
# window = Fuel_Temp()
# window.show()
# sys.exit(app.exec())
