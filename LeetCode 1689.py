class Solution:
    def minPartitions(self, n: str) -> int:
        for l in "9876543210":
            if l in n:
                return int(l)
# Other approach

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        b = []
        for i in range(n):
            b.append(nums[i])
            b.append(nums[i + n])
        return b
