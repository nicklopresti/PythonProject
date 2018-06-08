class Shape:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    type = "square"
    def area(self):
        return self.width * self.length
    def perimeter(self):
        return 2 * self.width + 2 * self.length
    def describe(self, text):
        self.type = text
    def scaleSize(self, scale):
        self.width = self.width * scale
        self.length = self.length * scale


s1 = Shape(567, 598545454522890034)

area = int(s1.area())

perimeter = int(s1.perimeter())

describe = s1.describe("Python")

print("the area is " + str(area))
