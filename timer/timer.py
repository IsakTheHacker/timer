from datetime import datetime
import time

hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

start = datetime.now()
end2 = datetime(year = start.year, month = start.month, day = start.day, hour = int(start.hour) + hours, minute = int(start.minute) + minutes, second = int(start.second) + seconds)
print("Start: {}".format(start))
print("End: {}".format(end2))

for i in range (hours * 3600 + minutes * 60 + seconds):
	diff = (end2 - datetime.now())
	
	seconds = diff.seconds
	day = seconds // (24 * 3600)
	seconds = seconds % (24 * 3600)
	hour = seconds // 3600
	seconds %= 3600
	minutes = seconds // 60
	seconds %= 60
	aseconds = seconds

	print("{}:{}:{}".format(hour, minutes, aseconds))
	time.sleep(1)

end = datetime.now()

elapsed = end - start