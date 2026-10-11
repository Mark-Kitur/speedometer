
import os

DEVICE = "/dev/raspi_master"

car_values = {}
#values =[0,0,0,0,0,0,0,0,0,0,0,0,0]
def read_data():
    global car_values
    try:
        fd = os.open(DEVICE, os.O_RDONLY)
        try:
            raw_data = os.read(fd, 128)
        finally:
            os.close(fd)

        # Convert ASCII bytes to integer values
        values = [int(value) for value in raw_data.decode("ascii").split()]

        if len(values) != 13:
            print(f"Expected 13 values, received {len(values)}: {values}")
            return

        car_values = {
            "speed": values[0],
            "abs": values[1],
            "airbag": values[2],
            "battery": values[3],
            "checkEngine": values[4],
            "doorOpen": values[5],
            "headLights": values[6],
            "fuelLevel": values[7],
            "temperature": values[8],
            "oilLevel": values[9],
            "seatBelt": values[10],
            "sterringWheel": values[11],
            "tirePressure": values[12],
        }

    except (OSError, UnicodeDecodeError, ValueError) as error:
        print(f"Arduino data read failed: {error}")
