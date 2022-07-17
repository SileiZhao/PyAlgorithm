class Solution(object):

    def longestPalidrome(self, s):
        """
        :param s: input string
        :return: the longest palindrome substring
        """
        if s is None:
            return None

        for length in range(len(s), 0, -1):
            for i in range(len(s) - length + 1):
                if self.isPalindrome(s, i, i + length - 1):
                    return s[i:i + length]

        return ""

    def isPalindrome(self, s, left, right):
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1

        return left >= right


if __name__ == '__main__':
    s = Solution()
    string = 'xabcbac'
    print(s.longestPalidrome(string))
