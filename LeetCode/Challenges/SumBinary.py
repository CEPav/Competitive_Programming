#Faster than 95%

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2) #set string as integer base 2
        b = int(b,2)
        return (bin(a+b)[2:])
