# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck test_people.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
from student import student

def main():
    student1 = student("John Smith", "jsmith@not-a-domain.tld")
    student2 = student("Name Surname Suffix", "name@host.com", False)

    print("Testing get name from person")
    print(student1.get_name())
    print(student2.get_name())

    print("")
    print("Testing get email from person")
    print(student1.get_email())
    print(student2.get_email())

    print("")
    print("Testing get attendance from student")
    print(student1.get_attendance())
    print(student2.get_attendance())

main()
