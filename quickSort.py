class Solution:
    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low - 1

        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1
    def quickSort(self, nums, low, high):
        if high is None:
            high = len(nums) - 1
        if low < high:
            storedVal = self.partition(nums, low, high)
            self.quickSort(nums, low, storedVal - 1)
            self.quickSort(nums, storedVal + 1, high)


sol = Solution()
val = [3, 5, 2, 8, 1, 9]
sortedVal = sol.quickSort(val, 0, None)
print("Quick Sort: ", val)