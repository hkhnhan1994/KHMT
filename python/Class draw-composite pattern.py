"""
Đề thi 2020 đợt 1
Câu 3
"""
from abc import ABC, abstractmethod
"""predefine abstract class"""
class Shape(ABC):
    pass
class DrawingShape(ABC):
    @abstractmethod
    def draw(self,s: Shape)->None:
        pass

class Shape(ABC):
    def __init__(self, _drawer:DrawingShape):
        self.drawer=_drawer
    def Shape(self,ds: DrawingShape):
        pass
    @abstractmethod
    def draw()-> None:
        pass
class DrawingCircle(DrawingShape):
    def draw(self, s:Shape)->None:
        pass
class DrawingRectangle(DrawingShape):
    def draw(self,s: Shape):
        pass
class Rectangle(Shape):
    def __init__(self, x:int,y:int,width:int,height:int,ds:DrawingShape):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.ds=ds
    def draw(self):
        print(f"point1 [{self.x},{self.y}]")