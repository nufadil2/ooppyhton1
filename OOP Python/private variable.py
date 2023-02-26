"""
pemberian akses kepada variable secara private untuk encapsulasi
agar tidak kebanyakan atau ada variable yang diprotek kepada user

"""

class Hero:

    #class variable
    jumlah = 0
    __privateJumlah = 0

    # jumlah variable
    def __init__(self,name,health) -> None:
        self.name=name
        self.health=health

        # variable instance private
        self.__private = "private"

        # variable instance protected
        self._protected = "protected"

lina = Hero("lina",100)

print(lina.__dict__)

print(lina.health)

# print(lina.__private) << tidak bisa akses error

# print(Hero.__privateJumlah) << tidak bisa akses error untuk class