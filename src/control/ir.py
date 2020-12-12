from subprocess import run


def sendCommand(command):
    longForm = ["irsend", "SEND_ONCE", "LEGO_Combo_Direct", command]
    run(longForm)