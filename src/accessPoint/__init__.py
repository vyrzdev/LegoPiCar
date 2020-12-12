from PyAccessPoint import pyaccesspoint


class Network:
    def __init__(self, ip, ssid, password, interface, forwardingInterface=None):
        self.accessPoint = pyaccesspoint.AccessPoint(ip=ip, ssid=ssid, password=password, wlan=interface, inet=forwardingInterface)
        self.accessPoint._write_hostapd_config()
        print("Success!")

    def start(self):
        self.accessPoint.start()
        print("Started!")

    def stop(self):
        self.accessPoint.stop()

    def running(self):
        return self.accessPoint.is_running()