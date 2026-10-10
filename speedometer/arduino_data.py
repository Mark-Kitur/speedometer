import os 
import random

# read_data from character device /dev/raspi_master
dev = os.open("/dev/raspi_master",os.O_RDONLY)

car_values = {}
def read_data():
    global car_values

    try:
        data = os.read(dev,64)
        #data = [120,1,0,1,0,0,1,7,7,0,1,1,0]
        #read data store them in a dictionary
        car_values.update( {
            'speed'       : data[0],
            'abs'         : data[1],
            'airbag'      : data[2],
            "battery"     : data[3],
            'checkEngine' : data[4],
            'doorOpen'    : data[5],
            'headLights'  : data[6],
            'fuelLevel'   : data[7],
            'temperature' : data[8],
            'oilLevel'    : data[9],
            'seatBelt'    : data[10],
            'sterringWheel': data[11],
            'tirePressure' : data[12],
        })
        #print(car_values)

    except OSError as error:
        print(f"Device read failed: {error}")

    

