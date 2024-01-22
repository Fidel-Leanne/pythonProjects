class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("No name specified")
        self.name = name


class Student(Wizard):
    def __init__(self, name,house):
        super().__init__(name)
        self.house = house
    
    def __str__(self):
        return f'{self.name}, {self.house}'

class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject

student= Student('Harry','eros')

print(student)
