class Weather:
    def __init__(self, doy, temperature, wetting, humidity, rain):
        self.doy = doy
        self.temperature = temperature
        self.wetting = wetting
        self.humidity = humidity
        self.rain = rain

class Event:
    def __init__(self,index, x):
        self.index = index
        self.x = x
