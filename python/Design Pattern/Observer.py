import abc
class Observer(abc.ABC):
    @abc.abstractmethod
    def update():
        pass
class Frame(Observer):
    def update():
        return 1
class Window(Observer):
    def update():
        return 1
class Button:
    def __init__(self):
        self.__observer:list[Observer]
    def addObserver(self, obs:Observer):
        self.__observer.append(obs)
    def removeObserver(self,obs:Observer):
        self.__observer.remove(obs)
    def notify(self):
        for o in self.__observer:
            print(o.update())

if __name__=='__main__':
    frame1=Frame()
    Window1=Window()
    But=Button()
    But.addObserver(frame1)
    But.addObserver(Windows1)
    But.notify()