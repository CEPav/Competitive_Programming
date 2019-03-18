# Clara Eleonore Pavillet
def FizzBuzz(n):
    for integer in range(1,n+1):
        if integer % 3 == 0 and integer % 5 != 0:
            print('Fizz')
        elif integer % 5 == 0 and integer % 3 != 0:
            print('Buzz')
        elif integer % 3 == 0 and integer % 5 == 0:
                print('FizzBuzz')
        else:
            print(integer)

n = input()
FizzBuzz(int(n))
