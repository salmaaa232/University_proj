# Hello, this should be where we contribute our work as a team
# Our team are: Mariam, Malak, Karim, Salma, and, finally, me, Kahrawi.

from abc import ABC, abstractmethod
from multipledispatch import dispatch
from datetime import date

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

    def create_book(self, title: str, author: str, num_pages: int):
            return Book(title, author, num_pages, self.name)


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


class examresult: #Salma
    student_records = {} #(semester (semester_gpa,total_credits))
    def __init__(self, semester, id):
        self.semester = semester
        self.id = id
        self.accum = {} #dah dict feeh {course_code: grade_point}
        self.result = {}  #w dah tuple feeh {course_code[grade, credit hour]}
        self.registered_ch = 0
        self.grade_points = { 'A+': 4.0, 'A': 3.7, 'B+': 3.3, 'B': 3.0,'C+': 2.7, 'C': 2.3, 'D+': 2.0, 'D': 1.7, 'F': 1.0 }
        if id not in examresult.student_records:
            examresult.student_records[id] = {}  #law el student awel gpa leeh fa yet3amalo dictionary gedeeda

    def addresult(self,  course_code , credit_hour, grade):
        if self.registered_ch + credit_hour > 18:
            print("Maximum credit hours reached.")
            return
        self.result[course_code] = (grade, credit_hour)  #to display el grades w  chs to calc. el gpa
        self.accum[course_code] = self.grade_points[grade]  #to calc el gpa bardo
        self.registered_ch += credit_hour #credit hours accumilated
        print(f"student {self.id}'s grade for {course_code} has been recorded")


class transcript(examresult): #Salma
    def __init__(self, semester, id):
        super().__init__(semester, id)  
       
    def calc_gpa(self):
        try:
            total_points = 0
            total_credits = 0
            for course_code, (grade, credit_hour) in self.result.items():  #iterating feeh 3shan ye7seb kol el courses
                if course_code in self.accum:  
                    total_points += self.accum[course_code] * credit_hour
                    total_credits += credit_hour    
            gpa = total_points / total_credits  
            examresult.student_records[self.id][self.semester] = (gpa, total_credits) #storing gpa per semester
            return gpa 
        except ZeroDivisionError:
            raise ZeroDivisionError('Error: Student has not completed any courses this semester.')
    
    def calc_cgpa(self):
        try:
            numerator = 0
            denominator = 0
            for semester, (semester_gpa, semester_credits) in examresult.student_records[self.id].items(): #nafs el fekra
                numerator += semester_gpa * semester_credits
                denominator += semester_credits
            cgpa = numerator / denominator
            return cgpa
        except ZeroDivisionError:
            raise ZeroDivisionError('Error: No completed semesters to date.')

    def display_transcript(self):
        print(f"Transcript for Student ID: {self.id} in semester : {self.semester}")
        for course_code, (grade, credit_hour) in self.result.items():
            print(f"{course_code}| Grade: {grade}, Credit Hours: {credit_hour}, Point: {self.accum[course_code]:.2f}")
        gpa = self.calc_gpa()  
        cgpa = self.calc_cgpa()  
        print(f"GPA: {gpa:.2f}")
        print(f"CGPA: {cgpa:.2f}")


