import time
import calendar
localtime = time.asctime(time.localtime(time.time()))
print "Local current time :", localtime
cal = calendar.month(2018, 1)
print "Here is the calendar:"
print cal