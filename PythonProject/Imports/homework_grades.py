"""
-Modules get used all the time throughout programming
-It helps with creating more files,with unique purposes,to help with clean maitainable code.
"""
import Imports.grade_average_service  as grade_service
homework_assignment_grades ={
    'homework_1':85,
    'homework_2':90,
    'homework_3':95,
}



grade_service.calculate_grade(homework_assignment_grades)