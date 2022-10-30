class person:
    def __init__(self, name,old,id):
        self.name=name
        self.old=old
        self._id=id

class man(person):
    def __init__(self,name,old,id):
        super().__init__(name,old,id)
    def printID(self):
        return self._id

groupman:person

groupman.append(man("N",1,10))
groupman.append(man("Q",1,11))

for i in groupman:
    print(i.printID())
