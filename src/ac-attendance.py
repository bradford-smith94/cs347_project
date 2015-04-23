# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck ac-attendance.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################

#ac_attendance
#this class is used to create and store a listOfStudents for taking attendance
class ac_attendance:
    listOfStudents = []
    listOfAbsentStudents = []

    #pre:takes in a file f
    #post:creates the listOfStudent variable from the students in the file
    def parse_file(f):
        #open file f
        #create new_student object for each student name and email found
        listOfStudents.append(new_student)

    #pre:none
    #post:returns the listOfStudents variable
    def get_listOfStudents():
        return self.listOfStudents

    #pre:none
    #post:listOfAbsentStudents variable is filled with all students who are absent
    def update_listOfAbsentStudents():
        for i in self.listOfStudents:
            if not i.get_attendance():
                self.listOfAbsentStudents.append(i)

    #pre:none
    #post:returns listOfAbsentStudents variable
    def get_listOfAbsentStudents():
        update_listOfAbsentStudents
        return self.listOfAbsentStudents

