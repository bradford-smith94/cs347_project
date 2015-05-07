CS 347: Software Development Processes
Group: Bradford Smith and David Ott

AbsenceCheck
############

Project Structure
src/
	-contains all the source code
	-contains unit tests for Assignment 3: first iteration
		-cd into src and run test_*.py files and look for desired output
            -e.g. $`<python> test_people.py`
            (where $ is your prompt and the command is surrounded in `)
            (and where <python> is the command to run python2 (this may differ
            from one machine to another))
			-desired output is provided in comments in the test_*.py files
	-to run the program cd into src and run main.py
		($`<python> main.py` where python is the command to run python2)
		-right now the program is hardcoded to get class role from class.csv and output cumulative attendance to cumulative.csv
			-class.csv is in this format: Student_First_Name,Student_Last_Name,Student_Email
			-cumulative.csv is in this format: Student_Name,Student_Email,Number_of_Absences
		-program also can only send from a gmail address (teacher email and password must be of an actual gmail address to send mail)
doc/
	-contains documentation files
	-contains uml diagrams
tests/
	-contains acceptance testing code
	-cucumber features
	-to run cucumber features: stay here in the project root
		-e.g. $`cucumber tests/Absent.feature`
		(where $ is your prompt and the command is surrounded in `)
		(this assumes that `python` will run python2 on your system)
