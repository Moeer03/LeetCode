class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        c = 0
        for i in range(1 , n + 1):
            if i % m == 0:
                c -= i
            else:
                c += i
        return c
