class Solution:
    def kidsWithCandies(self, c: List[int], e: int) -> List[bool]:
        a = max(c)
        b = len(c)
        r = [False] * b
        for i in range(b):
            if (c[i] + e) >= a:
                r[i] = True
        return r
