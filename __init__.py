import random
import time
import psutil
from DLG import *

def battery_alert():
    while True:
        time.sleep(10)
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent < 30:
            random_low = random.choice(low_b)
            return random_low

        elif percent < 10:
            random_low = random.choice(last_low)
            return random_low

        elif percent == 100:
            random_low = random.choice(full_battery)
            return random_low
        else:
            pass

        time.sleep(1500)

def check_plugin_status():
    battery = psutil.sensors_battery()
    previous_state = battery.power_plugged

    while True:
        battery = psutil.sensors_battery()

        if battery.power_plugged != previous_state:
            if battery.power_plugged:
              random_low = random.choice(plug_in)
              return random_low
            else:
              random_low = random.choice(plug_out)
              return random_low

            previous_state = battery.power_plugged

def battey_persentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    return (f"the device is running on {percent}% battery power")
    
