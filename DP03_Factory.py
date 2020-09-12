"""
Design Pattern - <group> - Factory

Reference: 
   	- Ref:  head first design patterns by Eric Freeman.
	- 
Guiding Rules:
    - We have bunch of classes, we don't know which one has to be instantiated until runtime 
    - Design should be open for extension, but closed for modification
    - Object creatins is open for modification, but process shouldn't change

Common Use Case:
    - Pizza Order 
    - 

Learnings: 

"""

"""
Example: Pizza Factory
   - We don't know the pizza in an order, till user selects
   - Adding or removing a pizza from menu, requires modifing Factory class only
     Need not remove the reciepy

"""

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Pizzas
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Abstract class ensures, the common taskes needed for process is maintained

from abc import abstractmethod

class absPizza(object):

    @abstractmethod
    def prepare():
        pass

    @abstractmethod
    def bake():
        pass
        
    @abstractmethod
    def cut():
        pass

    @abstractmethod
    def box():
        pass


class BasePizza(absPizza):

    def __init__(self, name, color):
        self.name  = name
        self.color = color

    def __str__(self):
        return self.name

    def prepare(self):
        print(f"Preparing all base '{self.name}' Pizza")

    def bake(self):
        print(f"Backing the '{self.name}' Pizza in '{self.color}' oven")

    def cut(self):
        print(f"Cutting the '{self.name}' Pizza")

    def box(self):
        print(f"Packing the '{self.name}' Pizza in '{self.color}' box")


class CheeesePizza(BasePizza):

    def __init__(self):
        super().__init__("Cheeese", "green")

    def prepare(self):
        BasePizza.prepare()
        print(f"  Adding cheese to '{self.name}' Pizza")


class PepperoniPizza(BasePizza):

    def __init__(self):
        super().__init__("Pepperoni", "green")

    def prepare(self):
        BasePizza.prepare()
        print(f"  Sprinkle Pepper pounder on '{self.name}' Pizza")


class VeggiePizza(BasePizza):

    def __init__(self):
        super().__init__("veggie", "red")

    def prepare(self):
        BasePizza.prepare()
        print(f"  Added veggies over '{self.name}' Pizza")


class BarbicChickenPizza(BasePizza):

    def __init__(self):
        super().__init__("BarbicChic", "red")

    def prepare(self):
        BasePizza.prepare()
        print(f"  Added Barbic chicken over '{self.name}' Pizza")


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Factory
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class PizzaFactory(object):

    @staticmethod
    def make(name):
        if   name == "cheeese"     : pizza = CheeesePizza()
        elif name == "Pepperoni"   : pizza = PepperoniPizza()
        # elif name == "veggies"     : pizza = VeggiePizza()
        elif name == "BarbicChic"  : pizza = BarbicChickenPizza()
        else: pizza = None 

        if not pizza: print("Invalid")

        return pizza


class PizzaOrder(object):
    order_no = 0

    @classmethod
    def getOrderNumber(cls):
        cls.order_no += 1
        return cls.order_no

    def __init__(self):
        self.order_no = self.getOrderNumber()
        self.pizzas = []

    def add(self, pizza):
        """"""
        pizza = PizzaFactory.make(pizza)
        print(f"Added the '{pizza}' pizza to order '{self.order_no}' ")
        self.pizzas.append(pizza)

    def deliver(self):

        for pizza in self.pizzas:
            print (f"### Starting '{pizza}' pizza in '{self.order_no}' order")
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.box()
            print (f"### Finished '{pizza}' pizza in '{self.order_no}' order.\n")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#  Testing Factory
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def test_Factory():
    
    order1 = PizzaOrder()
	order1.add("cheeese")
    order1.add("Pepperoni")
    order1.deliver()

    order2 = PizzaOrder()
    order2.add("cheeese")
    order2.add("BarbicChic")
    order2.deliver()

if __name__ == "__main__":
	test_Factory()



