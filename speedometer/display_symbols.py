from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QGridLayout, QWidget, 
                           QApplication, QLabel, QVBoxLayout)
from PyQt5.QtCore import Qt, QTimer
import sys
import random  


class DashboardIcon(QWidget):
    """Reusable widget for each dashboard icon"""
    def __init__(self, icon_path, label_text):
        super().__init__()
        self.is_active = False
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Icon Label
        self.icon_label = QLabel()
        self.pixmap = QPixmap(icon_path)
        if not self.pixmap.isNull():
            self.icon_label.setPixmap(self.pixmap.scaled(72,72, Qt.AspectRatioMode.KeepAspectRatio))
        else:
            self.icon_label.setText("NULL")
            self.icon_label.setStyleSheet("font-size: 48px; color: white;")
        
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Text Label
        self.text_label = QLabel(label_text)
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label.setStyleSheet("font-size: 12px; font-weight: bold; color: white;")
        
        layout.addWidget(self.icon_label)
        layout.addWidget(self.text_label)
        self.setLayout(layout)
        
        self.setFixedSize(120, 110)
        self.update_style()
    
    def update_style(self):
        """Change appearance when active (warning on)"""
        if self.is_active:
            self.setStyleSheet("""
                QWidget {
                    background-color: rgba(255, 50, 50, 80);
                    border: 2px solid #ff4444;
                    border-radius: 12px;
                }
            """)
        else:
            self.setStyleSheet("""
                QWidget {
                    background-color: rgba(40, 40, 40, 120);
                    border: 1px solid #555;
                    border-radius: 12px;
                }
            """)
    
    def trigger(self, state: bool):
        """Turn warning on/off"""
        self.is_active = state
        self.update_style()


class DISP_ICON(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dashboard")

        self.icons = {
            'icons/abs.png': 'abs',
            'icons/air-bag_13401736.png': 'airbag',
            'icons/battery.png': 'bat',
            'icons/check_engine.png': 'check eng',
            'icons/door_open.png': 'door open',
            "icons/head_lights.png": 'head lights',
            'icons/oil-indicator_1633107.png': 'check oil',
            'icons/seat_belt.png': 'belt',
            'icons/streering_dis.png': 'streering',
            'icons/tire-pressure_6380752.png': 'tire'
        }

        self.active_widgets = {}
        self.disp_icons()

        # NEW: Timer to trigger random updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.trigger_random_warnings)
        self.timer.start(1000)  # Fires every 1.0 second

    def disp_icons(self):
        self.main_layout = QGridLayout(self)
        
        for i, (path, name) in enumerate(self.icons.items()):
            row = i // 5
            col = i % 5

            icon_widget = DashboardIcon(path, name)
            self.main_layout.addWidget(icon_widget, row, col)
            self.active_widgets[name] = icon_widget

        self.setLayout(self.main_layout)

  
    def trigger_random_warnings(self):
        """Randomly toggles the warning state of all registered icons"""
        for name, icon_widget in self.active_widgets.items():
           
            random_state = random.choice([True, False])
            icon_widget.trigger(random_state)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DISP_ICON()
    window.show()
    sys.exit(app.exec())
