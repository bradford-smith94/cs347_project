# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck student.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################

class student(person):
    isHere = true #assume a student is here until otherwise known

    def set_attendance(here):
        if(here):
            isHere = true
        else:
            isHere = false

    def get_attendance():
        return self.isHere
