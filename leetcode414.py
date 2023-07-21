class Solution:
    @classmethod
    def thirdMax(self, nums):
        self.nums = nums
        x = max(nums)
        y = nums.count(x)
        z = 0
        if len(nums) >= 3:
            for z in range(2):
                for x in nums:
                    nums.remove(x)
        else:
            return max(nums)
        print(nums)


nums = [3,2,1]
Test = Solution
Test.thirdMax(nums)