import sys
from PyQt5.QtCore import QIODevice, QObject, pyqtSignal
from PyQt5.QtSerialPort import QSerialPort


class SerialReader(QObject):
    speed_received = pyqtSignal(float)  # Signal to emit received speed

    def __init__(self, port_name="/dev/ttyACM0", baud_rate=9600):
        super().__init__()
        self.serial = QSerialPort()
        self.serial.setPortName(port_name)
        self.serial.setBaudRate(baud_rate)

        self.serial.readyRead.connect(self.read_serial_data)

        if self.serial.open(QIODevice.OpenModeFlag.ReadWrite):
            print("Serial port opened successfully. Waiting for data...")
        else:
            print("Failed to open serial port.")
        
    def read_serial_data(self):
        data = self.serial.readAll().data()
        if data:
            try:
                speed = float(data.decode('utf-8').strip())
                #print(f"Received speed: {speed} km/h")
                self.speed_received.emit(speed)  
            except ValueError:
                pass
                #print("Received non-numeric data:", data)

    def close(self):
        if self.serial.isOpen():
            self.serial.close()
            print("Serial port closed.")