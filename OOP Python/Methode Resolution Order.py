# method resolution order // multiple inheritance

class A:
    
    def show(self):
        print("ini adalah show A")

class B:

    def show(self):
        print("ini adalah show B")

class C(B,A): # pengubahan posisi pada urutan exekusi class method
    pass

    # def show(self):
    #     print("ini adalah show C")

objek = C()
objek.show()

# help(objek) # untuk melihat urutan method resolution order