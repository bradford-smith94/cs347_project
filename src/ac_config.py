# Bradford Smith and David Ott
# CS 347 Project
# AbsenceCheck ac_config.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
#import teacher class
from teacher import teacher

#ac_config
#this class is used to setup and store the teacher
#   and a class description
class ac_config:
    #vars
    teacher
    classDescrip = ""

    #pre:takes in a teacher t
    #post:sets the teacher variable to t
    def set_teacher(self, t):
        self.teacher = t

    #pre:none
    #post:returns the teacher variable
    def get_teacher(self):
        return self.teacher

       #pre:takes in a string d
    #post:sets the classDescrip variable to d
    def set_class_descrip(self, d):
        self.classDescrip = d

    #pre:none
    #post:returns a string of the class description
    def get_class_descrip(self):
        return self.classDescrip
