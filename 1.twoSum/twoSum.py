class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        n = len(nums)

        for i in range(n):
            num = nums[i]
            complement = target - num
            if complement in map:
                return [map[complement], i]
            map[num] = i
        
        return [] # No solution found
