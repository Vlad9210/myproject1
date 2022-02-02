class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal): #dziedziczymy od klasy animal
    def voice(self):
        print("How How")

class Wolf(Dog): #dziedziczymy po Dog
    def getVoice(self):
        print("Jestem wilkiem, ")
        super().voice() #wyszukuje i wywołuje podana def (voice)

class Cat(Animal):
    def getVoice(self):
        print("Meow Meow")


dog = Dog("Reksio", 10)
print(dog.name)
print(dog.age)
dog.voice()

cat = Cat("Bury", 8)
cat.getVoice()

wolf = Wolf("Gerald", 55)
wolf.getVoice()
print(wolf.name)