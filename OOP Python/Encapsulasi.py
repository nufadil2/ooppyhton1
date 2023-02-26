"""
1. buat semua variable private
2. getter (menggambil variable )dan setter(mensettign variable)
3. selama permainan tidak bisa berubah untuk permainan
4. setter bisa mengubah dengan batasan

"""

class Hero:

    def __init__(self,name,health,attackPower) -> None:
        self.__name = name
        self.__health = health
        self.__attPower = attackPower


    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter

    def diserang(self,serangPower):
        self.__health -= serangPower

    def setAttpower(self,nilaibaru):
        self.__attPower = nilaibaru

earthshaker = Hero("earthshaker",50,5)
print(earthshaker.__dict__)

# game berjalan

print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.diserang(5)
print(earthshaker.getHealth())
