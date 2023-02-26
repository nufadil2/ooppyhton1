"""multiple inheritance dapat mengambil beberapa 
super class didalam beberapa methode"""

# contoh

class A:

    def method_A(self):
        print("ini adalah method A")

class B:
    
    def method_B(self):
        print("ini adalah method B")


class C (A,B):
    pass

objeck = C()

objeck.method_A()
objeck.method_B()

# penjelasan pada class Sesuatu dapat mendapatkan banyak inheritance dari banyak class atau super class 

# kegunaannya bisa menggambil beberapa kelas pada method yang dipilih

class Team:
    def setTeam(self,team):
        self.team = team
    
    def showTeam(self):
        print(self.team)

class Tipe_Hero:
    def setTipe(self,tipe):
        self.tipe = tipe

    def showTipe(self):
        print(self.tipe)


class Hero(Team,Tipe_Hero): # multiple inheritance
    def __init__(self,name,health):
        self.name = name
        self.health = health

Ucup = Hero('Ucup',100)

Ucup.setTeam("merah")
Ucup.setTipe("cundang")

Ucup.showTeam()
Ucup.showTipe()