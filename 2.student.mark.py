students = []
courses = []
class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.marks = {}

    def add_marks(self, student_id, marks):
        self.marks[student_id] = marks

class StudentMarkSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def num_of_stus(self):
        num_stus = int(input("Enter the number of students in the class: "))
        return num_stus

    def stu_in4(self):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth: ")
        student = Student(student_id, student_name, student_dob)
        self.students.append(student)

    def num_of_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        return num_courses

    def course_in4(self):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course = Course(course_id, course_name)
        self.courses.append(course)

    def stu_marks(self):
        course_id = input("Enter course ID: ")
        for student in self.students:
            marks = float(input(f"Enter marks for student {student.student_name} in course {course_id}: "))
            for course in self.courses:
                if course.course_id == course_id:
                    course.add_marks(student.student_id, marks)

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.course_name}")

    def list_stu(self):
        print("Students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.student_name}, DoB: {student.student_dob}")

    def show_stu_marks(self):
        course_id = input("Enter course ID: ")
        for course in self.courses:
            if course.course_id == course_id:
                print(f"Marks for course {course.course_name}:")
                for student_id, marks in course.marks.items():
                    for student in self.students:
                        if student.student_id == student_id:
                            print(f"Student: {student.student_name}, Marks: {marks}")

    def run(self):
        num_students = self.num_of_stus()
        for _ in range(num_students):
            self.stu_in4()

        num_courses = self.num_of_courses()
        for _ in range(num_courses):
            self.course_in4()

        while True:
            print("\nMenu:")
            print("1. List courses")
            print("2. List students")
            print("3. Add student marks for a course") 
            print("4. Show student marks for a given course")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.list_courses()
            elif choice == "2":
                self.list_stu()
            elif choice == "3":
                self.stu_marks()
            elif choice == "4":
                self.show_stu_marks()
            elif choice == "5":
                break
            else:
                print("Error. Please try again.")

student_mark_system = StudentMarkSystem()
student_mark_system.run()

