from ageexception.Person import Person
from ageexception.AgeException import AgeException
p = Person()
p.setAge(-1)

try:
    p.number()
except AgeException as e:
    print(e)