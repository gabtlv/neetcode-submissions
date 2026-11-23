class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # sort the string
        # if the sorted string is in the dictionary put it under the sublist 
        # else you put it in there as a sublist

        groups = {}

        for i in range(len(strs)):
            key = "".join(sorted(strs[i])) # sorts the string, then joins it

            if key not in groups:
                groups[key] = [] # if the key isn't in groups make an empty bucket
            
            groups[key].append(strs[i]) # put original word in the bucket

        return list(groups.values())