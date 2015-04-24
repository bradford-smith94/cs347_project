# Bradford Smith and David Ott
# CS 347 Assignment 3
# AbsenceCheck test_parse_file.py
# "I pledge my honor that I have abided by the Stevens Honor System."
#####################################################################
#imort ac_attendance class
from ac_attendance import ac_attendance

#class to test that the ac_attendance class will correctly parse a csv file
def main():
    attendance = ac_attendance()

    attendance.parse_file('test.csv')
    for s in attendance.get_listOfStudents():
        print("##Name: %s \t##Email: %s" %(s.get_name(), s.get_email()))

main()
