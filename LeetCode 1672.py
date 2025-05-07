class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        c = 0
        for i in accounts:
            if sum(i) > c:
                c = sum(i)
        return c
