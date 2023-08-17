# Static and classes methods in python

class person(object):
    def __init__(self, name , age):
        self.name=name
        self.age= age

    @classmethod
    def getPopulation(cls):
        return cls.getPopulation

    @staticmethod
    def isAdult(age):
        return age>=18
    
    def dispaly(self):
        print("Name: ", self.name, self.age , 'years old')

newPerson = person('tim', 10)



print(newPerson.isAdult(10))