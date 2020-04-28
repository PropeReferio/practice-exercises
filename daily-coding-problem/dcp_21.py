# Given an array of time intervals (start, end) for classroom lectures 
# (possibly overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

# Find latest time (max of max of tuples)
# Iterate through that range,
#  i. Add tuples/indices of tuples to a queue at their start time (tuple[0])
#      a. Update max_ocup to: max_ocup = max(max_ocup, len(queue)) each time a
#      class starts
#  ii. Pop them off the queue at their end time (tuple[1])

#Alternate to iterating through whole range:
#Two hashmaps, one for start, other for end. Times are keys, class index is value
#Iterate through a list of combined start and stop times. Either add or remove
# a class from the queue.
#Update max_ocup as above.
from collections import deque

schedule = [(30, 75), (0, 50), (60, 150), (40, 80), (49, 90), (51, 79)]

def space_needed(lst):
    start, stop, times, dq = {}, {}, [], deque([])
    max_ocup = 1
    for i in range(len(lst)):
        start[lst[i][0]] = i
        stop[lst[i][1]] = i
        times.extend([lst[i][0], lst[i][1]])
    for time in sorted(times):
        if time in start.keys():
            dq.appendleft(start[time])
            max_ocup = max(max_ocup, len(dq))
        if time in stop.keys():
            dq.remove(stop[time])
            # I use remove here to avoid the problem of the wrong course
            # being at the end of the deque. Pop wouldn't work in this case.
            #However, this code is problematic if two courses start and stop
            #at the same time. Oh wait... maybe not. Because first you would 
            #add a course, and update max_ocup... and then you'd remove the other
            #course. I'd have to ask the interviewer how such an overlap would be
            #counted... Could a class end and start in the same room simultaneously?
    return max_ocup
    

print(space_needed(schedule))
    