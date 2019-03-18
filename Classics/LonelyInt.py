# Clara Eleonore Pavillet

def PairingCheck(numbs):
    for integer in numbs:
        if numbs.count(integer) == 1:
            print(integer)
    
numbs = input()
numbs = numbs.split(', ')
numbs = list(map(int, numbs))
PairingCheck(numbs)

def PairingCheck(numbs):
     '''Optimized solution using bitwise operation XOR - to get O(1) space and O(n) time complexity'''
