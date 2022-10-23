import abc 
class Shape(abc.ABC):
    pass
class DrawingShape(abc.ABC):
    pass
class Shape(abc.ABC):
    def __init__(self,ds:DrawingShape):
        self._drawer=ds
    @abc.abstractmethod
    def draw(self):
        pass
class DrawingShape(abc.ABC):
    abc.abstractmethod
    def draw(self,s:Shape):
        pass
class Rectangle(Shape):
    def __init__(self,x,y,w,h,ds:DrawingShape):
        super().__init__(ds)
        self.__x=x
        self.__y=y
        self.__width=w
        self.__height=h
    def draw(self):
        self._drawer.draw(self)
class Circle(Shape):
    def __init__(self,x,y,radius, ds: DrawingShape):
        super().__init__(ds)
        self.__x=x
        self.__y=y
        self.__radius=radius
    def draw(self):
        self._drawer.draw(self)
class DrawingCircle(DrawingShape):
    def draw(self, s: Shape):
        return super().draw(s)
class DrawingRectangle(DrawingShape):
    def draw(self,s:Shape):
        return super().draw(s)

if __name__=="__main__":
    s:Shape=[]
    dr= DrawingRectangle()
    dc= DrawingCircle()
    s.append(Rectangle(1,2,3,4,dr))
    s.append(Rectangle(5,6,7,8,dr))
    s.append(Circle(9,9,9,dc))
    for i in s:
        print(i.draw())
    del dr
    del dc
    for i in s:
        del i
