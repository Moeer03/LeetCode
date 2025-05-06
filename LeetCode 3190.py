class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = 0
        for i in nums:
            if i % 3 != 0:
                counter += 1
        return counter


        # in case we got a no. where we cannot do it by just by increment or decrement 1, it is only possible in case of a no. greater than 3
        # So Follow below solution, but in case of only divisible by 3 above method is good
        r = []
        for i in range(len(nums)):
            a = nums[i]
            b = nums[i]
            c = 0
            d = 0
            while a % 3 != 0:
                a += 1
                c += 1
            while b % 3 != 0:
                b -= 1
                d += 1
            if c < d:
                r.append(c)
            else:
                r.append(d)
        s = 0
        for i in r:
            s += i
        return s
