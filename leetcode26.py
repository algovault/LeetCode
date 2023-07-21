from typing import List

class Solution:
    @classmethod
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        y = len(nums)
        for x in range(len(nums)):
             print(x)
             if (nums[0] == nums[1]):
               nums.remove(nums[0])
             elif(nums != nums[1]):
              nums.append(nums[0])
              nums.remove(nums[0])
              print(nums)
              k = x-len(nums)    
        for x in range(k):
           nums.append(0)
           print(nums)
           z = ", nums = "
           print(k, z.lstrip(" "), nums)
           

Test = Solution
nums = [0,0,1,1,1,3,3,3,3,4,4,5,6,19]
Test.removeDuplicates(nums)