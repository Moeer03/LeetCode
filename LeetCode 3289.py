class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        set1 =set()
        ans =[]
        for num in nums:
            if num in set1:
                ans.append(num)
                if len(ans)==2:
                    break
            else:
                set1.add(num)
        return ans
