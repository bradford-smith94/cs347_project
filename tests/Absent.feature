#David Ott and Bradford Smith
#Absent.feature
#3/8/15
##############################
Feature: Absent
	
	Some scenarios to test the program's ability to mark students absent

	Scenario Outline:
		Given the input "<name> <here?>"
		When the program is run
		Then the output should be "<status>"
	
	Examples:
		| name	| here?	| status	|
		| Bob	| y		| present	|
		| Steve | y		| present	|
		| Bob	| n		| absent	|
		| Steve	| n		| absent	|
		| Mike	| y		| present	|
		| Tom	| n		| absent	|
