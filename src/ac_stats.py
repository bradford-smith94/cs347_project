# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck ac_stats.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
#import csv to read and save .csv files
import csv
#import student and admin classes
from student import student
from admin import admin
from ac_notify import ac_notify

#ac_stats
#this class is used to save cumulative attendance statistics to a csv file
#   optionally this class will also notify an administrator if requested
class ac_stats:
    admin1

    #pre: takes in an admin a
    #post: sets the admin variable to a
    def set_admin(self, a):
        self.admin1 = a

    #pre:none
    #post:returns the admin variable
    def get_admin(self):
        return self.admin1

    #pre:takes in a list of students lst, and optionally a filename
    #post:saves cumulative absences in a csv file, and if admin.get_request
    #   notifies the admin
    def save_stats(self, lst, file="cumulative.csv"):
        print("TODO")
        #for each student in list of students print in csv
        #if student is absent incremenet absences
        #read absences from csv parse to int and increment
        #two cases (if csv already exists, if we have to make it)
