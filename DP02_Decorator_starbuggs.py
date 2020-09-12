"""
Design Pattern - <group> - Decorator

Guiding Priciples:
    - Class should be open for extension, but closed for modification
    - Include new responsibilities to the clasself, without modifying the class
    - Not all Part of your design, should follow "Open-Closed" Principle. 
      Some most common is good enough, learnt from subject experience
      Applying "Open-Closed", principle every where is wastefull, unneccessary.

Courtesy of: 
    - Ref:  head first design patterns by Eric Freeman.
        - StarBucks example looks more like a builder pattern, than Decorator

Description:

Learnings: 

"""

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Decorator
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

"""
"""
from abc import ABC, abstractmethod

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#  Abstract Class : To facilite Decorator
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class Beverage(ABC):

    def __init__(self):
        self.description = "Unknown Bevarage"

    def getDescription(self):
        return self.description

    @abstractmethod
    def cost():
        pass

class CondimentDecorator(Beverage):

    def __init__(self):
        super().__init__()
        self.description = "Unknown Condiments"

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#  Beverages
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class Espresso(Beverage):

    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self):
        return 1.99

class HouseBlend(Beverage):

    def __init__(self):
        super().__init__()
        self.description = "House Blend"

    def cost(self):
        return 0.89

class Decaf(Beverage):

    def __init__(self):
        super().__init__()
        self.description = "Decaf"

    def cost(self):
        return 0.89


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#  Condiments: For Decorator demo, we didn't optimize code
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage
        self.description = "Mocha"

    def getDescription(self):
        return self.beverage.getDescription() + " + Mocha"

    def cost(self):
        return 0.20 + self.beverage.cost()

class Soy(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage
        self.description = "Soy"

    def getDescription(self):
        return self.beverage.getDescription() + " + Soy"

    def cost(self):
        return 0.15 + self.beverage.cost()

class Whip(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage
        self.description = "Whip"

    def getDescription(self):
        return self.beverage.getDescription() + " + Whip"

    def cost(self):
        return 0.15 + self.beverage.cost()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#  Testing  Decorator
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def print_bill(bevarages):
    for bevarage in bevarages:
        print( f"{bevarage.getDescription():40s}  ${bevarage.cost()}" )

def test_Decorator():
    """ """

    bevarages = []
    # Now, build up a pipeline of decorators:
    bevarage = HouseBlend()
    bevarage = Mocha(bevarage)
    bevarage = Soy(bevarage)
    bevarages.append(bevarage)

    bevarage = Espresso()
    bevarage = Mocha(bevarage)
    bevarages.append(bevarage)

    print_bill(bevarages)


def main():
    test_Decorator()

if __name__ == "__main__":
    main()



