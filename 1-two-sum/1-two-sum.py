class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. use enumerate to assign original index to each number
        for i, n in enumerate(nums):
            # check if target - number is in the list.
            k = target - n
            if k in nums[i + 1:]:
                return [i, nums[i + 1:].index(k) + i + 1]