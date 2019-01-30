# 124 ms, faster than 67.05% of Python3 online submissions

# Can be improved

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman = {'I':1,
                'V':5,
                 'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000}
        
        Integer = 0
        for i,char in zip(range(len(s)-1), s):
            if char == 'I' and s[i+1] in ['V', 'X']:
                Integer -= Roman[char]
            elif char == 'X' and s[i+1] in ['L', 'C']:
                Integer -= Roman[char]
            elif char == 'C' and s[i+1] in ['D', 'M']:
                Integer -= Roman[char]
            else:
                Integer += Roman[char]
        
        Integer += Roman[s[-1]]
        
        return Integer
