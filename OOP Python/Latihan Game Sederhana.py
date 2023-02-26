class Hero:

    def __init__(self, name, health, attackPower, armorNumber) -> None:
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber
    
    def serang(self, lawan):
        print(self.name + ' Menyerang ' + lawan.name)
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackPower_lawan):
        print(self.name + " diserang " + lawan.name)
        attack_diterima = attackPower_lawan/self.armorNumber
        print('serangan terasa : ' + str(attack_diterima))
        self.health -= attack_diterima
        print('darah ' + self.name + ' Tersisa ' + str(self.health))

sniper = Hero('sniper', 100,10,2)
rikimaru = Hero('Rikimaru',100,5,10)

sniper.serang(rikimaru)
rikimaru.serang(sniper)