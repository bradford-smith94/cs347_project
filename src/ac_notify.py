# Bradford Smith and David Ott
# CS 347 Project
# AbsenceCheck ac_notify.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
#import email handling classes
import smtplib
from email.mime.text import MIMEText
import csv
#import person class
from person import person
from student import student
from admin import admin

#ac_notify
#this class is used to send the config file to absent students
class ac_notify:

    #pre:takes in a (student or admin) recipient and an ac_config config
    #   optionally takes in a csv file (required to send to admin)
    #post:creates and returns a MIMEText email message
    def create_message(self, recipient, config, statsFile=""):
        if isinstance(recipient, student) and statsFile == "":
            #send to student
            greet = ("Dear %s, \nHere is what you missed in class:\n\n" %(recipient.get_name()))
            body = (config.get_class_descrip())
            end = ("\nFrom %s" %(config.get_teacher().get_name()))
            msg = MIMEText(greet + body + end)
            msg["Subject"] = "Missed Class"
        elif isinstance(recipient, admin):
            #send to admin
            greet = ("Dear %s \nHere are the class total absences:\n\n" %(recipient.get_name()))
            body = ("Student Name |\tStudent Email |\tTotal Absences |\n")
            body += "=" * 45
            body += "\n"
            with open(statsFile, 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for line in reader:
                    body += str(line[0])
                    body += " |\t"
                    body += str(line[1])
                    body += " |\t"
                    body += str(line[2])
                    body += " |\n"
                csvfile.close()
            end = ("\nFrom %s" %(config.get_teacher().get_name()))
            msg = MIMEText(greet + body + end)
            msg["Subject"] = "Class Cumulative Absences"
        else:
            print("ERROR: recipient is of wrong type or csv file was not given")
            return
        msg["From"] = config.get_teacher().get_email()
        msg["To"] = recipient.get_email()
        return msg


    #pre:takes in an ac_config config and (either student or admin) recipient
    #   optionally takes in a csv file (required to send to admin)
    #post:sends an email, to recipient from config.get_teacher
    def send(self, config, recipient, csv=""):
        sender = config.get_teacher()
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(sender.get_email(), sender.get_password())
        if isinstance(recipient, student):
            message = self.create_message(recipient, config)
        elif isinstance(recipient, admin) and not csv == "":
            message = self.create_message(recipient, config, csv)
        else:
            print("ERROR: recipient is of wrong type or csv file was not given")
            return
        try:
            server.sendmail(str(sender.get_email()), str(recipient.get_email()), message.as_string())
        except:
            print("Message to %s did not send" %(recipient.get_name()))
        server.quit()
