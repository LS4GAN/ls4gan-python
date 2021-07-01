def some_complicated_thing(n):
    '''
    An internal implementation function.

    This is just to provide something separate from our "api" function
    fib() below.
    '''
    if n <= 0: return 0
    if n == 1: return 1
    return n+some_complicated_thing(n-1)


def fib(n):
    '''
    Return the n'th Fibonacci number
    '''
    return some_complicated_thing(n)
