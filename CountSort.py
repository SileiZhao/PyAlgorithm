class Solution(object):
    @staticmethod
    def CountSort(arr: [int]) -> [int]:
        min_number = min(arr)
        max_number = max(arr)
        count = [0 for _ in range(min_number, max_number + 1)]
        result = []
        for i in arr:
            count[i - min_number] += 1
        j, index = 0, 0
        while index < len(count):
            while count[j] > 0:
                result.append(index + min_number)
                count[j] -= 1
            index += 1
            j += 1
        return result
    # 稳定的计数排序
    def CountSort_1(self, arr: [int]) -> [int]:
        min_number = min(arr)
        max_number = max(arr)
        count = [0 for _ in range(min_number, max_number + 1)]
        result = [0 for _ in range(len(arr) + 1)]
        for i in arr:
            count[i - min_number] += 1
        # 构建累加数组
        for j in range(1, len(count)):
            count[j] += count[j - 1]
        # 倒序遍历数组寻找各个位置
        for k in range(len(arr) - 1, -1, -1):
            result[count[arr[k] - min_number]] = arr[k]
            count[arr[k] - min_number] -= 1
        return result


if __name__ == '__main__':
    array = [2, 4, 2, 3, 7, 1, 1, 0, 0, 5, 6, 9, 8, 5, 7, 4, 0, 9]
    solution = Solution()
    print(solution.CountSort(array))