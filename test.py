
class Computer:
    def __init__(self, hardware, software):
        self.hardware = hardware
        self.software = software

    def get_software(self): # this is an example of an accessor
        return self.software
    
    def get_hardware(self):
        return self.hardware
