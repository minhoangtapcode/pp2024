students=[]
courses=[]
#input number of students
def list_number_students():
    x = int(input("Type the number of students in the class: "))
    return x
#input student information
def information_students():
    name = input("Type student name: ")
    student_id = input("Type student ID: ")
    dob = input("Date of birth (DD-MM-YYYY): ")
    return {'id': student_id, 'name': name,'dob': dob, 'marks': {}}
#input number of courses
def list_number_courses():
    x = int(input("Type the number of courses: "))
    return x
#input course in4
def courses_info():
    courses_id = int(input("Course ID: "))
    name = input("Course name: ")
    return {'id': courses_id, 'name': name}
#input mark for students
def courses_and_marks(students, courses):
    list_courses(courses)
    courses_id = int(input("Course order ID to input marks: "))

    for student in students:
        mark = float(input(f"Enter {student['name']}'s mark for {courses[courses_id-1]['name']}: "))
        student['marks'][courses_id] = mark

    print("Marks update")

def list_courses(courses):
    print("\nList of Courses: ")
    i = 0
    for course in courses:
        print(f"{i+1}...ID: {course['id']}, Name: {course['name']}")
        i=i+1

def list_students(Students):
    print("\nList of Students: ")
    for student in Students:
        print(f"ID: {student['id']}, Name: {student['name']}")
#show marks
def show_student_course_marks(students, courses):
    list_students(students)
    student_id = input("Student id to see marks: ")

    if not any(student['id'] == student_id for student in students):
        print(f"Error Student Id: {student_id}")
        return
    
    list_courses(courses)
    course_id =int(input("Course id to see marks: "))

    if not any(course_id in courses['marks'] for student in students):
        print(f"Error Course ID: {course_id} and Student ID: {student_id}")
        return

    
    print(f"\nMarks for Student ID: {student_id} in Course ID: {course_id}: {students[students.index({'id': student_id})]['marks'][course_id]} ")

num_students = list_number_students()
for _ in range(num_students):
    students.append(information_students())

num_courses = list_number_courses()
for _ in range(num_courses):
    courses.append(courses_info())

#choosing
while True:
    print("\nStudent Mark Management System")
    print("1. Select Course and Input Marks")
    print("2. List Courses")
    print("3. List Students")
    print("4. Show Student Marks for a Course")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        courses_and_marks(students, courses)

    elif choice == '2':
        list_courses(courses)

    elif choice == '3':
        list_students(students)

    elif choice == '4':
        show_student_course_marks(students, courses)

    elif choice == '5':
        print("Exiting the Student Mark Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")