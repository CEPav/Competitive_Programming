def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

n = input()
answer = factorial(int(n))
print(answer)
