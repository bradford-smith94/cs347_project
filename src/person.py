# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck person.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################

#person
#this class provides the structure of a person with a name and an email
class person(object):
    #constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email

    #pre:none
    #post:returns the name variable
    def get_name():
        return self.name

    #pre:none
    #post:returns the email variable
    def get_email():
        return self.email
