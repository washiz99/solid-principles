from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):

    @abstractmethod
    def draw_circle(self):
        pass

    @abstractmethod
    def draw_square(self):
        pass


class Circle(Shape):

    def draw_circle(self):
        print('まるを描きます')

    def draw_square(self):
        """ no need logic """
        pass


circle = Circle()
circle.draw_circle()


"""
Circleクラスは、ShapeというInterfaceを継承しているため、
Circleクラスには、不要なdraw_squareの記載が必要
draw_squareを書かないとエラーなる。

不要なロジックを書かずに新しいクラスを作成するにはどうしたらいいのか？
ISPを守ることで解決できる。
"""