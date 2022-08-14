class Solution(object):

    def kmp(self, mom_string, son_string):
        # a mom_string and a son_string are given
        # return the index of the first occurrence of the son_string in the mom_string
        # if there is no son_string in the mom_string, return -1
        test = ''
        if type(mom_string) != type(test) or type(son_string) != type(test):
            return -1
        if len(son_string) == 0:
            return 0
        if len(mom_string) == 0:
            return -1
        # solve the next array
        next = [-1] * len(son_string)
        if len(son_string) > 1:  # 'if' is to prevent the error of index out of range
            next[1] = 0
            i, j = 1, 0
            while i < len(son_string) - 1:  # -1 for preventing the error of index out of range
                if j == -1 or son_string[i] == son_string[j]:
                    i += 1
                    j += 1
                    next[i] = j
                else:
                    j = next[j]

        # kmp flame
        m = s = 0  # initialize the index of mom_string and son_string and equal to 0
        while s < len(son_string) and m < len(mom_string):
            # success to find the son_string or quit because of the end of mom_string
            if s == -1 or mom_string[m] == son_string[s]:
                m += 1
                s += 1
            else:
                s = next[s]

        if s == len(son_string):  # success
            return m - s
        # fail
        return -1


if __name__ == '__main__':
    s = Solution()
    mom = 'abcdefg'
    son = 'bcd'
    print(s.kmp(mom, son))