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

# Clean user input if given in multiple lines
# Input received as one string 'integer' per line
input_n = input()
while(len(input_n)>0):
    input_n = int(input_n)
    ans = Fibonacci_DP(input_n)
    print(ans)
    input_n = input()


# list(map(int, input().split()))
