class rectengle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    @property
    def area(self):
        return self.length * self.width
    @property
    def perimeter(self):
        return 2 * (self.length + self.width)
h1=rectengle(1000000000000000,10)
print("Area:",h1.area)
print("Perimeter:",h1.perimeter)