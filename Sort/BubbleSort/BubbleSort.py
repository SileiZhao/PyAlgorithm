class Solution(object):
    def BubbleSort(self, array: [int]) -> [int]:
        # 这层循环实际上只控制次数，i 并不作为数组下标参与运算
        for i in range(0, len(array)):
            for j in range(0, len(array) - 1):
                if array[j] > array[j + 1]:
                    temp = array[j + 1]
                    array[j + 1] = array[j]
                    array[j] = temp
        return array

# 优化1：遍历数组没有元素发生位置交换时，结束排序,最好复杂度为O(n)

class optimizing(object):
    @staticmethod
    def BubbleSort(arr: [int]) -> [int]:
        # 这层循环实际上只控制次数，i 并不作为数组下标参与运算
        for i in range(0, len(arr) - 1):
            swapped = False
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if not swapped: break
        return arr


if __name__ == '__main__':
    array = [10, 2, 5, 6, 0, 9, 1, 3, 4, 8, 7]
    solution = Solution()
    print(solution.BubbleSort(array))
