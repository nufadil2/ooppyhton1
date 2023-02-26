"""
pewarisan adalah sesuatu yang di turunkan yang berlaku masing class
dengan penyebutan super class dan subclass

"""

class Hero: # super class

    def __init__(self,name,health) -> None:
        self.name = name
        self.health = health
        
# sub class
class Hero_intelligent(Hero):
    pass

class Hero_strength(Hero):
    pass


lina = Hero('lina', 100)
techies = Hero_intelligent('techies',50)
axe = Hero_strength('axe',200)

print(lina.name)
print(techies.name)
# print(help(techies))
print(axe.name)
# print(help(axe))