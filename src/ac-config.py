# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck ac-config.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################

#ac_config
#this class is used to setup and store the teacher's name, email
#   and a class description
class ac_config:
    #vars
    teacherName
    teacherEmail
    classDescrip

    #pre:takes in a string n
    #post:sets the teacherName variable to n
    def set_teacher_name(n):
        self.teacherName = n

    #pre:none
    #post:returns a string of the teacher's name
    def get_teacher_name():
        return self.teacherName

    #pre:takes in a string e
    #post:sets the teacherEmail variable to e
    def set_teacher_email(e):
        self.teacherEmail = e

    #pre:none
    #post:returns a string of the teacher's email address
    def get_teacher_email():
        return self.teacherEmail

    #pre:takes in a string d
    #post:sets the classDescrip variable to d
    def set_class_descrip(d):
        self.classDescrip = d

    #pre:none
    #post:returns a string of the class description
    def get_class_descrip():
        return self.classDescrip
