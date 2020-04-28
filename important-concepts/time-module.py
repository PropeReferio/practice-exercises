import time

start = time.time() # Number of seconds since the beginning of modern computers
print(time.asctime()) #Normal recognizable time
now = time.gmtime() # object that you can pull hours, weeks, etc from

print(f"It is the year {now[0]} and it is the {now[1]}nd month.")
time.sleep(10)
# You can also convert gmtime back to asctime format
print(time.asctime(now))

stop = time.time()

print(stop - start) # Measures how long code takes to run
