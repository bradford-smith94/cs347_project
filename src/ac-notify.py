# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck ac-notify.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
#import email handling classes
import smtplib
from email.mime.text import MIMEText
#import person class
from person import person

#ac_notify
#this class is used to send the config file to absent students
class ac_notify:

    #pre:takes in a teacher sender, student recipient, and student_name?
    #post:sends an email, to recipient from sender
    def send(self, sender, recipient, student_name):
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(sender.get_email(), sender.get_password())
        message = create_message(recipient)
        try:
            server.sendmail("email", recipient.get_email(), message.as_string)
        except:
            print("Message to %s did not send" %(recipient.get_name()))
        server.quit()

    def create_message(self, recipient):
        print("TODO")