class financialaid:  #Salma, Malak, Mariam
    def __init__(self):
        self.scholarships = {  
            "Top 100" : 100,
            "STEM" : 50,
            "World Championships": 100,
            "Arab/African Championships":80,
            "Local Championships": 50,
            "Employee children": 75,
            "Army children": 100,
        }
        self.student_scholarships = {} #(student id : discount percentage)

    def assign_student(self, id, scholarship_name):
            self.student_scholarships[id] = self.scholarships[scholarship_name]
            print(f"student {id} awarded '{scholarship_name}' scholarship with tuition discount {self.scholarships[scholarship_name]}%")
       
    def get_discount(self, id):
        return self.student_scholarships.get(id, 0) #default b zero law mafeesh discount
    
    def academicexcellence(self, id, semester):
        gettingcgpa = transcript(semester ,id)
        cgpa = gettingcgpa.calc_cgpa()
        if self.get_discount(id) == 0 and cgpa >= 3.85:
            self.student_scholarships[id] = 40
            print(f"Academic excellence discount 40% applied for student {id}.")
        elif self.get_discount(id)  == 0 and cgpa >= 3.7:
            self.student_scholarships[id] = 20
            print(f"Academic excellence discount 20% applied for student {id}.")
        else:
            print(f"Student {id} unfortently didn't meet the elgibility criteria for the 'Academic Excellence' scholarship.")
        
    def withdraw_scholarship(self, id, semester):
        gettingcgpa = transcript(semester ,id)
        cgpa = gettingcgpa.calc_cgpa()
        if cgpa < 2:
            self.student_scholarships[id] = 0
            print(f"Student {id} scholarship revoked due to acedemic negligence.")
        else:
            print(f"Student {id}'s scholarship has not been revoked, as they have not yet reached the minimum GPA requirement.")


financialaid = financialaid()


class payment:  #Salma

    def __init__(self, id, faculty):
        self.id = id
        self.faculty = faculty 
        faculty_fees = { "FOE": 90000, "BAS": 40000, "FIBH": 65000, "AnD": 50000, "CSIT": 70000, "PharmD": 95000, "SARCH": 85000 }
        self.duedate = [date(2025, 1, 25),  date(2025, 2, 25),  date(2025, 3, 25),   date(2025, 4, 25) ]  # Due date per installment
        self.total_fee = faculty_fees.get(self.faculty, 0)
        self.scholarship_discount = financialaid.get_discount(self.id)
        self.total_fee -= self.total_fee * self.scholarship_discount / 100
        self.amount_paid = 0
        self.quarter_payment = self.total_fee / 4
        self.quarters_paid = 0
        if self.scholarship_discount == 100:
            self.quarters_paid = 4
    
    def display_fees(self):
        if self.scholarship_discount == 100 :
            print(f"Student  admitted under a full-tuition scholarship, no further payment required.")
        else:
            print(f"Overall fee: {self.total_fee} pounds | Payment plan [4 Installments]: {self.quarter_payment} pounds")
    
    def make_payment(self, amount):
        if self.quarters_paid == 4:
            print("All installments paid.")
        else:
            duedate = self.duedate[self.quarters_paid]
            duedate = date(duedate.year, duedate.month, duedate.day) #7awelna el dates le acual dates
            if date.today() > duedate:
                print(f"This payment is past the due date, a late penalty fee of 1000 pounds has been applied. Revised total: {self.quarter_payment + 1000} pounds ")
                finalamount = self.quarter_payment + 1000
            else:
                finalamount = self.quarter_payment
                
            if amount != finalamount and self.quarters_paid != 4:
                print(f"invalid ammount, please pay {finalamount} pounds.")
            else:
                self.quarters_paid += 1
                self.amount_paid += amount
                print(f"installment {self.quarters_paid} has been paid by {self.id} for {self.faculty}. {4- self.quarters_paid} installments left.")
                    
    def check_payment(self):
        if self.quarters_paid < 4:
            if self.quarters_paid == 1:
                print("1st installment paid, 3 installments left.")
            else:
                print(f"{self.quarters_paid} installments paid, {4- self.quarters_paid} installments left.")
        else:
            print("All installments paid.")

