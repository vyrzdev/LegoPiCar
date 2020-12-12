from . import control, accessPoint
import logging
import subprocess
from time import sleep
import atexit

def cleanupHostAPD():
      LocalWiFi.stop()

atexit.register(cleanupHostAPD)
hostIP = "192.168.2.1"  # Must be same as in dnsmasq.conf to do captive portal.
netInterface = "wlan0"  # Must be same as in dnsmasq.conf to do captive portal.
subprocess.call(["sudo", "systemctl", "stop", "hostapd"])


# Car Definition
car = control.model.Car("Seb's LEGO Car")
leftWheel = control.output.Output("Left Wheel", "left", reversed=True)
rightWheel = control.output.Output("Right Wheel", "right")
car.register_output(leftWheel)
car.register_output(rightWheel)


LocalWiFi = accessPoint.Network(hostIP, "LEGO Car", "ImSorryDave", netInterface)
LocalWiFi.start()
print(LocalWiFi.running())
print("Trace")
LocalWiFi.stop()
LocalWiFi.start()
sleep(1)

from .web import app

app.run(host="0.0.0.0", port=80)
