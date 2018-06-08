class Shape:
    def _init_(self, x, y):
       self.x = x
       self.y = y
    type = "Shape type not assigned yet"
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self, text):
        self.type = text
    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale
