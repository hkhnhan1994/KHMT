"""
Đề thi 2021 Đợt 2
Câu 2
"""
"""Add Abstract Class."""
from abc import ABC, abstractmethod
class entity(ABC):
    """abstract class define an entity of the Structure."""
    @abstractmethod
    def __init__():
        """abstracted Constructor."""
        pass
    @abstractmethod
    def getsize():
        """pure abstracted method"""
        pass

class File(entity):
    """Define File."""
    def __init__(self, name):
        """Constructor."""
        self.name=name
        self.level=1
    def getsize(self):
        """Getsize method for file, size always equal 1"""
        return 1
    def gettype(self):
        return self.level
class  Folder(entity,Exception):
    """Define Folder."""
    def __init__(self,name,element:list[entity]=None):
        """Constructor."""
        self.name=name  
        try:
            for e in element:
                if e.gettype()==3:
                    raise _error
        except _error:
            print("A folder can not contain a drive")
            return -1
        self.list=element
        self.level=2
    def getsize(self):
        result=0
        for element in self.list:
            result+=element.getsize()
        return result
    def gettype(self):
        return self.level
class Drive(entity):
    """Define Drive."""
    def __init__(self,name,element:list[entity]=None):
        """Constructor."""
        self.name=name
        try:

            for e in element:
                if e.gettype()==3:
                    raise error
        except error:
            print("A drive can not contain a drive")
            return -1
        self.list=element
    def getsize(self):
        result=0
        for element in self.list:
            result+=element.getsize()
        return result
doc1=File("reader.doc")
doc2=File("tax.vsc")
doc3=File("hello1.jpg")
doc4=File("game.exe")
folder1=Folder("list1",[doc1,doc2])
folder2=Folder("List2",[folder1,doc3])
Drive2=Drive("drive2",[folder1,folder2,doc4])
Drive1=Drive("drive1",[Drive2,folder2,doc4])
print(Drive1.getsize())
