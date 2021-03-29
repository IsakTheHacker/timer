import datetime
import time

hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

start = datetime.datetime.now()

time.sleep(hours * 3600 + minutes * 60 + seconds)

end = datetime.datetime.now()

elapsed = end - start

print(elapsed)