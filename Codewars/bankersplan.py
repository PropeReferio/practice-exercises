# Useful Kata from codewars, Banker's Plan. 
# The idea is a plan detailing how much a retiree can withdraw per year
# Such that they still have zero or more dollars after n years.
# f0 = initial bank balance.
# p = interest on bank banlance
# wd = withdrawal possible to take for n years without exhausting bank balance.
# i = inflation, multiply wd by i to maintain standard of living.

def fortune(f0, p, wd, n, i):
    from math import trunc
    lst = []
    for year in range(1,n):
        f0 = trunc(f0 * (1+p/100))
        f0 -= wd
        wd = trunc(wd * (1+i/100))
    return f0 >= 0