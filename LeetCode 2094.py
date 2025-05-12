from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        result = []

        for num in range(100, 1000):
            if num % 2 != 0:
                continue

            hundreds = num // 100
            tens = (num // 10) % 10
            units = num % 10

            num_counter = Counter([hundreds, tens, units])

            # Check if we can construct this number with the digits we have
            if all(count[d] >= num_counter[d] for d in num_counter):
                result.append(num)

        return result
