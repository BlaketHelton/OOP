from datetime import date

class Student:



    def __init__(self, studentID, name, DOB, classification):
        self.studentID = studentID 
        self.name = name 
        self.DOB = DOB
        self.classification = classification

    def calculate_age(self):
        today = date.today()
        age_in_years = today.year - self.DOB.year
        
    def 