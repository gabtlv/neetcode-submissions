class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # use a dict to map the key value pair
        # for each number find the complement
        # if the complement is already in the dictionary
        # return [index, current index]

        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i
