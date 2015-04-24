# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck main.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
import sys


from ac_attendance import ac_attendance
from ac_notify import ac_notify
from ac_config import ac_config
from person import person
from student import student
from admin import admin
from teacher import teacher


def main():
    #vars
    teacher_name = ""
    teacher_email = ""
    teacher_pw = ""
    class_descript = ""
    config = ac_config()
   
    
    
    #promptig teacher to enter name
    name = raw_input("please enter your name: ")
    type(name)
    teacher_name = name
    
    #prompting teacher to enter email
    email = raw_input("please enter your email: ")
    type(email)
    teacher_email = email	
    
    #prompting the teacher to enter her email password
    password = raw_input("please enter your email password: ")
    type(password)
    teacher_pw = password
   
    teacher1 = teacher(teacher_name, teacher_email, teacher_pw)
    
    #prompting teacher to enter a class description
    classDescrip = raw_input("Please enter todays topics covered, assignments and related material: ")
    type(classDescrip)
    class_descript = classDescrip
    
    
    config.set_teacher(teacher1)
    config.set_class_descrip(classDescrip)
			





main()		

