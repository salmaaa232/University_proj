#Hello, this should be where we contribute our work as a team
#Our team are: Mariam, Malak, Karim, Salma, and, finally, me, Kahrawi.
class User:
    User_counter = 0

    def __init__(self, name: str, age: int, address: str, id: int, phone_number: str, per_email: str, bus_email:str, begin_date: str, password: str, end_date = None):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__id = id
        self.__phone_number = phone_number
        self.__per_email = per_email
        self.__bus_email = bus_email
        self.__begin_date = begin_date
        self.__end_date = end_date
        self.__password = password
        User.User_counter += 1

    def login(self, id, password):
        if self.id == id and self.password == password:
            print(f'Welcome {self.name} back!')
        else:
            print("Invalid Credentials. Try again.")
    def logout(self):
        out = int(input("Are you sure you want to log out? Press 1 to log out:"))
        if out == 1:
            print("You're logged out.")


    def display_userinfo(self):
        print(f'(General Info)User Name: {self.__name}, User Age: {self.__age}, User ID: {self.__id}, User Phone Number: {self.__phone_number}, User Personal Email: {self.__per_email}, User Business Email: {self.__bus_email}. Number of users: {User.User_counter}')
        print(f'They started with us in {self.__begin_date}')
        if self.__end_date:
            print(f'Unfortunately, they left us in {self.__end_date}')

class Student(User):
    def __init__(self, name: str, age: int, address: str, id: int, phone_number: str, per_email: str, bus_email:str, faculty: str, enrollment_date: str, begin_date: str, password: str, end_date = None , gpa = None, program = None):
        super().__init__(name, age, address, id, phone_number, per_email, bus_email, begin_date, end_date, password)
        self.__faculty = faculty
        self.__program = program
        self.__enrollment_date = enrollment_date
        self.__gpa = gpa
    def display_studentinfo(self):
        self.display_userinfo()
        print(f'Student Faculty: {self.__faculty}, Their Program: {self.__program}, Their Enrollment Date: {self.__enrollment_date}')

class Professor(User):
    students = []
    def __init__(self, name: str, age: int, address: str, id: int, phone_number: str, per_email: str, bus_email:str, faculty: str, begin_date: str, password: str, end_date = None):
        super().__init__(name, age, address, id, phone_number, per_email, bus_email, begin_date, end_date, password)
        self.__faculty = faculty
        self.__enrollment_date = enrollment_date

class Course:
    def __init__ (self, course_name: str, course_code: int, reg_students: list):
        self.course_name = course_name
        self.course_code = course_code
        self.reg_students = reg_students
    def display_courseinfo(self):
        print(f'Course Name: {self.course_name}, Course Code: {self.course_code}, Registered Students: {self.reg_students}')

class Administrator(User):
    def __init__(self, name: str, age: int, address: str, id: int, phone_number: str, per_email: str, bus_email:str,)





