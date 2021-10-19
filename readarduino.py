import serial
from pymongo import MongoClient
from datetime import datetime

ser = serial.Serial('/dev/ttyACM0', 9700)

f = open('databaseurl.txt', 'r')
URL = f.read()
client = MongoClient(URL)

db = client["SolarRacingData"]
collection = db['BoatData']

def parse_data(line):
    try:
        a = {'RPM': float(line), 'ISOString': datetime.now().isoformat()}
        print(a)
        return a
    except:
        print("Failed to parse")
        return None

if __name__ == "__main__":
    while 1:
        if (ser.in_waiting > 0):
            line = ser.readline()
            currdata = parse_data(line)
            if data:
                try:
                    collection.insert_one(currdata)
                except:
                    pass
            else:
                print("Data invalid")
