"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start - 1 # Store the initial starting number
        self.beginning = start # Set beginning to the starting number

    def generate(self):
        self.start += 1 # increment the starting value by 1
        return self.start # return new value
    
    def reset(self):
        self.start = self.beginning - 1 # reset the starting value
    

