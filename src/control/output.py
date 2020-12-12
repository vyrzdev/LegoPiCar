class Output:
    def __init__(self, friendlyName, position, reversed=False):
        self.friendlyName = friendlyName
        if position in ["left", "right"]:
            self.position = position
        else:
            raise ValueError

        if reversed is True:
            self.commands = {
                "forward": "BACKWARD",
                "backward": "FORWARD",
                "off": "FLOAT",
                "brake": "BRAKE"
            }
        else:
            self.commands = {
                "forward": "FORWARD",
                "backward": "BACKWARD",
                "off": "FLOAT",
                "brake": "BRAKE"
            }

    def forward(self):
        return self.commands.get("forward")

    def backward(self):
        return self.commands.get("backward")

    def brake(self):
        return self.commands.get("brake")

    def off(self):
        return self.commands.get("off")