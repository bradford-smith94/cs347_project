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
    

    def save_stats(self, file="cumulative.csv", lst):
        #open csv, check if csv is empty (first time ran)
        with open("cumulative.csv") as csv_file:
        if os.stat(csv_file).st_size == 0:
        	#print("The csv file is empty")
        	#write and read
        	writer = csv.writer(csv_file, delimiter = ',')       
        	int cumm_attendence
        	for student in listOfStudents:
        		if student.isHere:
        			cumm_attendence = 0
        		else:
        			cumm_attendence = 1	
        		line = [student.name, student.email, cumm_attendence].split(",")
        		writer.writerow(line)
        else:
        #comparing list of absent students with current cumulative csv and updating cumulative attendence 
        	csv_reader = csv.reader(csv_file) 
        	for student in listOfAbsentStudents:
        		for line in csv_reader:
        			if student.name == line[0] and student.isHere        		
        			cumm_attendence += 1
        	       
        

     
        
        #for each student in list of students print in csv
        #if student is absent incremenet absences
        #read absences from csv parse to int and increment
        #two cases (if csv already exists, if we have to make it)
