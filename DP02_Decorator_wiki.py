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

def print_header(s):
    print( f"\n#{'-='*35}\n# {s} \n#{'-='*35}")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Decorator
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

"""
Demonstrated decorators in a world of a 10x10 grid of values 0-255. 
"""

import random
from abc import ABC, abstractmethod

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Support
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def s32_to_u16(x):
    if x < 0:
        sign = 0xf000
    else:
        sign = 0
    bottom = x & 0x00007fff
    return bottom | sign

def seed_from_xy(x, y):
    return s32_to_u16(x) | (s32_to_u16(y) << 16)

class DataSquare:
    def __init__(self, initial_value=None):
        self.data = [initial_value] * 10 * 10

    def get(self, x, y):
        return self.data[(y * 10) + x]  # yes: these are all 10x10

    def set(self, x, y, u):
        self.data[(y * 10) + x] = u

class baseClass(ABC):
    """ """
    def __init__(self):
        pass

    @abstractmethod
    def get(self, x, y):
        return 0

    def draw(self):
        for y in range(10):
            for x in range(10):
                print(f"{self.get(x, y):5d}", end="")
            print()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Support
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# class RandomSquare(baseClass):
#     """Gets the Random number based on X,Y """
#     def __init__(self, seed_modifier):
#         super().__init__()
#         self.seed_modifier = seed_modifier

#     def get(self, x, y):
#         seed = seed_from_xy(x, y) ^ self.seed_modifier
#         random.seed(seed)
#         return random.randint(0, 255)

class RandomSquare(baseClass):
    """Gets the Random number based on X,Y """
    def __init__(self, seed_modifier):
        super().__init__()
        
    def get(self, x, y):
        return random.randint(0, 255)

class CacheDecorator(baseClass):
    """Get the values from Cache, if not initalized set it"""
    def __init__(self, decorated):
        super().__init__()
        self.decorated = decorated
        self.cache = DataSquare()

    def get(self, x, y):
        if self.cache.get(x, y) == None:
            self.cache.set(x, y, self.decorated.get(x, y))
        return self.cache.get(x, y)

class MaxDecorator(baseClass):
    """Ensure all numbers are below a given value"""
    def __init__(self, decorated, max):
        super().__init__()
        self.decorated = decorated
        self.max = max

    def get(self, x, y):

        if self.decorated.get(x, y) > self.max:
            return self.max
        return self.decorated.get(x, y)

class MinDecorator(baseClass):
    """Ensure all numbers are above a given value"""

    def __init__(self, decorated, min):
        super().__init__()
        self.decorated = decorated
        self.min = min

    def get(self, x, y):
        if self.decorated.get(x, y) < self.min:
            return self.min
        return self.decorated.get(x, y)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#  Testing  Decorator
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def test_Decorator():
    """ """

    # Now, build up a pipeline of decorators:

    obj = obj_sqr   = RandomSquare(635)
    obj = obj_cache = CacheDecorator(obj)    ; # Ensure Square is same 
    obj = obj_max   = MaxDecorator(obj, 200) ; # Clip the Max value
    obj = obj_min   = MinDecorator(obj, 100) ; # Clip the Min value
    obj.draw()

def main():
    test_Decorator()




if __name__ == "__main__":
    main()



