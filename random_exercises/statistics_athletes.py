#From kata: Statistics for an Athletic Association

def seconds_to_results(secs):
    h = secs // 3600 #This takes the total number of seconds and gives them hour and minute
                     #values. Make this into a function, and use it in a for loop
    m = (secs - 3600 * h) // 60
    s = secs - 3600 * h - 60 * m
    return "|".join(["0" + str(h) if len(str(h)) < 2 else str(h), #Each of these add
    "0" + str(m) if len(str(m)) < 2 else str(m), #a zero if value is single digit
    "0" + str(s) if len(str(s)) < 2 else str(s)])

def stat(strg):
    if not strg: return ''
    n = []
    totalsecs = []
    for x in strg.split(","): #Turns string into a list of lists
        n.append(x.split("|"))
    for runner in n: #Converts said lists into seconds
        totalsecs.append(int(runner[0]) * 3600 + int(runner[1]) * 60 + int(runner[2]))
    
    from statistics import median
    median =  int(median(totalsecs))
    range = max(totalsecs) - min(totalsecs)
    mean = int(sum(totalsecs)/len(totalsecs)) #This needs to be truncated, per the instructions
    return ("Range: " + seconds_to_results(range) + 
    " Average: " + seconds_to_results(mean) + 
    " Median: " + seconds_to_results(median))


