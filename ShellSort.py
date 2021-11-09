class Solution(object):
    @staticmethod
    def ShellSort(arr: [int]) -> [int]:
        gap = int(len(arr) / 2)
        while gap > 0:
            for i in range(gap, len(arr)):
                j = i
                temp = arr[i]
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap = int(gap / 2)
        return arr

if __name__ == '__main__':
    array = [10, 2, 5, 6, 0, 9, 1, 3, 4, 8, 7]
    solution = Solution()
    print(solution.ShellSort(array))