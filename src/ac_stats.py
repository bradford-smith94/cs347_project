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

#import python stat function
import os

#ac_stats
#this class is used to save cumulative attendance statistics to a csv file
#   optionally this class will also notify an administrator if requested
class ac_stats:

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
    def save_stats(self, lst, outfile="cumulative.csv"):
        #open csv for reading and writing (r+), check if csv is empty (first time ran)
        with open(outfile, 'r+') as csv_file:
            if os.stat(csv_file).st_size == 0:
                #file is empty, write it ourselves
                writer = csv.writer(csv_file, delimiter = ',')
                cumm_attendance = 0
                for student in lst:
                    if student.get_attendance():
                        cumm_attendance = 0
                    else:
                        cumm_attendance = 1
                    line = [student.get_name(), student.get_email(), cumm_attendance]

                    writer.writerow(line)
            else:
                #file is not empty, read and update
                csv_reader = csv.reader(csv_file)
                for student in lst:
                    updated = False
                    for line in csv_reader:
                        if student.get_name() == str(line[0]) and not student.get_attendance():
                            cumm_attendance = int(line[2])
                            cumm_attendance += 1
                            line[2] = cumm_attendance
                            updated = True
                    if not updated:
                        #this is a new student add a line in csv
                        if student.get_attendance():
                            cumm_attendance = 0
                        else:
                            cumm_attendance = 1
                        csv_writer = csv.writer(csv_file, delimiter = ',')
                        line = [student.get_name(), student.get_email(), cumm_attendance].split(",")
                        writer.writerow(line)
            csv_file.close()
