class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = []
        prev = 0

        for i in pref:
            arr.append(prev ^ i)
            prev = i
        
        return arr