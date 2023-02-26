class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan health: {}".format(self.name,self.health))

class Hero_intelligent(Hero):
    def __init__(self, name):
        # Hero.__init__(self,name,100) << contoh syntax yang bisa digunakan
        # self.name= name   # contoh syntax bentukan pengulangan terhadap 
                            # super class dan harus 
                            # dihindari pada pemorgraman
        # self.health=100
        super().__init__(name,100) # dengan menggunakan syntax methode super untuk mengembalikan class teratas tanpa pengulangan syntax
        super().showInfo()

class Hero_strength(Hero):
    def __init__(self, name):
        # Hero.__init__(self,name,200)       # contoh pemorgraman 
                                             # tanpa pengulangan
        # self.name= name
        # self.health=200
        super().__init__(name,200) # penggunaan methode super untuk mengembalikan class teratas
        super().showInfo()

lina = Hero_intelligent('lina')
axe = Hero_strength('axe')

# print(lina.name , " ", lina.health )

# print(axe.name , " ", axe.health )

"""
jadi pada syntax dengan methode super akan menggambil method teratas pada class
"""