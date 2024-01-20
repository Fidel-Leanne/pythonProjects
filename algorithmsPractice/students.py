class Student:
    def __init__(self,name, house, patronus):
        if not name:
            raise ValueError('Missing name')
        if house not in [ 'Gryffindor', 'Hufflepuff', 'Ravenclaw','Slytherin']:
            raise ValueError('invalid house')
        
        self.name = name
        self.house= house
        self.patronus= patronus


    def __str__(self):
            return f'{self.name} from {self.house}'
    
    def charm(self):
         match self.patronus:
              case 'staging' :
                   return '😀'
              case 'otter':
                   return '👍'
              case 'Jack Russell terrier' :
                   return '⭐'
              case _:
                   return '☔'
         

def main():
    student= get_student()
    print ('Expecto Patronous')
    print(student.charm())


def get_student():
   
    name=input('Name: ')
    house= input('House: ')
    patronus= input('Patronus: ')
    return Student(name , house, patronus)


if __name__ == '__main__':
    main()