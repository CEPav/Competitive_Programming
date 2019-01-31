# Faster than 99.65%

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s= s.lower().replace(' ','')
        s = re.sub(r'\W+', '', s)
        
        return s == s[::-1]
