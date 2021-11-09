# 原始算法
class Solution(object):
    def SelectionSort(self, array: [int]) -> [int]:
        for i in range(0, len(array) - 1):
            min_index = i
            # 内层每次循环的目的是找出最小下标值，而不是交换
            for j in range(i + 1, len(array)):
                min_index = j if array[j] < array[min_index] else min_index
            array[i], array[min_index] = array[min_index], array[i]
        return array


if __name__ == '__main__':
    arr = [2, 1, 4, 6, 9, 0, 8, 5, 3, 7]
    solution = Solution()
    print(solution.SelectionSort(arr))
