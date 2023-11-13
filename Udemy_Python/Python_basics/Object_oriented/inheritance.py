#Inheritance - Child class can use methods and properties of parent class or super class

class Device:
    def __init__(self, name,connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    def __str__(self):
        return f"Device {self.name} connected by ({self.connected_by})"
    def disconnect(self):
        self.connected = False
        print("Disconneted")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} remaining pages)"
    def print_it(self,pages):
        if not self.connected:
           print("Printer not connected ")
           return
                      
        print(f"Printing {pages} pages")
        self.remaining_pages -= pages
        



printer = Printer("printer", "usb",100)
print(printer.print_it(30))
print(printer)
printer.disconnect()
print(printer.print_it(30))