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
        self.__name = name
    @property
    def getName(self)-> str:
        return self.__name

class Parrot(Animal):
    def makeNoise(self) -> str:
        return "Ча-ча-ча-ча"
class Turtle(Animal):
    def makeNoise(self) -> str:
        return "Хррррррш"
class Person:
    def __init__(self,name:str,pet: Pet):
        self.__name = name
        self.__pet = pet

    def setPet(self,pet:Pet):
        self.__pet = pet
    @property
    def getPetInfo(self):
        return (
                "-" * 26 + "\n"
                           f"Питомец для {self.__name} называется {self.__pet.getName}\n"
                           "И он издаёт такой звук:\n"
                           f"{self.__pet.makeNoise()}\n"
        )





parrot = Parrot("Popugay")
turtle = Turtle("Cherepaha")
bob = Person("Bob",parrot)
tom = Person("Tom",turtle)

print(bob.getPetInfo)
print(tom.getPetInfo)