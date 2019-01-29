# Question
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters
# Ex:
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# ---------------------------
# My Solution (32 ms, faster than 100.00% of Python3)

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        Given string of digits (2-9), return all possible letter combinations
        """
        PhoneKeys = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y', 'z'],
        }
        if not digits:
            return []
        Letters = []
        for i in digits:
            Letters.append(PhoneKeys[i])
        
        combinations = list(itertools.product(*Letters))
        return [''.join(subset) for subset in combinations]