class Feedback: #Mariam, Salma
    
    courses_feedback = {}
 
    def submit_feedback(self, id, Course: Course , rating = int , comment = str ):
        if id in Course.reg_students:
            if Course.course_name not in Feedback.courses_feedback:
                Feedback.courses_feedback[Course.course_name] = [] #tuple coursename[rating, comment]
            Feedback.courses_feedback[Course.course_name].append([rating, comment])
        else:
            print(f"You are not registered in course {Course.course_name}.")

    def avg_rating(self, Course: Course ):
        if Course.course_name not in Feedback.courses_feedback:
            return 0
        else:
            total = 0.0
            count = 0.0
            for num in Feedback.courses_feedback[Course.course_name]:
                total += float(num[0]) #index 0 howa eli feeh el rating
                count += 1.0
            return round(total/count, 2)
        
    def bestcomment(self, Course: Course):
        if Course.course_name not in Feedback.courses_feedback:
            return ""
        else:
            best_rate = -1 #negative one 3shan mafeesh a2al meno fel rating , 3shan momken yekoon a7san rating lel course zero 
            best_comment = ""
            for num in Feedback.courses_feedback[Course.course_name]:
                if num[0] >= best_rate:
                    best_rate = num[0]
                    best_comment = num[1] #index 1 comment
        return best_comment
    
    def worstcomment(self, Course: Course):
        if Course.course_name not in Feedback.courses_feedback:
            return ""
        else:
            worst_rate = 6  #nafs fekret el -1 bas ma2loob
            worst_comment = ""
            for num in Feedback.courses_feedback[Course.course_name]:
                if num[0] <= worst_rate:
                    worst_rate= num[0]
                    worst_comment = num[1]
        return worst_comment
    
    def display_feedback(self, Course: Course):
        if Course.course_name not in Feedback.courses_feedback:
            print("Course has no feedback yet.")
        else:
            print(f"|Course Name: {Course.course_name} || Average Rating: {self.avg_rating(Course)} / 5.")
            print(f"|Top Comment: {self.bestcomment(Course)}")
            print(f"|Bottom Comment: {self.worstcomment(Course)}")

class courseregestration(Feedback): #Salma
    def __init__(self, id, semester):
        super().__init__()
        self.id = id
        self.semester = semester
        self.registered_courses = []
        self.chs = 0

    def register(self, Course):
        if self.chs + Course.credit_hours <= 18:
            super().display_feedback(Course)

            while True:
                approve = input("Do you want to register in this course? (y/n): ")
                
                if approve == "y":
                    print(f"Student {self.id} registered in course: {Course.course_name}")
                    Course.reg_students.append(self.id)
                    self.registered_courses.append(Course.course_name)
                    self.chs += Course.credit_hours
                    break  
                elif approve == "n":
                    print("Registration canceled.")
                    break  
                else:
                    print("Invalid choice. Please enter 'y' for yes or 'n' for no.")
        else:
            print("Credit limit reached, remove courses or request approval to proceed.")
    
    def withdraw(self, Course):
        if self.id in Course.reg_students:
            Course.reg_students.remove(self.id)    #removing el student mn el reg_list
            print(f"student {self.id} withdrawn from course {Course.course_name}")
        else:
            print(f"Student {self.id} not registered in {Course.course_name}")

    def display_registeredcourses(self):
        print("Registered courses: ")
        for num in self.registered_courses:
            print(self.registered_courses(Course.course_name))

class attendance(Course):  #Salma

    def __init__(self, Course: Course):
        self.Course = Course
        self.abs_amount = {} 
    def FW(self, id):  #forced withdrawl method

        if id in self.Course.reg_students:
            self.Course.reg_students.remove(id)  
            print(f"student {id} withdrawn from course {self.Course.course_name}, due to excessive absence.")
        else:
            print(f"Student {id} not registered in {self.Course.course_name}")

    def absent(self, id):  
        if id in self.Course.reg_students:
            self.abs_amount[id] = self.abs_amount.get(id, 0) + 1  
            if self.abs_amount[id] > 4:     #limit el absence le 4 times bas
                self.FW(id)
            else:
                print(f"Student {id}'s absence nunmber {self.abs_amount[id]} recorded")
        else:
            print(f"Student {id} not registered in {self.Course.course_name}")
            
    def display_absence(self, id):
        if id in self.Course.reg_students:
            print(f"{id} has an abscence record of {self.abs_amount.get(id, 0)}")
        else:
            print(f"Student {id} not registered in {self.Course.course_name}")


