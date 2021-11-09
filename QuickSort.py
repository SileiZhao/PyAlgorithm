class Solution(object):
    @staticmethod
    def partition(arr, leftBound, rightBound):
        left = leftBound
        right = rightBound - 2
        pivot = rightBound - 1
        while left < right:
            while left <= right and arr[left] <= arr[pivot]:
                left += 1
            while left <= right and arr[right] > arr[pivot]:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
        arr[left], arr[pivot] = arr[pivot], arr[left]
        return left

    def QuickSort(self, arr: [int], leftBound, rightBound):
        if leftBound >= rightBound:
            return arr
        mid = self.partition(arr, leftBound, rightBound)
        self.QuickSort(arr, leftBound, mid)
        self.QuickSort(arr, mid + 1, rightBound)
        return arr

if __name__ == '__main__':
    array = [7, 3, 2, 8, 1, 9, 5, 4, 6, 10, 0]
    solution = Solution()
    print(solution.QuickSort(array, 0, len(array)))
