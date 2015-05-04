#David Ott and Bradford Smith
#Stat.feature
#3/8/15
##############################
Feature: Stat

	Some scenarios to test the program's ability to calculate statistics
		(tallying the total number of a student's absences)

	Scenario Outline:
		Given the input "<name> <attendance> <total>"
		When the stats are calculated
		Then the output should be "<new-total>"

	Examples:
		| name	| attendance	| total	| new-total	|
		| Bob	| present		| 0		| 0			|
		| Steve	| present		| 1		| 1			|
		| Tom	| absent		| 2		| 3			|
		| Mike	| absent		| 0		| 1			|
		| Bill	| present		| 10	| 10		|
