class Solution(object):
    @staticmethod
    def RadixSort(arr: [int]):
        i = 0
        max_num = max(arr)
        # 取出最大数字的长度和位数
        j = len(str(max_num))
        while i < j:
        # 建桶
            bucketList = [[] for i in range(10)]
            #遍历 放数 每次循环完数组都是按位有序的
            for x in arr:
                bucketList[int(x/(10 ** i)) % 10].append(x)
            # 每次清空一次arr 放入新顺序的数组
            arr.clear()
            for bucket in bucketList:
                for y in bucket:
                    arr.append(y)
            i += 1
        return arr


if __name__ == '__main__':
    arr = [23, 123, 54, 233, 782, 3, 654, 300, 726, 912, 34]
    solution = Solution()
    print(solution.RadixSort(arr))