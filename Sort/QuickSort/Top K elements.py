# find the top k smallest elements in an array

class Solution(object):

    def findKElements(self, nums, k):
        """
        find the top k smallest elements in an array
        :param nums: a array with numbers
        :param k: the kth
        :return: a list of top k smallest elements
        """
        if nums is None or k < 1 or k > len(nums):
            return None
        return self.QuickSearch(nums, 0, len(nums) - 1, k - 1)


    def QuickSearch(self, nums, start, end, k):
        pivot = self.partition(nums, start, end)
        if pivot == k:
            return nums[:pivot + 1]
        elif pivot > k:
            return self.QuickSearch(nums, start, pivot - 1, k)
        else:
            return self.QuickSearch(nums, pivot + 1, end, k)


    def partition(self, nums, start, end):
        pivot = end
        left = start
        right = end - 1
        while left <= right:
            while left <= right and nums[left] < nums[pivot]:
                left += 1
            while left <= right and nums[right] >= nums[pivot]:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        nums[left], nums[pivot] = nums[pivot], nums[left]
        return left


if __name__ == '__main__':
    s = Solution()
    nums = [2, 4, 3, 9, 1, 0, 12, 6, 8, 7, 5]
    k = 2
    print(s.findKElements(nums, k))