class Solution:
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        leftSide = nums[:mid]
        rightSide = nums[mid:]
        sortedLeft = self.mergeSort(leftSide)
        sortedRight = self.mergeSort(rightSide)
        return self.merge(sortedLeft, sortedRight)
    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

sol = Solution()
unsortedArr = [7,4,1,5,3]
sortedArr = sol.mergeSort(unsortedArr)
print(sortedArr)