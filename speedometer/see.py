import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class See(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(10,10,640,640)
        self.UI_()

    def UI_(self):
        label = QLabel(self)

        path = str('icons/abs.png')
        img = QPixmap('icons/abs.png')
        label.setPixmap(img)
        #print(path)


if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = See()
    window.show()
    sys.exit(app.exec())