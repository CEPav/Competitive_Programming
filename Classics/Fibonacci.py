# Clara Eleonore Pavillet

def Fibonacci_Recursive(n):
'''O(2^n)'''
    if n <= 1:
        return n
    else:
        return (Fibonacci_Recursive(n-1)+Fibonacci_Recursive(n-2))

def Fibonacci_DP(n, cache={}):
'''O(n)'''
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = Fibonacci_DP(n-1)+Fibonacci_DP(n-2)
    return cache[n]
