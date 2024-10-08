# Altschool_1st_Exam
# Student Management System

## Overview

This project is a simple Student Management System implemented using Object-Oriented Programming (OOP) principles in Python. The system allows for the management of students, instructors, courses, and enrollments. It demonstrates the use of classes, objects, inheritance, polymorphism, and encapsulation.

## Class Structure

- **Person**: A base class for Student and Instructor with common attributes like name and id_number.
- **Student**: Inherits from Person and includes attributes specific to students, such as major.
- **Instructor**: Inherits from Person and includes attributes specific to instructors, such as department.
- **Course**: Represents a course with attributes such as course_name, course_id, and a list of enrolled students.
- **Enrollment**: Represents the enrollment of a student in a course with attributes such as student, course, and grade.
- **StudentManagementSystem**: Manages the students, instructors, courses, and enrollments, providing methods to add, remove, update, and retrieve data.

## Functionalities

- Add, remove, and update students and instructors.
- Add, remove, and update courses.
- Enroll students in courses.
- Assign grades to students for specific courses.
- Retrieve a list of students enrolled in a specific course.
- Retrieve a list of courses a specific student is enrolled in.

## Usage

1. **Initialize the system**:
    
    sms = StudentManagementSystem()


2. **Add a student**:
    
    student1 = Student("John Doe", "S001", "Computer Science")
    sms.add_student(student1)


3. **Add a course**:
    
    course1 = Course("Python Programming", "C001")
    sms.add_course(course1)


4. **Enroll the student in a course**:
    
    sms.enroll_student(student1, course1)


5. **Assign a grade**:
    
    sms.assign_grade(student1, course1, "A")


6. **Retrieve information**:
    
    print(sms.get_students_in_course(course1))
    print(sms.get_courses_for_student(student1))


## Conclusion

This Student Management System project provides a robust example of Object-Oriented Programming in Python. Through the use of classes and objects, the system effectively manages students, instructors, courses, and enrollments, demonstrating key OOP principles such as inheritance, encapsulation, and polymorphism.

Each class is responsible for specific aspects of the system, ensuring that the code is maintainable and easy to understand. The system includes error handling to manage common issues, such as attempting to enroll a student who is already enrolled or removing a non-existent student, which makes the system more user-friendly and resilient.

Furthermore, the project includes comprehensive examples and test cases, showcasing how the system can be used in practice. This not only verifies the correctness of the implementation but also serves as a guide for future enhancements.


Overall, this project lays a strong foundation for a fully functional Student Management System, with opportunities for further development and customization based on specific needs.
