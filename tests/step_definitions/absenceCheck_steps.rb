# Bradford Smith and David Ott
# CS 347 Project
# AbsenceCheck absenceCheck_steps.rb
# "I pledge my honor that I have abided by the Stevens Honor System."
######################################################################
Given(/^the input "(.*?)"$/) do |arg1|
	@input = arg1
end

#steps for Absent.feature
When(/^the attendance is taken$/) do
	@output = `ruby tests/step_definitions/attendance.rb #{@input}`
end

#steps for Notify.feature
When(/^the notifications are sent$/) do
	@output = `ruby tests/step_definitions/notify.rb #{@input}`
end

#steps for Stat.feature
When(/^the stats are calculated$/) do
	@output = `ruby tests/step_definitions/stats.rb #{@input}`
end

Then(/^the output should be "(.*?)"$/) do |arg1|
	raise('Error') unless @output == arg1
end
