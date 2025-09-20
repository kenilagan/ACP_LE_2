class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.student_id = student_id
        self.student_name = student_name
        self.email = email
        self.grades = grade if grades is not None else{}
        self.courses = courses if courses is not None else{}
    pass

class StudentRecords:
    def __init__(self):
        return f"Student ID: {self.student_id}, Name: {self.student_name}, Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}"
    pass

    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        student = student(student_id, student_name, email, grades, courses):
        self.student.append(student)
        return "Student added successfully"
    pass

    def update_student(self, student_id, email=None, grades=None, courses=None):
    
    pass

    def delete_student(self, student_id):
    
    pass

    def enroll_course(self, student_id, course):
    
    pass

    def search_student(self, student_id):
    
    pass
