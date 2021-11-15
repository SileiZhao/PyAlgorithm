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
    def SelectionSort_1(self, array: [int]) -> [int]:
        n = len(array)
        for i in range(n):
            min_index = i
            max_index = n - 1
            n = n - 1
            for j in range(i+1, n+1):
                if array[j] < array[min_index]:
                    min_index = j
                if array[j] > array[max_index]:
                    max_index = j
            array[min_index], array[i] = array[i], array[min_index]  # 将最小的放到本轮的最前面
            array[max_index], array[n] = array[n], array[max_index]  # 将最大的放到本轮的最前面


if __name__ == '__main__':
    arr = [2, 1, 4, 6, 9, 0, 8, 5, 3, 7]
    solution = Solution()
    print(solution.SelectionSort(arr))
