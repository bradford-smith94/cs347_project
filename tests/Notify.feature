#David Ott and Bradford Smith
#Notify.feature
#3/8/15
##############################
Feature: Notify

	Some scenarios to test that the program sends emails to absent students

	Scenario Outline:
		Given the input "<email> <attendance>"
		When the program is run
		Then the output should be "<send-email?>"

	Examples:
		| email				| attendance	| send-email?	|
		| bob@school.edu	| present		| n				|
		| steve@school.edu	| present		| n				|
		| tom@school.edu	| absent		| y				|
		| bill@school.edu	| absent		| y				|
		| mike@school.edu	| present		| n				|
