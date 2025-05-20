class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def is_palindromic(s):
            return s == s[::-1]

        for base in range(2, n - 1):
            representation = ""
            temp = n
            while temp > 0:
                representation = str(temp % base) + representation
                temp //= base
            if not is_palindromic(representation):
                return False
        return True
# Optimal Solution
# The problem is asking if there exists a base b such that the number n is palindromic in that base.
# The answer is always false for n > 3 because:
# 1. For n = 4, the only base is 2, and the representation is 100.
# 2. For n = 5, the only base is 3, and the representation is 12.
# 3. For n = 6, the only base is 4, and the representation is 12.

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False