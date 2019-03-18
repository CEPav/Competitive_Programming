# Clara Eleonore Pavillet

def BalanceCheck(delimiters):
    characters = {'(':')', '[':']', '{':'}'}
    stack = []
    for char in delimiters:
        if char in characters.keys():
            stack.append(char)
        elif char in characters.values():
            if not stack: #If empty then we dont want to close so False
                return False
            elif characters[stack.pop()] != char: #We start 'poping' out in closed pairs
                return False
        else:
            return False #Any other character not valid
    return not stack #True if empty - thus all balanced

    
delimiters = str(input())
balance = BalanceCheck(delimiters)
print(balance)
