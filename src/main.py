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

#module that handles command line arguments
import sys
import csv
import os

def main():
    #vars
    attendance = ac_attendance()
    config = setup_config()
    stats = ac_stats()
    notify = ac_notify()

    #we now need to take attendence and set the listOfAbsentStudents
    print("Please take attendance:")
    print("#######################")

    attendance.parse_file('test.csv')
    it = iter(attendance.listOfStudents)
    for student in it:
        print(student.name)
        var = str(raw_input("Present? (Y or N): "))
        var = var.lower()
        if var == "y":
            student.set_attendance(True)
        elif var == "n":
            student.set_attendance(False)
        else:
            while var != "y" and var != "n":
                var = str(raw_input("Please enter valid character (Y or N): "))
                var = var.lower()


    #setting up stats
    admin1 = setup_admin()
    stats.set_admin(admin1)
    stats.save_stats(attendance.get_listOfStudents())


def setup_admin():
    #vars
    admin_name = ""
    admin_email = ""
    admin_bool = True

    #setting up optional email to administrators
    boolval = raw_input("Would you like to send the cumulative absence statistics to an admisistrator? (Y or N): ")
    boolval = boolval.lower()
    if boolval == "y":
        adminName = raw_input("Please enter Administrators name: ")
        admin_name = adminName
        adminEmail = raw_input("Please enter Administrators email: ")
        admin_email = adminEmail
    elif boolval == "n":
        admin_bool = False
    else:
        while boolval != "y" and boolval != "n":
            boolval = str(raw_input("Please enter a valid character (Y or N): "))
            boolval = boolval.lower()
    return admin(admin_name, admin_email, admin_bool)


def setup_teacher():
    #vars
    teacher_name = ""
    teacher_email = ""
    teacher_pw = ""

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

    return teacher(teacher_name, teacher_email, teacher_pw)


def setup_config():
    #vars
    teacher1 = setup_teacher()
    class_descript = ""
    config = ac_config()


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
    return config


#call main to run the program
main()
