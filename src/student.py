# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck student.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
#import person class
from person import person

#student
#this class provides the structure of a student
#   student is a person with attendance
class student(person):

    #constructor
    def __init__(self, name, email, here=True):
        person.__init__(self, name, email)
        self.isHere = here #assume a student is here until otherwise known

    #pre:takes in a boolean here (True = student present, False = student absent)
    #post:sets the isHere variable to here
    def set_attendance(self, here):
        if(here):
            isHere = True
        else:
            isHere = False

    #pre:none
    #post:returns the isHere variable
    def get_attendance(self):
        return self.isHere
