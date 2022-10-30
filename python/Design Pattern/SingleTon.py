
class SingleTon:
    _count_object=0
    CONSTANT_NUMBER=3
    def __init__(self,val):
        if SingleTon._count_object<SingleTon.CONSTANT_NUMBER:
            self.obj=val
            SingleTon._count_object+=1
        else:
            print("meet limit of quantity of the creating object < 3 numbers")

Object1=SingleTon(1)
Object1=SingleTon(2)
Object1=SingleTon(3)
Object1=SingleTon(4)