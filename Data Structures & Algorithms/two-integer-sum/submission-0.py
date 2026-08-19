'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       nums= []
        for i, num in enumerate(nums):
            complement  = target-num

            if complement in nums:
                return (lst_1[complement], i)
           nums
           [num] = i
        return None'''

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return None
        