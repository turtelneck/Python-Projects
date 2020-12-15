

class Game:
    variable1 = 'Hello'
    variable2 = 'world'

class Organism:
    name = "unknown"
    species = "unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}, \nSpecies: {} \nLegs: {} \nArms {} \nDNA: \nOrigin {} \nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg


class Human(Organism):
    name = 'Guy'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    def selfdesc(self):
        msg = "\nI am a guy"
        return msg


class Dog(Organism):
    name = "Dog Guy"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"
    
    def selfdesc(self):
        msg = "\nI am a dog guy. Bark."
        return msg


class Bacteria(Organism):
    name = "X"
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = "Mars"

    def selfdesc(self):
        msg = "\nI am a bacteria, not a guy. Sorry."
        return msg






if __name__ == "__main__":
    x = Game()
    print("{} {}".format(x.variable1, x.variable2))

    human = Human()
    print(human.information())
    print(human.selfdesc())

    dog = Dog()
    print(dog.information())
    print(dog.selfdesc())

    bacteria = Bacteria()
    print(bacteria.information())
    print(bacteria.selfdesc())
