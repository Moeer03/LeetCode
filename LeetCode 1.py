class Solution:
    def countMaxOrSubsets(self, nums):
        self.max_or = 0
        self.count = 0

        def backtrack(i, curr_or):
            if i == len(nums):
                if curr_or > self.max_or:
                    self.max_or = curr_or
                    self.count = 1
                elif curr_or == self.max_or:
                    self.count += 1
                return
            # Include nums[i]
            backtrack(i + 1, curr_or | nums[i])
            # Exclude nums[i]
            backtrack(i + 1, curr_or)

        backtrack(0, 0)
        return self.count
''