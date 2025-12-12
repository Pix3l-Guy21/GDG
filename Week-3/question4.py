#No4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = f'Area of rectangle {width*height}'

print(Rectangle(5, 2).area)