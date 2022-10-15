from abc import abstractmethod


class Shape:
    pass
class DrawingShape:
    pass
class Shape:
    def __init__(self,ds:DrawingShape):
        self._drawer=ds
    @abstractmethod
    def draw():
        pass
class DrawingShape:
    @abstractmethod
    def draw(self,s:Shape):
        pass

class Rectangle(Shape):
    def __init__(self, x,y,w,h,ds:DrawingShape):
        super().__init__(ds)
        self.x=x
        self.y=y
        self.width=w
        self.heigh=h
    def draw(self):
        self._drawer