class Publication: #Mariam
    def __init__(self, publication_id: int, title: str, authors: list, journal: str, date: str, abstract: str):
        self.publication_id = publication_id
        self.title = title
        self.authors = authors
        self.journal = journal
        self.date = date
        self.abstract = abstract
    def add_publication(self) -> None:
        print(f"Publication '{self.title}' added with ID {self.publication_id}.")
    def view_publication_details(self) -> None:
        print(f"Publication details {self.publication_id}: Title '{self.title}', Authors {self.authors}, Journal {self.journal}, Date {self.date}.")
  
class building : #Mariam
    def __init__ (self , building_id : int ,name : str ,address: str, number_of_floors: int, classrooms: list = None):
        self.building_id = building_id
        self.name = name
        self.address = address
        self.number_of_floors = number_of_floors
        self.classrooms = classrooms
    def add_classroom(self, classroom: str) -> None:
        self.classrooms.append(classroom)
        print(f"Classroom {classroom} added to building {self.building_id}.")
    def view_building_details(self) -> None:
        print(f"Building details {self.building_id}: Name '{self.name}', Address '{self.address}', Floors {self.number_of_floors}, Classrooms {self.classrooms}.")

class MedicalRecord: #Mariam
    def __init__(self, record_id: int, student_id: int, date: str, diagnosis: str, treatment: str, doctor_name: str):
        self.record_id = record_id
        self.student_id = student_id
        self.date = date
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.doctor_name = doctor_name
    def add_record(self) -> None:
        print(f"Medical record {self.record_id} added for student {self.student_id}.")
    def view_record(self) -> None:
        print(f"Medical record {self.record_id}: Date {self.date}, Diagnosis '{self.diagnosis}', Treatment '{self.treatment}', Doctor '{self.doctor_name}'.")
    def update_record(self) -> None:
        print(f"Medical record {self.record_id} updated.")

class Parking: #Mariam
    def __init__(self, parking_id: int, location: str, capacity: int, availability: int, user_id: int = None):
        self.parking_id = parking_id
        self.availability = availability
        self.user_id = user_id
    def allocate_parking_spot(self) -> bool:
        if self.availability > 0:
            self.availability -= 1
            print(f"Parking spot allocated at {self.location}.")
            return True
        else:
            print(f"No parking spots available at {self.location}.")
            return False
    def check_availability(self) -> int:
        return self.availability
    def view_parking_details(self) -> None:
        print(f"Parking details {self.parking_id}: Location {self.location}, Capacity {self.capacity}, Availability {self.availability}.")

class Inventory: #Mariam
    def __init__(self, item_id: int, name: str, quantity: int, location: str, description: str):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.location = location
        self.description = description
    def add_item(self) -> None:
        self.quantity += 1
        print(f"Item {self.name} added to inventory.")
    def remove_item(self) -> None:
        if self.quantity > 0:
            self.quantity -= 1
            print(f"Item {self.name} removed from inventory.")
        else:
            print(f"Cannot remove item {self.name}. Quantity is zero.")
    def check_inventory(self) -> int:
        return self.quantity

class Club: #Mariam
    def __init__(self, club_id: int, name: str, president_id: int, members: list = None, activities: list = None):
        self.club_id = club_id
        self.name = name
        self.president_id = president_id
        self.members = members or []
        self.activities = activities or []
    def add_member(self, member: str) -> None:
        self.members.append(member)
        print(f"Member {member} added to club {self.name}.")
    def schedule_activity(self, activity: str) -> None:
        self.activities.append(activity)
        print(f"Activity '{activity}' scheduled for club {self.name}.")
    def view_club_details(self) -> None:
        print(f"Club details {self.club_id}: Name '{self.name}', President ID {self.president_id}, Members {self.members}, Activities {self.activities}.")

