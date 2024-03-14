class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob
        self.marks = {}

    def calculate_gpa(self):
        total_credits = 0
        weighted_sum = 0
        for course_id, marks in self.marks.items():
            for course in courses:
                if course.course_id == course_id:
                    total_credits += course.credits
                    weighted_sum += course.credits * marks
        if total_credits == 0:
            return 0
        else:
            return weighted_sum / total_credits
        