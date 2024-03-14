from domain.course import Course
from domain.marks import StudentMarkSystem
from domain.students import Student

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

