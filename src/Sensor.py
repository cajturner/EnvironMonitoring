from pisense import SenseHAT
from opentsdb import OpenTSDBClient

class Sensor:

    def __init__(self):
        self.hat = SenseHAT(emulate=True)
        self.hat.screen.clear()
        self.hat.environ._interval = 1
        self.running = False
        self.opentsdb = OpenTSDBClient()

    def loop(self):
        self.running = True
        for reading in self.hat.environ:
            self.opentsdb.log_temperature(reading.temperature)
            self.opentsdb.log_humidity(reading.humidity)
            self.opentsdb.log_pressure(reading.pressure)


if __name__ == '__main__':
    s = Sensor()
    s.loop()
