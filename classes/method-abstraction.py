from abc import ABC, abstractmethod

class Tattoo(ABC):
    def chest(self, thing):
        print("You have a giant",thing,"tattooed on your chest. Classy.")

    @abstractmethod
    def leftBicep(self, thing):
        pass

class AnotherTattoo(Tattoo):
    def leftBicep(self, thing):
        print("And you have a",thing,"tattooed on your left bicep. Also classy.")

obj = AnotherTattoo()
obj.chest("Python shell full of terrible code")
obj.leftBicep("error message for a problem you don't know how to solve")
