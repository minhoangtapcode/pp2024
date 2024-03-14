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
        credits = int(input("Enter course credits: "))
        course = Course(course_id, course_name, credits)
        self.courses.append(course)

    def stu_marks(self):
        course_id = input("Enter course ID: ")
        for student in self.students:
            marks = float(input(f"Enter marks for student {student.student_name} in course {course_id}: "))
            marks = math.floor(marks * 10) / 10  
            for course in self.courses:
                if course.course_id == course_id:
                    course.add_marks(student.student_id, marks)

    def calculate_average_gpa(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student.calculate_gpa()

    def sort_students_by_gpa(self):
        sorted_students = sorted(self.students, key=lambda student: student.calculate_gpa(), reverse=True)
        return sorted_students


    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.course_name}, Credits: {course.credits}")

    def list_stu(self):
        print("Students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.student_name}, DoB: {student.student_dob}")