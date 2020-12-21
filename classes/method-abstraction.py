from abc import ABC, abstractmethod

class Tattoo(ABC):
    def chest(self, thing):
        print("You have a giant",thing,"tattooed on your chest. Classy.")
    # A method in the parent that can be defined
    # in different ways by subsequent child classes
    @abstractmethod
    def leftBicep(self, thing):
        pass

class AnotherTattoo(Tattoo):
    # an example of a way to redefine the abstracted method
    def leftBicep(self, thing):
        print("And you have a",thing,"tattooed on your left bicep. Also classy.")

obj = AnotherTattoo()
obj.chest("Python shell full of terrible code")
obj.leftBicep("error message for a problem you don't know how to solve")
