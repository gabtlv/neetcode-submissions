class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        for num, count in freq.items():
            buckets[count].append(num)

        result = []
        for count in range(n,0,-1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result
        