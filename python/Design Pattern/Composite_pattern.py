"""Import module abstraction method"""
import abc

class component(abc.ABC):
    @abc.abstractmethod
    def get_size(self):
        pass

class File(component):
    def __init__(self, name,size):
        self.__name=name
        self._size=size
    def get_size(self):
        return self._size

class Folder(component):
    def __init__(self, name, component):
        self.__name=name
        self.__component=component
    def get_size(self):
        size=0
        for ele in self.__component:
            size+=ele.get_size()
        return size
class Drive:
    def __init__(self,name, component):
        self.__name=name
        self.__component=component
    def get_size(self):
        size=0
        for ele in self.__component:
            size=size+ele.get_size()
        return size
if __name__ =='__main__':
    doc1=File("doc1",1)
    doc2=File("doc2",1)
    doc3=File("doc3",1)
    doc4=File("doc4",1)
    folder1=Folder("folder1",[doc1,doc2])
    folder2=Folder("folder2",[doc3,doc4])
    folder3=Folder("folder2",[folder1,folder2])
    drive1=Drive("drive1",[folder3])
    drive2=Drive("drive2",[drive1,folder3])
    print(drive2.get_size())