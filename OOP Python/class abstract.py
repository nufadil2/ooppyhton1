# abstract mengubah instance class yang default dari objek kepada class
# klo abstarct class akan memaksakan class untuk mengimplementasikan methode nya

# membuat class abstrack

# penggunaan class pada button apabila di absrtackan akan menghilangkan fungsi inheritance
# abc = abstract base class
from abc import ABC, abstractmethod

class Butoon(ABC):

    @abstractmethod
    def click (self): 
        pass # pada sintax ini akan eror apabila method digunakan
        # print("button click")

class PushButton(Butoon):
    

    def click (self):
        print("push button click")

class RadioButton(Butoon):

    def click(self):
        print("radio button click")

# tombol2 = Butoon() # Can't instantiate abstract class Butoon with abstract method click
tombol1 = PushButton()
tombol3 = RadioButton()
# tombol2.click()
tombol1.click()
tombol3.click()

# help(tombol1)

# keggunaan dari abstrack class untuk memkaskan setiap class untuk mengikuti class 
# abstrak dan tidak bisa mengubah method walau printahnya sama

# pada oop digunakan untuk mendesign sebuah struktur