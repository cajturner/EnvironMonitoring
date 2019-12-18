import potsdb

class OpenTSDBClient:

    def __init__(self):
        self.client = potsdb.Client('localhost')

    def _send(self, metric_path, metric_value):
        self.client.send(metric_path, metric_value)

    def log_temperature(self, temperature):
        self._send('test.temperature', temperature)

    def log_humidity(self, humidity):
        self._send('test.humidity', humidity)

    def log_pressure(self, pressure):
        self._send('test.pressure', pressure)