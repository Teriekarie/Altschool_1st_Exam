# The Person class is a base class for both Student and Instructor.
# It holds common attributes like name and ID number.
class Person:
    def __init__(self, name, id_number):
        # Initialize the Person object with a name and ID number
        self.name = name
        self.id_number = id_number

    def __str__(self):
        # Return a string representation of the Person object
        return f"Name: {self.name}, ID: {self.id_number}"


# The Student class inherits from the Person class and represents a student.
class Student(Person):
    def __init__(self, name, id_number, major):
        # Initialize the Student object using the Person initializer
        super().__init__(name, id_number)
        # Add a major attribute specific to students
        self.major = major

    def __str__(self):
        # Return a string representation of the Student object,
        # including the major field.
        return f"{super().__str__()}, Major: {self.major}"


# The Instructor class inherits from the Person class and represents an instructor.
class Instructor(Person):
    def __init__(self, name, id_number, department):
        # Initialize the Instructor object using the Person initializer
        super().__init__(name, id_number)
        # Add a department attribute specific to instructors
        self.department = department

    def __str__(self):
        # Return a string representation of the Instructor object,
        # including the department field.
        return f"{super().__str__()}, Department: {self.department}"

# The Course class represents a course that students can enroll in.
class Course:
    def __init__(self, course_name, course_id):
        # Initialize the Course object with a course name and ID
        self.course_name = course_name
        self.course_id = course_id
        # A list to keep track of enrolled students
        self.enrolled_students = []

    def add_student(self, student):
        # Add a student to the course if they are not already enrolled
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)

    def remove_student(self, student):
        # Remove a student from the course if they are enrolled
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)

    def __str__(self):
        # Return a string representation of the Course object,
        # including the list of enrolled students.
        students_list = ', '.join([student.name for student in self.enrolled_students])
        return f"Course Name: {self.course_name}, ID: {self.course_id}, Enrolled Students: {students_list}"


# The Enrollment class represents the enrollment of a student in a course.
class Enrollment:
    def __init__(self, student, course):
        # Initialize the Enrollment object with a student and a course
        self.student = student
        self.course = course
        # The grade is initially set to None
        self.grade = None

    def assign_grade(self, grade):
        # Assign a grade to the student for this course
        self.grade = grade

    def __str__(self):
        # Return a string representation of the Enrollment object,
        # including the assigned grade.
        return f"Student: {self.student.name}, Course: {self.course.course_name}, Grade: {self.grade}"


# The StudentManagementSystem class manages students, instructors, courses, and enrollments.
class StudentManagementSystem:
    def __init__(self):
        # Lists to keep track of all students, instructors, courses, and enrollments
        self.students = []
        self.instructors = []
        self.courses = []
        self.enrollments = []

    # Methods to manage students
    def add_student(self, student):
        # Add a student to the system
        self.students.append(student)

    def remove_student(self, student):
        # Remove a student from the system
        if student in self.students:
            self.students.remove(student)

    def update_student(self, student, name=None, major=None):
        # Update a student's details in the system
        if student in self.students:
            if name:
                student.name = name
            if major:
                student.major = major

    # Methods to manage instructors
    def add_instructor(self, instructor):
        # Add an instructor to the system
        self.instructors.append(instructor)

    def remove_instructor(self, instructor):
        # Remove an instructor from the system
        if instructor in self.instructors:
            self.instructors.remove(instructor)

    def update_instructor(self, instructor, name=None, department=None):
        # Update an instructor's details in the system
        if instructor in self.instructors:
            if name:
                instructor.name = name
            if department:
                instructor.department = department

    # Methods to manage courses
    def add_course(self, course):
        # Add a course to the system
        self.courses.append(course)

    def remove_course(self, course):
        # Remove a course from the system
        if course in self.courses:
            self.courses.remove(course)

    # Methods to manage enrollments
    def enroll_student(self, student, course):
        # Enroll a student in a course
        if student in self.students and course in self.courses:
            course.add_student(student)
            enrollment = Enrollment(student, course)
            self.enrollments.append(enrollment)

    def assign_grade(self, student, course, grade):
        # Assign a grade to a student for a specific course
        for enrollment in self.enrollments:
            if enrollment.student == student and enrollment.course == course:
                enrollment.assign_grade(grade)
                break

    # Methods to retrieve information
    def get_students_in_course(self, course):
        # Get a list of students enrolled in a specific course
        return [student.name for student in course.enrolled_students]

    def get_courses_for_student(self, student):
        # Get a list of courses a specific student is enrolled in
        return [enrollment.course.course_name for enrollment in self.enrollments if enrollment.student == student]



## Testing the Student Management System

# Create a student and an instructor
student1 = Student("John Doe", "S001", "Computer Science")
instructor1 = Instructor("Dr. Smith", "I001", "Computer Science")

# Create a course
course1 = Course("Python Programming", "C001")

# Create the management system
sms = StudentManagementSystem()

# Add student, instructor, and course to the system
sms.add_student(student1)
sms.add_instructor(instructor1)
sms.add_course(course1)

# Enroll the student in the course
sms.enroll_student(student1, course1)

# Assign a grade
sms.assign_grade(student1, course1, "A")


# Retrieve students in a course
print("Students enrolled in Python Programming:")

