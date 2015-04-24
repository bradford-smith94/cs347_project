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

    #desired output is commented next to each print statement
    print("Testing get name from student")
    print(student1.get_name()) #John Smith
    print(student2.get_name()) #Name Surname Suffix
    print("Testing get name from admin")
    print(admin1.get_name()) #Joe Admin
    print(admin2.get_name()) #root
    print("Testing get name from person")
    placeholder = student1 #John Smith
    print(placeholder.get_name())
    placeholder = student2 #Name Surname Suffix
    print(placeholder.get_name())
    placeholder = admin1 #Joe Admin
    print(placeholder.get_name())
    placeholder = admin2 #root
    print(placeholder.get_name())

    print("")
    print("Testing get email from student")
    print(student1.get_email()) #jsmith@not-a-domain.tld
    print(student2.get_email()) #name@host.com
    print("Testing get email from admin")
    print(admin1.get_email()) #it@ti.com
    print(admin2.get_email()) #root@localhost
    print("Testing get email from person")
    placeholder = student1
    print(placeholder.get_email()) #jsmith@not-a-domain.tld
    placeholder = student2
    print(placeholder.get_email()) #name@host.com
    placeholder = admin1
    print(placeholder.get_email()) #it@ti.com
    placeholder = admin2
    print(placeholder.get_email()) #root@localhost

    print("")
    print("Testing get attendance from student")
    print(student1.get_attendance()) #True
    print(student2.get_attendance()) #False

    print("")
    print("Testing get request from admin")
    print(admin1.get_admin_request()) #True
    print(admin2.get_admin_request()) #False

main()
