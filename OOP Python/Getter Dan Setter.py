class Hero:
    def __init__(self, name, health, armor) -> None:
        self.__name=name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\thealth: {}".format(self.__name,self.__health)

    """
    di pyhton terdapat dekorator yang disebut property
    pada sebelumnya terdapat dekorator yang saticmethod dan classmethod
    pada tahap ini ada yang disebut property dengan menggunakan @property <<merubah sebuah methode menjadi variable

    """

    @property
    def info(self):
        return "name {} : \n\thealth: {}".format(self.__name,self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self,input):
        self.__armor = input

    @armor.deleter #<< mengubah nilai menjadi kosong
    def armor(self):
        print('armor di deleted')
        self.__armor = None

sniper = Hero('sniper',100,10)

print('merubah info')
print(sniper.info)
sniper.name = 'dadang'

print(sniper.info)

print('getter dan setter untuk __armor:')
print(sniper.armor)
print(sniper.__dict__)
sniper.armor = 50
print(sniper.armor)
print(sniper.__dict__)

print('delet armor')

del sniper.armor

print(sniper.__dict__)