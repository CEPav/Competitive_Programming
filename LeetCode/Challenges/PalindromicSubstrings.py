# First solution (not optimal)

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        Count = 0
        
        def palindrome_check(substring):
            return substring == substring[::-1]

        for i in range(len(s)):
            for j in range(i, len(s)):
                if palindrome_check(s[i:j+1]):
                    Count += 1
     
        return Count
