# find the kth largest number in an array

class Solution(object):

    def findKthLargest(self, nums, k):
        """
        find the Kth largest element in the array
        :param nums: the array
        :param k: the kth
        :return: number
        """
        if nums is None or k < 1 or k > len(nums):
            return None
        return self.QuickSelect(nums, 0, len(nums) - 1, k)


    def QuickSelect(self, nums, start, end, k):
        """
        :param nums: the array
        :param start: the left pointer
        :param end:  the right pointer
        :param k:  the kth
        :return:  the numbers in the nums
        """
        if start == end:
            return nums[start]
        pivot = self.partition(nums, start, end)
        if pivot + 1 == k:
            return nums[pivot]
        elif pivot + 1 < k:
            return self.QuickSelect(nums, pivot + 1, end, k)
        else:
            return self.QuickSelect(nums, start, pivot - 1, k)


    def partition(self, nums, start, end):
        """
        :param nums: the array
        :param start: the left pointer
        :param end: the right pointer
        :return: the pivot
        """
        pivot = end
        left = start
        right = end - 1
        while left <= right:
            while left <= right and nums[left] > nums[pivot]:
                left += 1
            while left <= right and nums[right] <= nums[pivot]:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        nums[left], nums[pivot] = nums[pivot], nums[left]
        return left


if __name__ == '__main__':
    s = Solution()
    nums = [2, 4, 3, 9, 1, 0, 12, 6, 8, 7, 5]
    k = len(nums)
    print(s.findKthLargest(nums, k))