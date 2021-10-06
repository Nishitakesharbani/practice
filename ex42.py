## animal is a object (yes sort of confusing)look at thr extra credit
class animal(object):
    pass

##??

class dog(animal):
    def __init__(self,name):
        #??
        self.name=name

class cat(animal):
    def __init__(self,name):
        #??
        self.name=name
class person(object):
    def __init__(self,name):
        #??
        self.name=name
class Employee(person):
    def __init__(self,name,salary):
        super(Employee,self).__init__(name)
        #??
        self.salary=salary
##??
class fish(object):
    pass

##??
class salmon(fish):
    pass

class Halibut(fish):
    pass

##rover is a dog
rover=dog("Rover")

satan=cat("Satan")

marry=person("Mary")
marry.pet=satan
frank=Employee("Frank",120000)
frank.pet=rover
flipper=fish()
crous=salmon()
harry=Halibut()