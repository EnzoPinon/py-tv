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

    def set_channel(self, new_channel):
        if not type(new_channel) is int:
            print("The new channel must be an integer.")
        else:
            self.channel = new_channel
            print("The new channel of ", self.name, " is now: ", new_channel)
    
    def set_volume(self, new_volume):
        if not type(new_volume) is int:
            print("The new volume must be an integer.")
        else:
            if new_volume >= 0 and new_volume <= 100:
                self.volume = new_volume
                print("The new volume of ", self.name, " is now: ", new_volume)
            else:
                print("the volume receives is not in an acceptable range of 0-100")
    
    def turn_on(self):
        self.is_on = True
        print(self.name, " has been switched on!")
    
    def turn_off(self):
        self.is_on = False
        print(self.name, " has been switched off!")

    def rename(self, new_name):
        if not type(new_name) is str:
            print("The new name of this TV must be a string.")
        else:
            print("The new name of ", self.name, " is now: ", new_name)
            self.name = new_name

    def volume_up(self):
        self.volume = self.volume + 1
        print("The volume of ", self.name, " is raised to: ", self.volume)

    def volume_down(self):
        self.volume = self.volume - 1
        print("The volume of ", self.name, " is lowered to: ", self.volume)            