from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):

    def draw(self):
        print('まるを描きます')

class Square(Shape):
    def draw(self):
        print('しかくを描きます')


circle = Circle()
circle.draw()

square = Square()
square.draw()