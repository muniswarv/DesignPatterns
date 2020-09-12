"""
Design Pattern - Creational -Singleton

Courtesy of: 
   	- https://www.youtube.com/watch?v=wElVjMlYVAw&t=1342s
	- https://github.com/aarav-tech/design-patterns-python

This can be implemented on four methods
   - Lazy SingleTon method
   - Mono State SingleTone : Object will be same
   - SingleTon Decorator
   - SingleTon metaclass

"""

def print_header(s):
	print( f"\n#{'-='*35}\n# {s} \n#{'-='*35}")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#  Lazy Singleton
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class SingleTon_Lazy(object):
	
	_inst = None
	data  = 10

	def __new__(cls, *args, **kwargs):

		# print("__new__ : Called")
		if not cls._inst:
			cls._inst = super().__new__(cls, *args, **kwargs)
			print("__new__ : Creating the object")
		else:
			print("__new__ : Using existing object")
		
		return cls._inst

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Mono State : Single Tone
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class Borg(object):
    _shared = {}

    def __init__(self):
        self.__dict__ = self._shared


class SingleTon_Borg(Borg):

    def __init__(self, data=10):
        Borg.__init__(self)
        self.data = data

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Single Tone : With decorator, It is extention to lazy 
#   - Used to create single to classes
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class SingletonDecorator(object):

    def __init__(self, klass):
        self.klass = klass
        self.instance = None
        
    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.klass(*args,**kwargs)
            print("decorator : Creating the object")
        else:
        	print("decorator : Using existing object")
        return self.instance


@SingletonDecorator
class SingleTon_Deco(object):

    def __init__(self, data=10):
        self.data = data

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Single Tone : With decorator, It is extention to lazy
#   - Used to create single to classes
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class SingletonMeta(type):
    __insts = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__insts:
            cls.__insts[cls] = super().__call__(*args, **kwargs)    	
            print("metaclass : Creating the object")
        else:
        	print("metaclass : Using existing object")

        # print(cls.__insts)
        return cls.__insts[cls]


class SingleTon_meta(metaclass=SingletonMeta):

    def __init__(self, data=10):
    	print(f"__init__ : {self} ")
    	self.data = data

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Mono State : Single Tone
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def is_same(v1, v2, msg=""):
	status = "same" if v1 == v2 else "different"
	print( msg.format(status=status) )

def test_singleton(obj1, obj2, header):

	print_header(header)
	print_header("Print Objects: Address is same/different")
	print( f"obj1 = {obj1}")
	print( f"obj2 = {obj2}")

	print_header("Print Objects: Check Object IDs ")

	is_same(obj1, obj2, msg="Create Obj1 and Obj2 are {status}")

	print( f"id(obj1) = {id(obj1)}")
	print( f"id(obj2) = {id(obj2)}")

	print_header("Print data")
	is_same(obj1.data, obj2.data, msg="After object creation : obj1.data and obj2.data are {status}")

	print ( f"obj1.data = {obj1.data}" )
	print ( f"obj2.data = {obj2.data}" )

	print_header("Print data After update")
	obj1.data = "update_obj1"

	is_same(obj1.data, obj2.data, msg="After update : obj1.data and obj2.data are {status}")

	print ( f"obj1.data = {obj1.data}" )
	print ( f"obj2.data = {obj2.data}" )


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Testing SingleTon
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# print_header("Creating : singlton_lazy class")
# lazy_obj1 = SingleTon_Lazy()
# lazy_obj2 = SingleTon_Lazy()

# test_singleton(lazy_obj1, lazy_obj2, "Testing Lazy Single Tone")


# print_header("Creating : singlton_Borg class")

# borg_obj1 = SingleTon_Borg()
# borg_obj2 = SingleTon_Borg()

# test_singleton(borg_obj1, borg_obj2, "Testing borg Single Tone")

# print_header("Creating : singlton Decoratios class")

# deco_obj1 = SingleTon_Deco()
# deco_obj2 = SingleTon_Deco()

# test_singleton(deco_obj1, deco_obj2, "Testing deco Single Tone")


print_header("Creating : singlton metaclass class")

meta_obj1 = SingleTon_meta()
meta_obj2 = SingleTon_meta()

test_singleton(meta_obj1, meta_obj2, "Testing metaclass Single Tone")