class Department: #Mariam
    def __init__(self, department_id: int, name: str, head_of_department: str, courses_offered: list, faculty_members: list):
        self.department_id = department_id
        self.name = name
        self.head_of_department = head_of_department
        self.courses_offered = courses_offered
        self.faculty_members = faculty_members
    def get_department_info(self) -> None:
        print(f"Department ID: {self.department_id}")
        print(f"Name: {self.name}")
        print(f"Head of Department: {self.head_of_department}")
        print(f"Courses Offered: {self.courses_offered}")
        print(f"Faculty Members: {self.faculty_members}")
    def list_courses(self) -> None:
        print("Courses Offered:")
        for course in self.courses_offered:
            print(f"- {course}")
    def list_professors(self) -> None:
        print("Faculty Members:")
        for professor in self.faculty_members:
            print(f"- {professor}")

class Classroom: #Mariam
    def __init__(self, classroom_id: int, location: str, capacity: int, schedule: dict):
        self.classroom_id = classroom_id
        self.location = location
        self.capacity = capacity
        self.schedule = schedule
    def allocate_class(self, time_slot: str, course: str) -> None:
        if time_slot not in self.schedule:
            self.schedule[time_slot] = course
            print(f"Classroom {self.classroom_id} allocated for {course} at {time_slot}.")
        else:
            print(f"Time slot {time_slot} is already occupied.")
    def check_availability(self, time_slot: str) -> bool:
        return time_slot not in self.schedule
    def get_classroom_info(self) -> None:
        print(f"Classroom ID: {self.classroom_id}")
        print(f"Location: {self.location}")
        print(f"Capacity: {self.capacity}")
        print(f"Schedule: {self.schedule}")

class Schedule: #Mariam
    def __init__(self, schedule_id: int, course: str, professor: str, time_slot: str, location: str):
        self.schedule_id = schedule_id
        self.course = course
        self.professor = professor
        self.time_slot = time_slot
        self.location = location
    def assign_schedule(self) -> None:
        print(f"Schedule {self.schedule_id} assigned: {self.course} with {self.professor} at {self.time_slot} in {self.location}.")
    def update_schedule(self, time_slot: str = None, location: str = None) -> None:
        if time_slot:
            self.time_slot = time_slot
        if location:
            self.location = location
        print(f"Schedule {self.schedule_id} updated.")
    def view_schedule(self) -> None:
        print(f"Schedule ID: {self.schedule_id}")
        print(f"Course: {self.course}")
        print(f"Professor: {self.professor}")
        print(f"Time Slot: {self.time_slot}")
        print(f"Location: {self.location}")

class Exam: #Mariam
    def __init__(self, exam_id: int, course: str, date: str, duration: str, student_results: dict):
        self.exam_id = exam_id
        self.course = course
        self.date = date
        self.duration = duration
        self.student_results = student_results
    def schedule_exam(self) -> None:
        print(f"Exam {self.exam_id} scheduled for {self.course} on {self.date} for {self.duration}.")
    def record_results(self, student_id: int, score: float) -> None:
        self.student_results[student_id] = score
        print(f"Result recorded for student {student_id} in exam {self.exam_id}.")
    def view_exam_info(self) -> None:
        print(f"Exam ID: {self.exam_id}")
        print(f"Course: {self.course}")
        print(f"Date: {self.date}")
        print(f"Duration: {self.duration}")
        print(f"Student Results: {self.student_results}")

