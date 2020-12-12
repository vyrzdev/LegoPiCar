from . import ir


class Car:
    def __init__(self, friendlyName):
        self.friendlyName = friendlyName
        self.outputs = {
            "left": list(),
            "right": list()
        }

    def register_output(self, outputObject):
        if outputObject.position == "left":
            self.outputs["left"] = outputObject
        elif outputObject.position == "right":
            self.outputs["right"] = outputObject
        else:
            raise ValueError

    @staticmethod
    def buildCommand(left, right):
        return f"{left}_{right}"

    def forward(self):
        left = self.outputs.get("left").forward()
        right = self.outputs.get("right").forward()
        command = Car.buildCommand(left, right)
        ir.sendCommand(command)

    def right(self):
        left = self.outputs.get("left").forward()
        right = self.outputs.get("right").backward()
        command = Car.buildCommand(left, right)
        ir.sendCommand(command)

    def left(self):
        left = self.outputs.get("left").backward()
        right = self.outputs.get("right").forward()
        command = Car.buildCommand(left, right)
        ir.sendCommand(command)

    def backward(self):
        left = self.outputs.get("left").backward()
        right = self.outputs.get("right").backward()
        command = Car.buildCommand(left, right)
        ir.sendCommand(command)