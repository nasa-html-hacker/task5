class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

class Person2:
    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}"

class Student(Person, Person2):
    def __init__(self, name: str, surname: str, age: int, university: str):
        super().__init__(name, surname, age)
        self.university = university
    def __str__(self):
        return f"{super().__str__()}, University: {self.university}"    

stu = Student("Nick", "Kuloshvili", 19, "Tbilisi State Medical University")

print(stu) 
