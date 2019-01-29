# Question
# Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm:
# 1) Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a)
# 2) Capitalize every vowel in this new string (a, e, i, o, u)

# My Solution

def LetterChanges(string): 
    '''Alpha swap to i + 1 and upper vowels'''
    Vowels = ['a','e','i','o','u']
    Alpha = 'abcdefghijklmnopqrstuvwxyz'
	
    modified_str = []
    for char in list(string):
        if char.isalpha(): 
			
			if Alpha.find(char.lower()) == len(Alpha) - 1:
				index = 0
			else:
				index = Alpha.find(char.lower())
			
			if Alpha[index+1] in Vowels:
				modified_str.append(Alpha[index+1].upper())
			else:
				modified_str.append(Alpha[index+1])
        else:
		    modified_str.append(char)

    return ''.join(modified_str)
