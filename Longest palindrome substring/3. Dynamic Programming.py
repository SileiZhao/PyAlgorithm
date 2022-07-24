class Solution(object):

    def longestPalindrome(self, s):
        """
        :param s: the input string
        :return: the longest palindrome substring
        """

        if not s:
            return ""

        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(n):
            is_palindrome[i][i - 1] = True

        start, longest = 0, 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                is_palindrome[i][j] = (is_palindrome[i + 1][j - 1] and s[i] == s[j])
                if is_palindrome[i][j] and length > longest:
                    start, longest = i, length

        return s[start:start + longest]


if __name__ == '__main__':
    s = Solution()
    string = 'xabcbac'
    print(s.longestPalindrome(string))