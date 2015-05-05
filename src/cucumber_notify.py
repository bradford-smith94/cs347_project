# Bradford Smith and David Ott
# CS 347 Project
# AbsenceCheck cucumber_notify.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
#enable the print function from python3 in python2
from __future__ import print_function
#import student class
from student import student
#import sys to get command line args
import sys

def create_student(email, status):
    if (status == "present"):
        status = True
    else:
        status = False

    return student("Filler", email, status)

student = create_student(sys.argv[1], sys.argv[2])
if (not student.isHere):
    print("y", end="")
else:
    print("n", end="")