class GPAStimulator: #Malak
    def __init__(self):
        self.courses = [] #storing (course name & grade & credit hr)

    def add_course(self, course_name: str, grade: str, credit_hours: float):
        self.grade = grade
        self.credit_hours = credit_hours
        self.course_name = course_name
        grade_points = self.convert_grade(grade)
        if grade_points is not None:
            self.courses.append((course_name, grade_points, credit_hours))
        else:
            print(f"Invalid grade: {grade}")
    
    def convert_grade(self, grade: str): #convert to grade points
        grade_scale = {
            'A+': 4.0, 'A': 3.7,
            'B+': 3.3, 'B': 3.0,
            'C+': 2.7, 'C': 2.3,
            'D+': 2.0, 'D': 1.7,
            'F': 1.0
        }
        return grade_scale.get(grade.upper())
    
    def calculate_gpa(self): #Calcu gpa
        total_points = sum(grade * credits for _, grade, credits in self.courses)
        total_credits = sum(credits for _,_, credits in self.courses)
        
        return round(total_points / total_credits, 2) if total_credits > 0 else 0.0
    
    def display_courses(self): #displays calculated courses
        for course_name, grade, credit_hours in self.courses:
            print(f"Course name: {course_name}, Grade: {grade}, Credit hours: {credit_hours}")

class Internship(Student):#Malak
    def __init__(self, student_data, company, position, duration):
        super().__init__(
    student_data['name'],
    student_data['age'],
    student_data['address'],
    student_data['id'],
    student_data['phone_number'],
    student_data['per_email'],
    student_data['bus_email'],
    faculty=student_data['faculty'],
    enrollment_date=student_data['enrollment_date'],
    graduation_date=student_data['begin_date'],
    password=student_data['password'],
    status=student_data.get('status', 'active'),
    group=student_data.get('group', 1),
    section=student_data.get('section', 1),
    enrolled_courses=student_data.get('enrolled_courses', []),
    assignments=student_data.get('assignments', []),
    quizzes=student_data.get('quizzes', []),
    exams=student_data.get('exams', []),
    deadlines=student_data.get('deadlines', []),
    schedule=student_data.get('schedule', None),
    gpa=student_data.get('gpa', None),
    program=student_data.get('program', None)
)

        self.company = company
        self.position = position
        self.duration = duration
        self.applicants = []

    def apply_internship(self, applicant):
        if isinstance(applicant, list):
            self.applicants.extend(applicant)
        else:
            self.applicants.append(applicant)
        return f"Applied: {self.applicants}"

    def __str__(self):
        return f"Internship at {self.company} for {self.position}, duration: {self.duration}"

class research:#Malak
    researches = []

    def __init__(self, name: str, per_email , research_id: int, title: str, students_involved, start_date, end_date):
        self.name = name
        self.__per_email = per_email
        self.title = title
        self.research_id = research_id
        self.students_involved = students_involved if students_involved else []
        self.start_date = start_date
        self.end_date = end_date
        research.researches.append(self)

    @classmethod
    def add_research(cls, name, per_email , research_id, title, start_date , end_date ,students_involved=None):
        return cls(name, per_email , research_id, title, start_date, end_date, students_involved)
    
    @classmethod
    def list_researches(cls):
        for research in cls.researches:
            print(f"ID: {research.research_id}, Professor: {research.name}, Title: {research.title}, Students: {', '.join(research.students_involved)}")

class Notification:#Malak
    Notifications = []

    def __init__(self, notification_id, userr, message):
        self.notification_id = notification_id
        self.userr = userr
        self.message = message
        Notification.Notifications.append(self)

    def add_notification(self):
        Notification.Notifications.append(self)

    @staticmethod
    def display_notification():
        if not Notification.Notifications:
            print("no notifications")
            
        else:
            for notification in Notification.Notifications:
                print(f"ID: {notification.notification_id}, User: {notification.userr}, message: {notification.message}")

    @staticmethod
    def delete_notifications(notification_id):

        for notification in Notification.Notifications:
            if notification_id == notification_id:
                Notification.Notifications.remove(notification)
                print(f"{notification_id} has been deleted")
                return
            else:
                print(f"{notification_id} isn't avalible")

