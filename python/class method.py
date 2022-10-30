from datetime import date#
#random Nhanvien
class Nhanvien:    
    def __init__(self, ten, tuoi):        
        self.ten = ten        
        self.tuoi = tuoi    
    @classmethod    
    def fromBirthYear(cls, ten, birthYear):
        # inputs are a class with parameters of the class itself        
        return cls(ten, date.today().year - birthYear)    
    def ketqua(self):        
        print("Tuổi của " + self.ten + " là: " + str(self.tuoi))
nhanvien = Nhanvien('Alice', 23)
nhanvien.ketqua()
nhanvien1 = Nhanvien.fromBirthYear('Simon', 1990)
nhanvien1.ketqua()