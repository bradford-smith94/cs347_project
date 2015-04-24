# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck ac-attendance.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
#import csv to read .csv files
import csv
#import student class
from student import student

#ac_attendance
#this class is used to create and store a listOfStudents for taking attendance
class ac_attendance:
    listOfStudents = []
    listOfAbsentStudents = []

    #pre:takes in a csv file f
    #post:creates the listOfStudent variable from the students in the file
    def parse_file(self, f):
        with open(f, 'r') as csvfile:
            lineReader = csv.reader(csvfile, delimiter=',')
            for line in lineReader:
                fn = line[0] #first name
                ln = line[1] #last name
                em = line[2] #email
                new_student = student(" ".join([fn, ln]), em)
                self.listOfStudents.append(new_student)

    #pre:none
    #post:returns the listOfStudents variable
    def get_listOfStudents(self):
        return self.listOfStudents

    #pre:none
    #post:listOfAbsentStudents variable is filled with all students who are absent
    def update_listOfAbsentStudents(self):
        for i in self.listOfStudents:
            if not i.get_attendance():
                self.listOfAbsentStudents.append(i)

    #pre:none
    #post:returns listOfAbsentStudents variable
    def get_listOfAbsentStudents(self):
        self.update_listOfAbsentStudents()
        return self.listOfAbsentStudents

