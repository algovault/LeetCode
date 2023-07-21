import math

class Solution:
    @classmethod
    def mySqrt(self, x):
        self.x = x
        if (math.sqrt(x) != int):
             math.trunc(math.sqrt(x))
             print(math.trunc(math.sqrt(x)))
        

        

x = 8
Test = Solution
Test.mySqrt(x)