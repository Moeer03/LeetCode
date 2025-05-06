class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        b = []
        for i in range(n):
            b.append(nums[i])
            b.append(nums[i + n])
        return b
