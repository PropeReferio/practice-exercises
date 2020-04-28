cache = {}
def nth_term_fib(n):
    if type(n) != int:
        raise TypeError('n must be a positive integer.')
    elif n < 1:
        raise ValueError('n must be a positive integer.')
    if n in cache:
        return cache[n] #This way, instead of recomputing function calls
        #We've already made, we check if we've done it already and return
        #that value if so.
    elif n == 1:
        value = 1
    elif n == 2:
        value = 1   #Time complexity is O(2^n), because you recursively call the
        #same function twice every time you call it once.
    elif n > 2:
        value = nth_term_fib(n-2) + nth_term_fib(n-1)
    cache[n] = value
    return value



print(nth_term_fib(1.1))
# for n in range(1,100):
#     print(nth_term_fib(n)) #
