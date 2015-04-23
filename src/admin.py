# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck admin.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################

class admin(person):
    wants_info = true #assume an administrator wants info to be sent through ac-notify

    def send_admin(request):
        if(request):
            wants_info = true
        else:
            wants_info = false

    def get_admin_request():
        return self.wants_info
