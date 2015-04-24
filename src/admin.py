# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck admin.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
#import person class
from person import person

#admin
#this class provides the structure of an admin
#   admin is a person with a boolean for requesting stats
class admin(person):

    #constructor
    def __init__(self, name, email, request=True):
        person.__init__(self, name, email)
        self.wants_info = request #assume an administrator wants info to be sent through ac-notify

    #pre:takes in a boolean request (True = admin wants stats, False = admin doesn't want stats)
    #post:updates the wants_info variable with request
    def send_admin(self, request):
        if(request):
            wants_info = True
        else:
            wants_info = False

    #pre:none
    #post:returns the wants_info variable
    def get_admin_request(self):
        return self.wants_info
