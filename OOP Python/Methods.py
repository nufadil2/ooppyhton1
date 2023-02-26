"""


"""

class Hero:
    # class Variable
    Jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor) -> None:
        #instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.Jumlah_hero += 1

        # methode dibagi menjadi tiga

        # 1. methode dengan argumen
        # 2. methode tanpa argumen
        # 3. methode dengan return


    # void funcion, methode tanpa return, tanpa arumen
    def siapa(self):
        print("namaku adalah " + self.name)

    # methode dengan argumen, tanpa retrun
    def healthUp(self,up):
        self.health += up
    
    # methode dengan return
    def getHealth(self):
        return self.health

hero1 = Hero('sniper', 100, 10, 5)
hero2 = Hero('mario bross', 90, 5, 10)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())
