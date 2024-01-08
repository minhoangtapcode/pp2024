students = []
courses = []

#students
def num_of_stus():
    num_stus = int(input("Enter the number of students in the class: "))
    return num_stus

def stu_in4():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    student = (student_id, student_name, student_dob)
    students.append(student)

#courses
def num_of_courses():
    num_courses = int(input("Enter the number of courses: "))
    return num_courses

def course_in4():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    course = {"id": course_id, "name": course_name, "marks": {}}
    courses.append(course)

#marks
def stu_marks():
    course_id = input("Enter course ID: ")
    for student in students:
        marks = float(input(f"Enter marks for student {student[1]} in course {course_id}: "))
        for course in courses:
            if course["id"] == course_id:
                course["marks"][student[0]] = marks

#list
def list_courses():
    print("Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def list_stu():
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

#show
def show_stu_marks():
    course_id = input("Enter course ID: ")
    for course in courses:
        if course["id"] == course_id:
            print(f"Marks for course {course['name']}:")
            for student_id, marks in course["marks"].items():
                for student in students:
                    if student[0] == student_id:
                        print(f"Student: {student[1]}, Marks: {marks}")

#main
num_students = num_of_stus()
for _ in range(num_students):
    stu_in4()

num_courses = num_of_courses()
for _ in range(num_courses):
    course_in4()

while True:
    print("\nMenu:")
    print("1. List courses")
    print("2. List students")
    print("3. Show student marks for a given course")
    print("4. Add student marks for a course")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        list_courses()
    elif choice == "2":
        list_stu()
    elif choice == "3":
        show_stu_marks()
    elif choice == "4":
        stu_marks()
    elif choice == "5":
        break
    else:
        print("Error. Please try again.")