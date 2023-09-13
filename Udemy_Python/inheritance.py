

class Device:
    def __init__(self,name,connected_by):
        self.name = name
        self.connected_by=connected_by
        self.connected = True
    def __str__(self):
        return f"Device {self.name} is connected by {self.connected_by}"
    def Disconnected(self):
        self.connected = False
        print("Disconnected")

class Printer(Device):
    def __init__(self,name,connected_by,capacity):
        super().__init__(name,connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity
    def __str__(self):
        return f"{super().__str__()}({self.remaining_pages} pages remaining)"
    def print(self,pages):
        if not self.connected:
            print("Printer no connected")
        print(f"Printing {pages} pages")
        self.remaining_pages -=pages


printer = Printer('printer','usb',500)
print(printer)
printer.print(200)
print(printer)
printer.Disconnected()