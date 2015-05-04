# Bradford Smith and David Ott
# CS 347 Project
# AbsenceCheck cucumber_attendance.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
#enable the print function from python3 in python2
from __future__ import print_function
#import student class
from student import student
#import sys to get command line args
import sys

def create_student(name, isHere):
    if (isHere == "y"):
        isHere = True
    else:
        isHere = False

    test = student(name, "filler@email.com", isHere)
    return test

student = create_student(sys.argv[1], sys.argv[2])
if (student.isHere):
    print("present", end="")
else:
    print("absent", end="")
