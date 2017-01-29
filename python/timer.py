from timeit import default_timer as timer
import time
import datetime

start_time = timer()
time.sleep(5)
end_time = timer()

print str(datetime.timedelta(seconds=(end_time - start_time)))