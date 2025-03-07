class ControlTV:
    def __init__(self):
        self.is_on = False
        self.is_mute = False
        self.volume = 15
        self.volumeMAX = 20
        self.channels = [range(0, 101)]
        self.channel = 10

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        if not self.is_on:
            return 
        self.is_on = False
    
    def mute(self):
        if not self.is_on:
            return 
        self.mute = True

    def up_volume(self):
        if not self.is_on:
            return 
        if self.is_mute:
            self.is_mute = False
        if self.volume > self.volumeMAX:
            self.volume = self.volumeMAX
            return 
        self.volume += 1
    
    def low_volume(self):
        if not self.is_on:
            return
        if self.is_mute:
            self.is_mute = False
        if self.volume <= 0:
            self.volume = 0
            self.is_mute = True
            return
        self.volume -= 1
    
    def up_channel(self):
        if not self.is_on:
            return
        if self.channel > 100:
            self.channel = 0
            return
        self.channel += 1
    
    def low_channel(self):
        if not self.is_on:
            return
        if self.channel < 0:
            self.channel = 100
            return
        self.channel -= 1
    
    def find_channel(self, channel: int):
        if not self.is_on:
            return
        if channel < 0 or channel > 100:
            print(f"Channel {channel} not find")
        if int(channel) in self.channel:
            self.channel = channel
        
    def info(self):
        if self.is_on:
            info = f"""Mute: {'✅ On' if self.is_mute else '❌ Off'}\nVolume: {self.volume}\nChannel: {self.channel}"""
            return info