class Transportation:#Malak
    def __init__(self, transport_id, route, schedule, avalible_seats):
        self.transport_id = transport_id
        self.route = route
        self.schedule = schedule
        self.avalible_seats = avalible_seats
    def book_seats(self):
        if self.avalible_seats >0:
            self.avalible_seats -= 1
            print("seat booked")
        else:
            print("no avalible seats")
    def view_schedule(self):
        print(f"schedule of {self.transport_id} is: {self.schedule}")
    def view_avalible_seats(self):
        print(f"number of avalible seats are: {self.avalible_seats}")

class hostel:#Malak
    assigned_students = set()
    def __init__(self, building_name, avalibilty, room_number , room_capacity=2 ,students_assigned=0):
        self.building_name = building_name
        self.avalibilty = avalibilty
        self.room_number= room_number
        self.room_capacity= room_capacity
        self.students_assigned = students_assigned
        self.students = []
    def assign_room(self,  stu_name: str, stu_id: int):
        if stu_id in hostel.assigned_students:
            print(f"Error: Student {stu_name} (ID: {stu_id}) is already assigned to another room!")
            return
        if self.students_assigned < self.room_capacity:
            self.students.append({"name": stu_name, "id": stu_id})
            self.students_assigned +=1
            hostel.assigned_students.add(stu_id)

            print(f"Room {self.room_number} is assigned to {stu_name} id: {stu_id} in {self.building_name}")
        else:
            print(f"Error: Room {self.room_number} in {self.building_name} is full (Max: {self.room_capacity})!")
    def unassign_room(self, stu_name: str, stu_id: int):
        for student in self.students:
            if student["name"] == stu_name and student["id"] == stu_id:
                self.students.remove(student)
                hostel.assigned_students.remove(stu_id)
                self.students_assigned -= 1
                #self.avalibilty += 1 
                print(f"{stu_name} (ID: {stu_id}) has withdrawn from the hostel")
                return
        print(f"Error: Student {stu_name} (ID: {stu_id}) not found in Room {self.room_number}!")
        
    def view_info(self):
        print(f"Building: {self.building_name}, avalibilty: {self.avalibilty}, students assigned: {self.students_assigned}")
    def view_student_housing_details(self):
        if self.students:
            print(f"Room {self.room_number} in {self.building_name} has the following students:")
            for student in self.students:
                print(f" - {student['name']} (ID: {student['id']})")
        else:
            print(f"No students assigned to Room {self.room_number} in {self.building_name}")
 
class Book:  # Malak
    def __init__(self, title: str, author: str, num_pages: int, book_type: str):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.book_type = book_type
    
    def __str__(self):
        return f"{self.title} by {self.author} | Type: {self.book_type} | Pages: {self.num_pages}"

class Library:#Malak
    def __init__(self, library_id: int):
        self.library_id = library_id
        self.books = []
        self.students_registered = []
    
    def add_book(self, book: Book) -> None:
        self.books.append(book)
        print(f"Added book: {book.title}")
    
    def borrow_book(self, student_id: int, book_title: str) -> None:
        for book in self.books:
            if book.title == book_title:
                print(f"Book '{book_title}' borrowed by student {student_id}.")
                return
        print(f"Book '{book_title}' is not available.")
    
    def return_book(self, student_id: int, book_title: str) -> None:
        print(f"Book '{book_title}' returned by student {student_id}.")
    
    def check_availability(self, book_title: str) -> bool:
        return any(book.title == book_title for book in self.books)
    
    def display_books(self) -> None:
        print("\nLibrary Collection:")
        for book in self.books:
            print(f"- {book}")



foe_faculty = Faculty("FOE", [], [], [], [], [], [])
new_foe_book = foe_faculty.create_book("Electric Power", "Dr. Ahmed", 320)
print(new_foe_book)

csit_book = Book("Data Structures", "Dr. X", 300, "CSIT major")
foe_book = Book("Circuits", "Dr. Y", 250, "FOE")
pharma_book = Book("Pharmacology 101", "Dr. Z", 400, "Pharma D")

#importantttt

my_library = Library(library_id=1)

books = [csit_book, foe_book, pharma_book, new_foe_book]
for book in books:
    my_library.add_book(book)
           