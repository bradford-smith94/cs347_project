# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck teacher.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
#import person class
from person import person

#teacher
#this class provides the structure of a teacher
#   teacher is a person with an email password
class student(person):

    #constructor
    def __init__(self, name, email, pw):
        person.__init__(self, name, email)
        self.password = pw

    #pre:none
    #post:returns the variable password
    def get_password(self):
        return self.password
