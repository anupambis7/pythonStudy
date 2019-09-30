print("################ Class  #######################")

class Dog(object):
    # Class object Attribute
    category = "Anumal"
    def __init__(self,breed,name="Buno"):
        self.breed_type = breed
        self.dog_Name = name

stray = Dog(breed ="Stray_Type")        # instantiating with the parameter name
stray2 = Dog("Stray_Type")              # instantiating without the parameter name
dobernan = Dog(breed="dobernan_Type",name= "gublu")

print(stray.breed_type)
print(stray2.breed_type)
print(dobernan.breed_type)

## Printing class objects
print(dobernan.category)
print(stray2.category)

## printing the optional parameter
print(dobernan.dog_Name)            # This gets the name that is passed
print(stray2.dog_Name)              # This gets the dafault name as no parameters passed

## printing the type of the objects
print(type(stray))
print(type(dobernan))

# Note :    Here category is a class object attribute , So we can see that it remans the same for all the Dog objects.

print("################ Methods  #######################")
## Methods are functions defined inside the body of a calss
class Circle(object):
    pi = 3.14

    # Circle get instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius

    # Area method calculates the area. Note the use of self.
    def area(self):
        return self.radius * self.radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, radius):
        self.radius = radius


    # Method for getting radius (Same as just calling .radius)
    def getRadius(self):
        return self.radius
    def areaOfOtherCircle (self,radius):
        radious2= radius
        return radious2 * radious2 * Circle.pi


circle1 = Circle(2)
print("Area of Circle is " + str(circle1.area()))
print("Radius of Circle is " + str(circle1.getRadius()))
print("Area of Other Circle is " + str(circle1.areaOfOtherCircle(4)))       # Passig parameter value to Method
print("Radius of Circle is " + str(circle1.getRadius()))
circle1.setRadius(1)
print("Area of Circle is " + str(circle1.area()))
print("Radius of Circle is " + str(circle1.getRadius()))

print("################ Inheritance  #######################")
class Animal(object):
    def __init__(self):
        print ("Animal created")

    def whoAmI(self):
        print ("Animal")

    def eat(self):
        print ("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print ("Dog created")

    def whoAmI(self):
        print ("Dog")

    def bark(self):
        print ("Woof!")

d = Dog()
d.whoAmI()
d.eat()

print("################ Special methods  #######################")
class Book(object):
    def __init__(self, title, author, pages):
        print ("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title:%s , author:%s, pages:%s " %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print ("A book is destroyed")

book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print(book)
print (len(book))
del book