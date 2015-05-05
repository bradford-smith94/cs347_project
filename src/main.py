# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck main.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
#all the imports
from ac_attendance import ac_attendance
from ac_notify import ac_notify
from ac_config import ac_config
from person import person
from student import student
from admin import admin
from teacher import teacher
from ac_stats import ac_stats

def main():
    #vars
    teacher_name = ""
    teacher_email = ""
    teacher_pw = ""
    class_descript = ""
    config = ac_config()

    #prompting teacher to enter name
    #loop executes until user enters something (string cannot be empty)
    while True:
        name = raw_input("Please enter your name: ")
        type(name)
        if (len(name) > 0):
            break
    teacher_name = name

    #prompting teacher to enter email
    #loop executes until user enters something (string cannot be empty)
    while True:
        email = raw_input("Please enter your email: ")
        type(email)
        if (len(email) > 0):
            break
    teacher_email = email

    #prompting the teacher to enter email password
    #loop executes until user enters something (string cannot be empty)
    while True:
        password = raw_input("Please enter your email password: ")
        type(password)
        if (len(password) > 0):
            break
    teacher_pw = password

    teacher1 = teacher(teacher_name, teacher_email, teacher_pw)

    #prompting teacher to enter a class description
    #loop executes until user enters something (string cannot be empty)
    while True:
        classDescrip = raw_input("Please enter todays topics covered, assignments and/or related material: ")
        type(classDescrip)
        if (len(classDescrip) > 0):
            break
    class_descript = classDescrip

    #initialize the config object
    config.set_teacher(teacher1)
    config.set_class_descrip(classDescrip)

main()
