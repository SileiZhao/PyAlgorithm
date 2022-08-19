class Solution(object):
    """
    Given a array, and a target find two numbers that can add up to the target.
    """
    def twoSum(self, nums, target):
        """
        :param nums: a array with numbers
        :param target: the target
        :return: a list of index of two numbers
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        if left >= right:
            return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    nums = [2, 4, 6, 9]
    target = 10
    print(s.twoSum(nums, target))