from abc import ABC,abstractmethod



class Pet(ABC):
    @abstractmethod
    def makeNoise(self) -> str:
        pass
    @abstractmethod
    def getName(self) -> str:
        pass
class Animal(Pet):
    def __init__(self, name:str):
        self._name = name
    def getName(self)-> str:
        return self._name
    def makeNoise(self) -> str:
        pass

class Parrot(Animal):
    def makeNoise(self) -> str:
        return "Ча-ча-ча-ча"
class Turtle(Animal):
    def makeNoise(self) -> str:
        return "Хррррррш"
class Person:
    def __init__(self,name:str,pet: Pet):
        self.name = name
        self.pet = pet
    def setPet(self,pet:Pet):
        self.pet = pet
    def getPetInfo(self):
        print("-" * 26)
        print(f"Питомец для {self.name} называется {self.pet.getName()}")
        print("И он издаёт такой звук:")
        print(self.pet.makeNoise())





parrot = Parrot("Popugay")
turtle = Turtle("Cherepaha")
bob = Person("Bob",parrot)
tom = Person("Tom",turtle)

bob.getPetInfo()
tom.getPetInfo()

