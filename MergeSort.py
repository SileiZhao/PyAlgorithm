from typing import List
class Solution(object):
    @staticmethod
    def merge(arr1: List[int], arr2: List[int]):
        result = []
        while arr1 and arr2:
            if arr1[0] < arr2[0]:
                result.append(arr1.pop(0))
            else:
                result.append(arr2.pop(0))
        if arr1:
            result += arr1
        if arr2:
            result += arr2
        return result

    def merge_sort(self, arr: List[int]):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        return self.merge(self.merge_sort(arr[:mid]), self.merge_sort(arr[mid:]))


if __name__ == '__main__':
    array = [1, 4, 7, 8, 3, 6, 9]
    solution = Solution()
    print(solution.merge_sort(array))