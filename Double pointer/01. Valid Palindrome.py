class Solution:

    def isPalindrome(self, string):
        """
        whether the string is a valid palindrome.
        :param string: input string
        :return: True if the string is a valid palindrome otherwise False.
        """
        if string is None:
            return False
        if len(string) == 0 or len(string) == 1:
            return True
        left = 0
        right = len(string) - 1

        while left < right:
            while left < right and not self.isValidChar(string[left]):
                left += 1
            while left < right and not self.isValidChar(string[right]):
                right -= 1
            if left < right and string[left].lower() != string[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def isValidChar(self, s):
        return s.isalpha() or s.isdigit()


if __name__ == '__main__':
    s = Solution()
    string = 'A man, a plan, a canal: Panama'
    print(s.isPalindrome(string))