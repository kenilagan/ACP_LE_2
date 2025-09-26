class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.id_name = (student_id, student_name) # store id and name as a tuple
        self.email = email 
        self.grades = grades if grades is not None else {} # dictionary for grades        
        self.courses = courses if courses is not None else set() # set for unique courses
        
    # show student info
    def __str__(self):
        return f"ID: {self.id_name[0]}, Name: {self.id_name[1]}, Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}"

    # challenge: compute GPA
    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        scale = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0}
        total = 0
        for score in self.grades.values():
            total += scale.get(score, 0)
        return round(total / len(self.grades), 2)

class StudentRecords:
    def __init__(self):
        self.students = []

    # add new student
    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        s = Student(student_id, student_name, email, grades, courses)
        self.students.append(s)
        return "Student added successfully"

    # update existing student
    def update_student(self, student_id, email=None, grades=None, courses=None):
        for s in self.students:
            if s.id_name[0] == student_id:
                if email:
                    s.email = email
                if grades:
                    s.grades.update(grades)
                if courses:
                    s.courses.update(courses)
                return "Student updated successfully"
        return "Student not found"

    # delete a student
    def delete_student(self, student_id):
        for s in self.students:
            if s.id_name[0] == student_id:
                self.students.remove(s)
                return "Student deleted successfully"
        return "Student not found"

    # enroll student in a course
    def enroll_course(self, student_id, course):
        for s in self.students:
            if s.id_name[0] == student_id:
                s.courses.add(course)
                return "Course enrolled successfully"
        return "Student not found"

    # search student by ID
    def search_student(self, student_id):
        for s in self.students:
            if s.id_name[0] == student_id:
                return str(s)
        return "Student not found"

    # challenge: search by name (partial match)
    def search_by_name(self, name):
        results = []
        for s in self.students:
            if name.lower() in s.id_name[1].lower():
                results.append(str(s))
        return results if results else "No student found"
        
records = StudentRecords()

# adding 3 students
print(records.add_student(1, "Jhon Rhei", "jhonrhei@email.com",
                          {"Advanced Computer Programming": "A"},
                          {"Advanced Computer Programming"}))

print(records.add_student(2, "Ken", "ken@email.com",
                          {"Object-Oriented Programming": "B"},
                          {"Object-Oriented Programming"}))

print(records.add_student(3, "Drei", "drei@email.com",
                          {"Database Management System": "C"},
                          {"Database Management System"}))

# show all students
print(records.search_student(1))
print(records.search_student(2))
print(records.search_student(3))

# enroll Ken in a new course
print(records.enroll_course(2, "Computer Networking"))

# update email and grade
print(records.update_student(3, email="andrei123@email.com",
                             grades={"Advanced Computer Programming": "B"}))

# delete Jhon Rhei
print(records.delete_student(1))

# search by name
print(records.search_by_name("dr"))

# show GPA for Ken
print("Ken GPA:", records.students[0].calculate_gpa())

