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
	@output = `cd src/ && python cucumber_attendance.py #{@input}`
    raise('Attendance failed') unless $?.success?
end

#steps for Notify.feature
When(/^the notifications are sent$/) do
	@output = `cd src/ && python cucumber_notify.py #{@input}`
    raise('Notify failed') unless $?.success?
end

#steps for Stat.feature
When(/^the stats are calculated$/) do
	@output = `cd src/ && python cucumber_stats.py #{@input}`
    raise('Stats failed') unless $?.success?
end

Then(/^the output should be "(.*?)"$/) do |arg1|
	raise("Error: Expected: #{arg1} Given: #{@output}") unless (@output == arg1)
end
