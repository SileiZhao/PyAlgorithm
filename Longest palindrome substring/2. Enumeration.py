# Enumerate the middle of the string and check if it is a palindrome.
# For a string of length n and n is an odd, there are n middles.
# For a string of length n and n is an even, there are n-1 middles.

class Solution(object):

    def longestPalidrome(self, s):
        """
        :param s: input string
        :return: the longest palindrome substring
        """
        if s is None:
            return None

        answer = (0, 0)
        for mid in range(len(s)):
            answer = max(answer, self.get_palidrome_from(s, mid, mid))
            answer = max(answer, self.get_palidrome_from(s, mid, mid + 1))

        return s[answer[1]: answer[0] + answer[1]]

    def get_palidrome_from(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1, left + 1


if __name__ == '__main__':
    s = Solution()
    string = 'xabcbac'
    print(s.longestPalidrome(string))