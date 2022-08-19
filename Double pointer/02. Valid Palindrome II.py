class Solution(object):

    def findDifference(self, string, left, right):
        while left < right and string[left] == string[right]:
            left += 1
            right -= 1
        return left, right

    def isParindrome(self, string, left, right):
        left, right = self.findDifference(string, left, right)
        return left >= right

    def ValidParindrome(self, string):
        if string is None:
            return False
        if len(string) == 0 or len(string) == 1:
            return True

        left = 0
        right = len(string) - 1

        left, right = self.findDifference(string, left, right)
        if left >= right:
            return True

        return self.isParindrome(string, left + 1, right) or self.isParindrome(string, left, right - 1)
