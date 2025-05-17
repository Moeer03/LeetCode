class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # implemented timsort using python code, used in python standard library
        '''🥇 Timsort (used by Python's built-in list.sort() and sorted())
        In-place: ✅ (partially)

        Stable: ✅

        Time Complexity:

        Best: O(n)

        Average: O(n log n)

        Worst: O(n log n)

        Space Complexity: O(n) (not purely in-place, but optimized)'''
        ''' MIN_RUN = 32 is a tuning parameter used in CPython's actual Timsort.

        The algorithm uses insertion sort for small chunks and merge sort for combining.

        This version is simplified and may not perform as well as the C implementation in CPython but works well for educational understanding.'''
        MIN_RUN = 32

        def insertion_sort(arr, left, right):
            for i in range(left + 1, right + 1):
                key = arr[i]
                j = i - 1
                while j >= left and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

        def merge(arr, l, m, r):
            left = arr[l:m+1]
            right = arr[m+1:r+1]

            i = j = 0
            k = l

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        def timsort(arr):
            n = len(arr)

            # Step 1: Sort individual subarrays of size MIN_RUN using insertion sort
            for start in range(0, n, MIN_RUN):
                end = min(start + MIN_RUN - 1, n - 1)
                insertion_sort(arr, start, end)

            # Step 2: Start merging from size MIN_RUN
            size = MIN_RUN
            while size < n:
                for left in range(0, n, 2 * size):
                    mid = min(n - 1, left + size - 1)
                    right = min((left + 2 * size - 1), n - 1)

                    if mid < right:
                        merge(arr, left, mid, right)

                size *= 2
        timsort(nums)
