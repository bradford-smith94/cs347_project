# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck student.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
from person import person

class student(person):

    def __init__(self, name, email, here=True):
        person.__init__(self, name, email)
        self.isHere = here #assume a student is here until otherwise known

    def set_attendance(here):
        if(here):
            isHere = True
        else:
            isHere = False

    def get_attendance():
        return self.isHere
