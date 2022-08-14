class Solution(object):

    def Rabin_Karp(self, source, target):

        if source is None or target is None:
            return -1

        m = len(target)
        if m == 0:
            return 0

        BASE = 1000000
        # 31 ^ m
        power = pow(31, m) % BASE

        target_hash = 0
        for i in range(len(target)):
            target_hash = (target_hash * 31 + ord(target[i])) % BASE

        source_hash = 0
        for j in range(len(source)):
            # abc + d
            source_hash = (source_hash * 31 + ord(source[j])) % BASE
            if j < m - 1:
                continue
            if j >= m:
                # abcd - a
                source_hash = (source_hash - power * ord(source[j - m])) % BASE
                if source_hash < 0:
                    source_hash += BASE
            # double check the string
            if source_hash == target_hash:
                if source[j - m + 1: j + 1] == target:
                    return j - m + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    source = 'abc defg'
    target = 'def'
    print(s.Rabin_Karp(source, target))