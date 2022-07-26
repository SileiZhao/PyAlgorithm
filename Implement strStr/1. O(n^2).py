class Solution:

    def strStr(self, source, target):
        """
        :param source: the source string
        :param target: the target string
        :return: the index of the first occurrence of the target string in the source string
        """

        if source is None or target is None:
            return -1

        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i + j] != target[j]:
                    break
            else:
                return i

        return -1
