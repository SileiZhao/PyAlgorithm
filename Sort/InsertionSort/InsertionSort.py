class Solution(object):
    @staticmethod
    def InsertionSort(arr: [int]) -> [int]:
        # 同样的，for的外层循环只控制循环次数
        for i in range(1, len(arr)):
            j = i
            # j 是需要和前面已经排好数据比较的次数
            while j > 0:
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
        return arr


if __name__ == "__main__":
    array = [10, 2, 5, 6, 0, 9, 1, 3, 4, 8, 7]
    solution = Solution()
    print(solution.InsertionSort(array))
