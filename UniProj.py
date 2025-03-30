# Hello, this should be where we contribute our work as a team
# Our team are: Mariam, Malak, Karim, Salma, and, finally, me, Kahrawi.

from abc import ABC, abstractmethod
from multipledispatch import dispatch
class User(ABC):
    User_counter = 0

    def __init__(self, name: str, age: int, address: str, phone_number: str, per_email: str, uni_email: str, password: str):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number
        self.__per_email = per_email
        self.uni_email = uni_email
        self.__password = password
        User.User_counter += 1

    @abstractmethod
    def login(self, id, password):
        pass

    def logout(self):
        out = int(input("Are you sure you want to log out? Press 1 to log out:"))
        if out == 1:
            print("You're logged out.")
    @abstractmethod
    def display_info(self):
        pass
    @abstractmethod
    def view_dashboard(self):
        pass
    def get_password(self):
        return self.__password

    def reset_password(self, password):
        self.__password = password


class Employee(User):
    def __init__(self, name: str, age: int, address: str, phone_number: str, per_email: str, bus_email: str, password: str, emp_date, salary: int, work_hours: int, end_date = None):
        super().__init__(name, age, address, phone_number, per_email, bus_email, password)
        self.emp_date = emp_date
        self.end_date = end_date
        self.__salary = salary
        self.work_hours = work_hours
