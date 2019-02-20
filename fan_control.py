import threading
import io
import time
from gpiozero import PWMLED


class FanControl(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.fan = PWMLED(18)

    def run(self):
        while True:
            f = open("/sys/class/thermal/thermal_zone0/temp", "r")
            t = f.readline ()
            temp = float(t) / 1000
            print(temp)
            if temp < 35:
                self.fan.value = 0
            elif temp > 35 and temp < 40:
                self.fan.value = 0.7
            elif temp > 40:
                self.fan.value = 1
            time.sleep(2)
