# student class, has a name and id
class Student:

    # the constructor method
    def __init__(self, name: str, id: int) -> None:
        self.name: str = ____
        self.id: int = __

    # the __repr__ method is another special method, used to get a string representation of the object so we can print meaningful data
    # otherwise, printing will output memory address like this
    # <__main__.Student object at 0x7aff4af93d30>
    def __repr__(self) -> str:
        return f"Student({self.name}, {self.id})"

# department class, has a name and a list of students
class Department:
    def _________(self, name: str):
        self.name: str = ____
        self.students: list[Student] = []

    def add(self, student: Student):
        self._______.append(_____)

    def remove(self, student: Student):
        self._______.remove(_______)

    def num_students(self):
        return len(_________)

# Make a new department and add students
csdept : Department = Department("Computer Science")
csdept.add(s1 := Student("Adam", 1))
csdept.add(s2 := Student("John", 2))
csdept.add(s3 := Student("Mia", 3))
csdept.add(s4 := Student("Charlie", 4))

print(csdept.num_students())

del csdept # remove the csdept department object

# this should cause an exception as csdept no longer exists
try: 
    print(csdept.num_students())
except Exception as err:
    print(err)

# this should work since the objects are related by aggregation
print(s1, s2, s3, s4)