class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
    def display_date(self):
        print(f"{self.day}/{self.month}/{self.year}")
    def set_date(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
class Course:
    def __init__(self, course_name: str, course_code: int, reg_students: list, credit_hours: int):
        self.course_name = course_name
        self.course_code = course_code
        self.reg_students = reg_students
        self.credit_hours = credit_hours

    def display_info(self):
        print(f'Course Name: {self.course_name}, Course Code: {self.course_code}, Registered Students: {self.reg_students}, Credit Hours:{self.credit_hours}')
    def set_info(self, course_name, course_code = None):
        self.course_name = course_name
        if course_code:
            self.course_code = course_code
class Assessment(ABC):
    def __init__(self, code: str, course, date, num_of_qs: int):
        self.code = code
        self.num_of_qs = num_of_qs
        self.course = course
        self.date = date
    @abstractmethod
    def display_info(self):
        pass
    @abstractmethod
    def set_info(self, *args):
        pass

class Exam(Assessment):
    def __init__(self, code: str, course, date, duration: str, building, num_of_qs):
        super().__init__(code, course, date, num_of_qs)
        self.building = building
        self.duration = duration
    def display_info(self):
        print(f"Exam Code: {self.code}, Course code: {self.course.course_code}, Date: {self.date.display_date()}, Duration: {self.duration}")
    def set_info(self, duration, building = None ):
        self.duration = duration
        if building:
            self.building = building
class Quiz(Exam):
    def __init__(self, code: str, course, date, duration: str, building, num_of_qs):
        super().__init__(code, course, date, duration, building, num_of_qs)
    def display_info(self):
        print(f"Quiz Code: {self.code}, Course code: {self.course.course_code}, Date: {self.date.display_date()}, Duration: {self.duration}")


class Assignment(Assessment):
    def __init__(self, code, issuer, course, date, deadline, reference, num_of_qs):
        super().__init__(code, course, date, num_of_qs)
        self.issuer = issuer
        self.deadline = deadline
        self.reference = reference
    def display_info(self):
        print(f"Assignment Issuer: {self.issuer}, Course: {self.course}, date: {self.date.display_date()}, Number of question: {self.num_of_qs}")
    def set_into(self, deadline, num_of_qs = None):
        self.deadline = deadline
        if num_of_qs:
            self.num_of_qs = num_of_qs


class Student(User):
    def __init__(self, name: str, age: int, address: str, student_id: int, phone_number: str, per_email: str, uni_email: str,
                 faculty: str, enrollment_date, graduation_date, password: str, status, group: int, section: int, enrolled_courses: list, assignments: list, quizzes: list, exams: list, deadlines: list, schedule, gpa=None,
                 program=None):
        super().__init__(name, age, address, phone_number, per_email, uni_email, password)
        self.student_id = student_id
        self.faculty = faculty
        self.program = program
        self.enrollment_date = enrollment_date
        self.graduation_date = graduation_date
        self.enrolled_courses = enrolled_courses
        self.assignments = assignments
        self.quizzes = quizzes
        self.exams = exams
        self.deadlines = deadlines
        self.__gpa = gpa
        self.schedule = schedule
        self.status = status
        self.section = section
        self.group = group

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Address: {self.address}, Email: {self.uni_email}")
        print(f'Student Faculty: {self.faculty}, Their Program: {self.program}, Their Enrollment Date: {self.enrollment_date.display_date()}')
        if self.graduation_date:
            print(f"And they graduated on {self.graduation_date.display_date()}")
    def login(self, id, password):
        if self.student_id == id and self.get_password() == password:
            print(f"Successfully logged in! Welcome back student {self.name}!")
        else:
            print("Invalid Credentials")
    @dispatch(Course)
    def add(self, course):
        self.enrolled_courses.append(course)
    @dispatch(Course)
    def remov(self, course):
        self.enrolled_courses.remove(course)

    def view_dashboard(self):
        print("Course Overview: ")
        print(self.enrolled_courses)
        print(self.assignments)
        print(self.deadlines)
        print("GPA and Grades: ")

        print("Schedule: ")
        self.schedule.print_sched()

    def update_info(self, program, gpa):
        self.program = program
        self.__gpa = gpa
class Result:
    def __init__(self, student, course, assessment: str, score: int):
        self.student = student
        self.course = course
        self.assessment = assessment
        self.score = score
    def display_info(self):
        print(f"Student Name: {self.student.name}, ID, {self.student.student_id}, Course: {self.course.course_name}, Assessment: {self.assessment}, Score: {self.score}")
class Attendance:
    def __init__(self, student, lec_tut, is_absent: bool): #Instead of making attributes for lecture and tutorial, lec_tut makes it easier, because the user could add a lecture or a tutorial.

        self.student = student
        self.lec_tut = lec_tut
        self.is_absent = is_absent
    def display_info(self):
        if self.is_absent:
            print(f"Student {self.student.name}, ID: {self.student.student_id} attended lecture: {self.lec_tut.code} in {self.lec_tut.date.display_date()}")
        else:
            print(f"Student {self.student.name}, ID: {self.student.student_id} was absent in lecture: {self.lec_tut.code} in {self.lec_tut.date.display_date()}")
    def set_info(self, is_absent, lec_tut = None, student = None):
        self.is_absent = is_absent
        if lec_tut:
            self.lec_tut = lec_tut
        if student:
            self.student = student
class Lecture:
    def __init__(self, code: str, course, lecturer, time_slot: str, weekday: str, location: str, group: int):
        self.code = code
        self.course = course
        self.lecturer = lecturer
        self.time_slot = time_slot
        self.location = location
        self.weekday = weekday
        self.group = group

    def update_info(self, time_slot, location: str = None):
        self.time_slot = time_slot
        print(f"Lecture {self.code} updated. It's still held in {self.location} but at a different time slot: {self.time_slot}")
        if location:
            self.location = location
            print(f"Lecture {self.code} updated. Now, it's held in {self.location} at {self.time_slot}")

    def view_info(self):
        print(f"Lecture Code: {self.code}")
        print(f"Course: {self.course}")
        print(f"Professor: {self.lecturer}")
        print(f"Time Slot: {self.time_slot}")
        print(f"Location: {self.location}")
class Tutorial(Lecture):
    def __init___(self, code, time_slot, course, lecturer, weekday, location, group, section: int):
        super().__init__(code, course, lecturer, time_slot, weekday, location, group)
        self.section = section
    def view_info(self):
        print(f"Tutorial Code: {self.code}, Course Code: {self.course.course_code}, Teaching Assistant: {self.lecturer.name}, Location: {self.location}, Weekday: {self.weekday}, Time Slot: {self.time_slot}, Group: {self.group}, Section: {self.section}")
    def update_info(self, weekday, lecturer = None, location = None, time_slot = None):
        self.weekday = weekday
        if lecturer:
            self.lecturer = lecturer
        if location:
            self.location = location
        if time_slot:
            self.time_slot = time_slot
class TA(Employee):
    def __init__(self, name: str, ta_id, age: int, address: str, phone_number: str, per_email: str, uni_email,
                 faculty, schedule, students: list, courses_taught: list, results: list, attendances: list, tutorials: list, password, emp_date, work_hours: int, salary, end_date = None):
        super().__init__(name, age, address, phone_number, per_email, uni_email, password, emp_date, work_hours, salary, end_date)
        self.faculty = faculty
        self.ta_id = ta_id
        self.students = students
        self.results = results
        self.schedule = schedule
        self.courses_taught = courses_taught
        self.attendances = attendances
        self.tutorials = tutorials
    def login(self, ta_id, password):
        if ta_id == self.ta_id and password == self.get_password():
            print(f"You're logged in! Welcome Back {self.name}!")
    def display_info(self):
        print(f"Teaching Assistant's Name: {self.name}, Age: {self.age}, Address: {self.address}, Email: {self.uni_email}")
        print(f"Faculty: {self.faculty.name}, Employment Date: {self.emp_date.display_date()} , Working Hours: {self.work_hours}")
        if self.end_date:
            print(f"Sadly, they left und on {self.end_date.display_date()}")
    @dispatch(Date)
    def add(self, deadline):
        student_key = input("Enter student id to add deadline: ")
        for student in self.students:
            if student.student_id == student_key:
                student.deadlines.append(deadline)
            else:
                print("Student Not Found")

    @dispatch(Assignment)
    def add(self, assignment):
        student_key = input("Enter student id to add assignment: ")
        for student in self.students:
            if student.student_id == student_key:
                student.deadlines.append(assignment.deadline)
                student.assignments.append(assignment)
            else:
                print("Student Not Found")
    @dispatch(Quiz)
    def add(self, quiz):
        student_key = input("Enter student id to add assignment: ")
        for student in self.students:
            if student.student_id == student_key:
                student.quizzes.append(quiz)
            else:
                print("Student Not Found")
    @dispatch(Date)
    def remov(self, deadline):
        student_key = input("Enter student id to remove deadline: ")
        for student in self.students:
            if student.student_id == student_key:
                student.deadlines.remove(deadline)
            else:
                print("Student Not Found")

    @dispatch(Assignment)
    def remov(self, assignment):
        student_key = input("Enter student id to remove assignment: ")
        for student in self.students:
            if student.student_id == student_key:
                student.assignments.remove(assignment)
                student.deadlines.remove(assignment.deadline)
            else:
                print("Student Not Found")
    @dispatch(Quiz)
    def remov(self, quiz):
        student_key = input("Enter student id to remove quiz: ")
        for student in self.students:
            if student.student_id == student_key:
                student.quizzes.remove(quiz)
            else:
                print("Student Not Found")


    @dispatch(Result)
    def add(self, result):
        self.results.append(result)
    @dispatch(Course)
    def add(self, course):
        self.courses_taught.append(course)

    @dispatch(Attendance)
    def add(self, attend):
        self.attendances.append(attend)
    @dispatch(Tutorial)
    def add(self, tut):
        self.tutorials.append(tut)

    @dispatch(Attendance)
    def remov(self, attend):
        if attend in self.attendances:
            self.attendances.remove(attend)

    @dispatch(Result)
    def remov(self, result):
        if result in self.results:
            self.results.remove(result)

    @dispatch(Tutorial)
    def remov(self, tut):
        if tut in self.tutorials:
            self.tutorials.remove(tut)
    @dispatch(Course)
    def remov(self, course):
        if course in self.courses_taught:
            self.courses_taught.remove(course)

    def view_dashboard(self):
        print("Students: ")
        for student in self.students:
            print(f"Student name: {student.name}, ID: {student.student_id}")
            for course in student.enrolled_courses:
                if course in self.courses_taught:
                    print(f"Course: {course}")
        print("Courses Taught: ")
        for course in self.courses_taught:
            print(f"Course Name: {course.course_name}, Course Code: {course.course_code}")
        print ("Schedule: ")
        self.schedule.print_sched()
        tut_key = input("Enter lecture id to see its attendance records: ")
        for tut in self.tutorials:
            if tut_key == tut.code:
                print (f"Attendance Records of tutorial {tut.code} : ")
                print("Students who attended")
                for attend in self.attendances:
                    for tutorial in self.tutorials:
                        if attend.lec_tut.code == tutorial.code:
                            if attend.is_absent:
                                attend.display_info()
                print("Absent Students: ")
                for attend in self.attendances:
                    for tutorial in self.tutorials:
                        if attend.lec_tut.code == tutorial.code:
                            if not attend.is_absent:
                                attend.display_info()
        assign_key = input("Enter assignment id to see results:")
        for result in self.results:
            if result.assessment.code == assign_key:
                result.display_info()
        quiz_key = input("Enter quiz id to see results: ")
        for result in self.results:
            if result.assessment.code == quiz_key:
                result.display_info()



class Professor(Employee):
    def __init__(self, name: str, age: int, address: str, phone_number: str, per_email: str, uni_email,
                 faculty, students: list, TAs: list, courses_taught: list, results: list, schedule, attendances: list, lectures: list, password, prof_id, emp_date, work_hours: int, salary, end_date = None):
        super().__init__(name, age, address, phone_number, per_email, uni_email, password, emp_date, work_hours, salary, end_date)
        self.faculty = faculty
        self.students = students
        self.TAs = TAs
        self.prof_id = prof_id
        self.attendances = attendances
        self.courses_taught = courses_taught
        self.results = results
        self.lectures = lectures
        self.schedule = schedule

    def login(self, prof_id, password):
        if self.prof_id == prof_id and self.get_password() == password:
            print(f"You've successfully logged in! Welcome back, {self.name} !")
            return True
        else:
            print("Invalid Credentials")
            return False

    def display_info(self):
        print(f"Professor Name: {self.name}, Age: {self.age}, Address: {self.address}, Email: {self.uni_email}")
        print(f"Faculty: {self.faculty.name}, Employment Date: {self.emp_date.display_date()} , Working Hours: {self.work_hours}")
        if self.end_date:
            print(f"Sadly, they left und on {self.end_date.display_date()}")
    @dispatch(Student)
    def add(self, student):
        self.students.append(student)
    @dispatch(TA) #Teaching Assistant Addition
    def add(self, ta):
        self.TAs.append(ta)
    @dispatch(Course)
    def add(self, course):
        self.courses_taught.append(course)
    @dispatch(Result)
    def add(self, result):
        self.results.append(result)
    @dispatch(Attendance)
    def add(self, attend):
        self.attendances.append(attend)
    @dispatch(Lecture)
    def add(self, lecture):
        self.lectures.append(lecture)
    @dispatch(Quiz)
    def add(self, quiz):
        for student in self.students:
            student.quizzes.append(quiz)
    @dispatch(Exam)
    def add(self, exam):
        for student in self.students:
            student.exams.append(exam)
    @dispatch(Student)
    def remov(self, student):
        if student in self.students:
            self.students.remove(student)
    @dispatch(TA)
    def remov(self, ta):
        if ta in self.TAs:
            self.TAs.remove(ta)

    @dispatch(Course)
    def remov(self, course):
        if course in self.courses_taught:
            self.courses_taught.remove(course)

    @dispatch(Attendance)
    def remov(self, attend):
        if attend in self.attendances:
            self.attendances.remove(attend)

    @dispatch(Result)
    def remov(self, result):
        if result in self.results:
            self.results.remove(result)

    @dispatch(Lecture)
    def remov(self, lecture):
        if lecture in self.lectures:
            self.lectures.remove(lecture)

    @dispatch(Quiz)
    def remov(self, quiz):
        for student in self.students:
            if quiz in student.quizzes:
                student.quizzes.remove(quiz)
    @dispatch(Exam)
    def remov(self, exam):
        for student in self.students:
            if exam in student.exams:
                student.exams.remove(exam)
    def view_dashboard(self):
        print("Students: ")
        for student in self.students:
            print(f"Student name: {student.name}, ID: {student.student_id}")
            for course in student.enrolled_courses:
                if course in self.courses_taught:
                    print(f"Course: {course}")
        print("Teaching Assistants: ")
        for TA in self.TAs:
            print(f"Teaching Assistant's name: {TA.name}, University Email: {TA.uni_email}")
        print("Courses Taught: ")
        for course in self.courses_taught:
            print(f"Course Name: {course.course_name}, Course Code: {course.course_code}")
        print ("Schedule: ")
        self.schedule.print_sched()
        lec_key = input("Enter lecture id to see its attendance records: ")
        for lecture in self.lectures:
            if lec_key == lecture.lecture_name:
                print (f"Attendance Records of lecture {lecture.lecture_name} : ")
                print("Students who attended")
                for attend in self.attendances:
                    if attend.lecture.lecture_name == lecture.lecture_name:
                        if attend.is_absent:
                            attend.display_info()
                print("Absent Students: ")
                for attend in self.attendances:
                    if attend.lecture.lecture_name == lecture.lecture_name:
                        if not attend.is_absent:
                            attend.display_info()
        assign_key = input("Enter assignment id to see info:")
        for result in self.results:
            if result.assessment.code == assign_key:
                result.display_info()
        quiz_key = input("Enter quiz id to see info:")
        for result in self.results:
            if result.assessment.code == quiz_key:
                result.display_info()
        exam_key = input("Enter exam id to see info:")
        for result in self.results:
            if result.assessment.code == exam_key:
                result.display_info()

class Faculty:
    def __init__(self, name: str, professors: list, TAs: list, frst_grd_students: list, scnd_grd_students: list, trd_grd_students: list, frth_grd_students: list):
        self.name = name
        self.professors = professors
        self.TAs = TAs
        self.frst_grd_students = frst_grd_students
        self.scnd_grd_students = scnd_grd_students
        self.trd_grd_students = trd_grd_students
        self.frth_grd_students = frth_grd_students
    @dispatch(Professor)
    def add(self, prof):
        self.professors.append(prof)
    @dispatch(TA)
    def add(self, TA):
        self.TAs.append(TA)
    @dispatch(Student)
    def add(self, student):
        if student.status == "First grade":
            self.frst_grd_students.append(student)
        elif student.status == "Second grade":
            self.scnd_grd_students.append(student)
        elif student.status == "Third grade":
            self.scnd_grd_students.append(student)
        elif student.status == "Fourth grade":
            self.scnd_grd_students.append(student)
        else:
            print("Unknown Student Status. Please Check Status.")


class Department:
    def __init__(self, department_id: int, name: str, head_of_department: str, courses_offered: list,
                 faculty_members: list):
        self.department_id = department_id
        self.name = name
        self.head_of_department = head_of_department
        self.courses_offered = courses_offered
        self.faculty_members = faculty_members

    def get_department_info(self):
        print(f"Department ID: {self.department_id}")
        print(f"Name: {self.name}")
        print(f"Head of Department: {self.head_of_department}")
        print(f"Courses Offered: {self.courses_offered}")
        print(f"Faculty Members: {self.faculty_members}")

    def list_courses(self):
        print("Courses Offered:")
        for course in self.courses_offered:
            print(f"- {course}")

    def list_professors(self):
        print("Faculty Members:")
        for professor in self.faculty_members:
            print(f"- {professor}")

class Schedule:
    def __init__(self, sun_lecs: list, mon_lecs: list, tues_lecs: list, wed_lecs: list, thurs_lecs: list, big_list = None):
        self.sun_lecs = sun_lecs
        self.mon_lecs = mon_lecs
        self.tues_lecs = tues_lecs
        self.wed_lecs = wed_lecs
        self.thurs_lecs = thurs_lecs
        self.big_list = big_list
        self.big_list = [self.sun_lecs, self.mon_lecs, self.tues_lecs, self.wed_lecs, self.thurs_lecs]


    def add_lec(self, lecture):
        match lecture.weekday:
            case "Sunday": self.sun_lecs.append(lecture)
            case "Monday": self.mon_lecs.append(lecture)
            case "Tuesday": self.tues_lecs.append(lecture)
            case "Wednesday": self.wed_lecs.append(lecture)
            case "Thursday": self.thurs_lecs.append(lecture)
            case _: print("Unknown Error")
    def print_sched(self):
        for day in self.big_list:
            for lecture in day:
                print(f"{lecture.weekday}: Lecture Name:{lecture.lecture_name}, Professor: {lecture.professor.name}, Location: {lecture.location}, Time Slot: {lecture.time_slot}")







