class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        print (self.width * self.height)

res = Rectangle(5, 3)
res.get_area()