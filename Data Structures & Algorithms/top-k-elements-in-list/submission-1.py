class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # iterate through the list, if you see a different number thats not in the dictionary, add a counter
        # later see what is the highest count for the number
        # return the first k of them

        counts = {}

        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] = counts[nums[i]] + 1
            else:
                counts[nums[i]] = 1
        
        return sorted(counts, key=counts.get, reverse=True)[:k]
         
