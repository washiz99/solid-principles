class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        self._width = width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        self._height = height
    
    def area(self):
        return self._width * self._height


class Square(Rectangle):

    def __init__(self, size):
        self._width = size
        self._height = size

    @Rectangle.width.setter
    def width(self, size):
        self._width = size
        self._height = size
    
    @Rectangle.height.setter
    def height(self, size):
        self._width = size
        self._height = size


class CalcArea:

    def verify_area(self, r: Rectangle):
        r.width = 5
        r.height = 4
 
        if r.area() != 20:
            raise Exception('Bad area!')
        return True


c = CalcArea()

r = Rectangle(2, 3)
if c.verify_area(r):
    print('OK')

s = Square(5)
if c.verify_area(s):
    print('OK')