print(sms.get_students_in_course(course1))

# Retrieve courses for a student
print("Courses John Doe is enrolled in:")
print(sms.get_courses_for_student(student1))


## More instances

# Adding students
student1 = Student("Meredith Grey", "S004", "Computer Science")
student2 = Student("Jackson Booman", "S006", "Mechanical Engineering")
student3 = Student("Alice Dakota", "S003", "Electrical Engineering")
student4 = Student("Bob Brown", "S009", "Civil Engineering")
student5 = Student("Anita Baker", "S019", "Medcine")
sms.add_student(student1)
sms.add_student(student2)
sms.add_student(student3)
sms.add_student(student4)
print("Students after adding:")
for student in sms.students:
    print(student)


# Removing a student
sms.remove_student(student4)
print("\nStudents after removing Bob Brown:")
for student in sms.students:
    print(student)

# Updating a student
sms.update_student(student3, name="Alice Davis", major="Software Engineering")
print("\nStudents after updating Alice Johnson to Alice Davis:")
for student in sms.students:
    print(student)

# Adding instructors
instructor1 = Instructor("Dr. Gorge", "I004", "Computer Science")
instructor2 = Instructor("Dr. Williams", "I006", "Mechanical Engineering")
sms.add_instructor(instructor1)
sms.add_instructor(instructor2)
print("\nInstructors after adding:")
for instructor in sms.instructors:
    print(instructor)

# Removing an instructor
sms.remove_instructor(instructor2)
print("\nInstructors after removing Dr. Williams:")
for instructor in sms.instructors:
    print(instructor)

# Updating an instructor
sms.update_instructor(instructor1, name="Dr. John Smith", department="Data Science")
print("\nInstructors after updating Dr. Smith to Dr. John Smith:")
for instructor in sms.instructors:
    print(instructor)

# Adding courses
course1 = Course("Python Programming", "C009")
course2 = Course("Thermodynamics", "C008")
course3 = Course("Data Structures", "C007")
course7 = Course("Data Types", "C017")
sms.add_course(course1)
sms.add_course(course2)
sms.add_course(course3)
print("\nCourses after adding:")
for course in sms.courses:
    print(course)

# Removing a course
sms.remove_course(course2)
print("\nCourses after removing Thermodynamics:")
for course in sms.courses:
    print(course)

# Updating a course (in this case, let's just modify the course name directly for simplicity)
course3.course_name = "Advanced Data Structures"
print("\nCourses after updating Data Structures to Advanced Data Structures:")
for course in sms.courses:
    print(course)

# Enrolling students in courses
sms.enroll_student(student1, course1)
sms.enroll_student(student2, course1)
sms.enroll_student(student3, course3)
print("\nEnrollments after enrolling students in courses:")
for enrollment in sms.enrollments:
    print(enrollment)

# Assigning grades to students
sms.assign_grade(student1, course1, "A")
sms.assign_grade(student2, course1, "B")
sms.assign_grade(student3, course3, "A-")
print("\nEnrollments after assigning grades:")
for enrollment in sms.enrollments:
    print(enrollment)

# Retrieve a list of students enrolled in a specific course
print("\nStudents enrolled in Python Programming:")
print(sms.get_students_in_course(course1))

print("\nStudents enrolled in Advanced Data Structures:")
print(sms.get_students_in_course(course3))

# Retrieve a list of courses a specific student is enrolled in
print("\nCourses John Doe is enrolled in:")
print(sms.get_courses_for_student(student1))

print("\nCourses Alice Davis is enrolled in:")
print(sms.get_courses_for_student(student3))


##Error Handling
#this is to manage cases like trying to remove a student who doesn't exist or 
# enrolling a student in a course they are already enrolled in.

def remove_student(self, student):
    if student in self.students:
        self.students.remove(student)
    else:
        print(f"Error: {student.name} is not in the student list.")

def enroll_student(self, student, course):
    if student in self.students and course in self.courses:
        if student not in course.enrolled_students:
            course.add_student(student)
            enrollment = Enrollment(student, course)
            self.enrollments.append(enrollment)
        else:
            print(f"Error: {student.name} is already enrolled in {course.course_name}.")
    else:
        print("Error: Either the student or the course is not in the system.")


# Error Handling Example 1: Attempt to remove a student who is not in the system
print("\nAttempting to remove a student who is not in the system:")
sms.remove_student(student5)  # student5 (Anita Baker) was never added, so this should trigger an error

# Enroll a student in the course
sms.enroll_student(student1, course1)  # This should succeed

# Error Handling Example 2: Enroll a student in a course they are already enrolled in
print("\nAttempting to enroll the same student again in the same course:")
sms.enroll_student(student1, course1)  # This should trigger an error because student1 is already enrolled

# Error Handling Example 3: Attempt to enroll a student in a course that is not in the system
print("\nAttempting to enroll a student in a course that is not in the system:")
course2 = Course("Advanced Algorithms", "C010")  # This course is not added to the system
sms.enroll_student(student2, course2)  # This should trigger an error because course2 is not in the system

# Error Handling Example 4: Attempt to enroll a student who is not in the system
print("\nAttempting to enroll a student who is not in the system:")
sms.enroll_student(student5, course1)  # This should trigger an error because student5 is not in the system
