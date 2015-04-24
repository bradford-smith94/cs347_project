# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck ac-notify.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
from ac_config import ac_config
from ac_attendance import ac_attendance
from student import student
from person import person

#ac_notify
#this class is used to send the config file to absent students
class ac_notify:

    #vars
    attendance = ac_attendance();
    admin = person()
    student_name = student()
    recipient = person()
    config = ac_config()

    def sender(self, recipient, student_name):
        print("TODO")

    def get_attendance(self):
        attendance.get_listOfStudents

    def get_admin(self):
        return self.admin

    def get_email_body(self):
        return self.config.get_class_descrip()
