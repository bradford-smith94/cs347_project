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

    #pre:takes in an ac_config config and student recipient
    #post:sends an email, to recipient from config.get_teacher
    def send(self, config, recipient):
        sender = config.get_teacher()
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(sender.get_email(), sender.get_password())
        message = create_message(recipient, config)
        try:
            server.sendmail("email", recipient.get_email(), message.as_string)
        except:
            print("Message to %s did not send" %(recipient.get_name()))
        server.quit()

    #pre:takes in a student recipient and an ac_config config
    #post:creates and returns a MIMEText email message
    def create_message(self, recipient, config):
        greet = MIMEText("Dear %s \nHere is what you missed in class:\n" %(recipient.get_name()))
        body = MIMEText(config.get_class_descrip())
        msg = greet + body
        msg["Subject"] = "Missed Class"
        msg["From"] = config.get_teacher().get_email()
        msg["To"] = recipient.get_email()
        return msg
