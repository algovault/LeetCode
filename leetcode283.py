class Solution:
    @classmethod
    def moveZeroes(self, nums):
        self.nums = nums
        i = 0
        for i in range(nums.count(0)):
            if 0 in nums:
                nums.append(0)
                nums.remove(0)
                


nums = [0,1,0,3,12]
Test = Solution
Test.moveZeroes(nums)
print(nums)