"""
Design Pattern - <group> - Template

Reference: 
   	- Ref:  head first design patterns by Eric Freeman.
	- 
Guiding Rules:
    - There is lot common between two tasks, except few steps
    - Will have a template, task customizes few  

Common Use Case:
    - Pizza Order 
    - 

Learnings: 

"""

"""
Example: Pizza Template
   - We don't know the pizza in an order, till user selects
   - Adding or removing a pizza from menu, requires modifing Template class only
     Need not remove the reciepy

"""

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Pizzas
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Abstract class ensures, the common taskes needed for process is maintained


class TemplatePizza(object):

    def __init__(self, name, color):
        self.name  = name
        self.color = color

    def __str__(self):
        return self.name

    def prepare(self):
        print(f"Preparing all base '{self.name}' Pizza")

    def bake(self):
        print(f"Baking the '{self.name}' Pizza in '{self.color}' oven")

    def cut(self):
        print(f"Cutting the '{self.name}' Pizza")

    def box(self):
        print(f"Packing the '{self.name}' Pizza in '{self.color}' box")

    def make(self):

        print (f"### Starting '{self}' pizza ")
        self.prepare()
        self.bake()
        self.cut()
        self.box()
        print (f"### Finished '{self}' pizza \n")


class VeggiePizza(TemplatePizza):

    def __init__(self):
        super().__init__("veggie", "red")

    def prepare(self):
        TemplatePizza.prepare(self)
        print(f"  Added veggies over '{self.name}' Pizza")


class BarbicChickenPizza(TemplatePizza):

    def __init__(self):
        super().__init__("BarbicChic", "red")

    def prepare(self):
        TemplatePizza.prepare(self)
        print(f"  Added Barbic chicken over '{self.name}' Pizza")


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#  Testing Template
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def test_Template():

    VeggiePizza().make()

    BarbicChickenPizza().make()


if __name__ == "__main__":
	test_Template()



