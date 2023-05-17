class TV:
    def __init__(self, name, volume, channel, is_on):
        self.name = name
        self.volume = volume
        self.channel = channel
        self.is_on = is_on
    
    def view(self):
        print("====================\nTV information\n====================")
        print("TV name: ", self.name, "\nCurrent volume: ", self.volume, "\nCurrent channel: ", self.channel)

        if self.is_on is True:
            print("TV is on?: YES\n")
        else:
            print("TV is on?: NO\n")
    
    def get_volume(self):
        print("The volume of ", self.name, " is ", self.volume)
    
    def get_channel(self):
        print("the current channel of ", self.name, " is ", self.channel)
    
    
    