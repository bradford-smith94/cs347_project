# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck test_people.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
from person import person
from student import student
from admin import admin

#class to test the person class and its descendents
#   check to make sure that descendent classes implement inheritance correctly
def main():
    student1 = student("John Smith", "jsmith@not-a-domain.tld")
    student2 = student("Name Surname Suffix", "name@host.com", False)
    admin1 = admin("Joe Admin", "it@ti.com")
    admin2 = admin("root", "root@localhost", False)
    placeholder = person("", "")

    print("Testing get name from student")
    print(student1.get_name())
    print(student2.get_name())
    print("Testing get name from admin")
    print(admin1.get_name())
    print(admin2.get_name())
    print("Testing get name from person")
    placeholder = student1
    print(placeholder.get_name())
    placeholder = student2
    print(placeholder.get_name())
    placeholder = admin1
    print(placeholder.get_name())
    placeholder = admin2
    print(placeholder.get_name())

    print("")
    print("Testing get email from student")
    print(student1.get_email())
    print(student2.get_email())
    print("Testing get email from admin")
    print(admin1.get_email())
    print(admin2.get_email())
    print("Testing get email from person")
    placeholder = student1
    print(placeholder.get_email())
    placeholder = student2
    print(placeholder.get_email())
    placeholder = admin1
    print(placeholder.get_email())
    placeholder = admin2
    print(placeholder.get_email())

    print("")
    print("Testing get attendance from student")
    print(student1.get_attendance())
    print(student2.get_attendance())

    print("")
    print("Testing get request from admin")
    print(admin1.get_admin_request())
    print(admin2.get_admin_request())

main()
