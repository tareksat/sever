import threading
import io
import time
from gpiozero import LED


class FanControl(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.fan = LED(18)

    def run(self):
        while True:
            f = open("/sys/class/thermal/thermal_zone0/temp", "r")
            t = f.readline ()
            temp = float(t) / 1000
            print(temp)
            if temp < 35:
                self.fan.off()
            elif temp > 45 :
                self.fan.on()

            time.sleep(2)
