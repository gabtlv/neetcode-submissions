class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = set() # O(1) better time

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
        return False

        