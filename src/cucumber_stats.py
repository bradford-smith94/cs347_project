# Bradford Smith and David Ott
# CS 347 Project
# AbsenceCheck cucumber_stats.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
#enable the print function from python3 in python2
from __future__ import print_function
#import student class
from student import student
#import sys to get command line args
import sys

def create_student(name, status):
    if (status == "present"):
        status = True
    else:
        status = False

    return student(name, "filler@email.com", status)

student = create_student(sys.argv[1], sys.argv[2])
total = int(sys.argv[3])
if (not student.isHere):
    total += 1
print("%d" % total, end="")
