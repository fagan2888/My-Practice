

###############################################
########## Inheritance & Polymorphism #########
###############################################


class Dog:
    
    # Class Attribute
    species='mammal'
    
    # Initializer / Instance Attributes / Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # instance method
    def description(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    # instance method
    def sound(self, sound):
        return '{} says {}'.format(self.name, sound)
    
    def __add__(self,other):
        return Dog(self.name, self.age+other.age)


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return '{} runs {}'.format(self.name, speed)

# Child classes inherit attributes and behaviors from the parent class
jim = RussellTerrier("Jim", 12)
print(jim.description())

# Child classes have specific attributes and behaviors as well
print(jim.run("slowly"))

# Is jim an instance of Dog()?
print(isinstance(jim, Dog))

# Is julie an instance of Dog()?
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

# Is julie and instance of jim?
print(isinstance(julie, jim))

# Child class could override attributes and behavior of parent class
class SomeOtherBreed(Dog):
    species = 'reptile'

beans = SomeOtherBreed('unknown',0)
print(beans.species)


a = Dog('A',1)
b = Dog('B',2)
c = Dog('C',3)
print(a.description())
print(b.sound('wang wang'))

def get_biggest_age(*args):
    return max(args)
print("The oldest dog is {} years old.".format(get_biggest_age(a.age, b.age, c.age)))




class BasePosition:
    def __init__(self, shrs, long):
        self.shares = shrs
        self.isLong = long
        print ("calling BasePosition class constructor")

    def __del__(self):
        print("calling BasePosition class destructor")

    def printPos(self):
        print("calling printPos from Base")
        print(self.shares)
        print(self.isLong)

class ChildPosition(BasePosition):
    def __init__(self, shrs, long, childShrs):
            self.childShares = childShrs
            BasePosition.__init__(self, shrs, long)
            print("calling ChildPosition class constructor")

    def __del__( self ):
        print("calling ChildPosition class destructor ")

    def printPos (self):
        print("calling printPos from Child")
        print(self.shares)
        print(self.isLong)
        print (self.childShares)

basePos1 = BasePosition (100, 1)
basePos2 = BasePosition (75, 0)

childPos1 = ChildPosition (25, 0, 5)
childPos2 = ChildPosition (150, 1, 0)

basePos3 = basePos1 + basePos2

