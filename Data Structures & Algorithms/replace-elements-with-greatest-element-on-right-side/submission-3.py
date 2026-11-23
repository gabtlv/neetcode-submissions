class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last = len(arr) - 1
        maxsofar = arr[last]

        arr[last] = -1

        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = maxsofar
            if temp > maxsofar:
                maxsofar = temp
        
        return arr

