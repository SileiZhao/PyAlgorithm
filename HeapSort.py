class Solution(object):
    def HeapSort(self, arr: [int], n: int) -> [int]:
        # 建堆
        self.buildHeap(arr, n)
        # 建堆完成后堆顶为最大值，下标为0
        for i in range(n - 1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            # 取值之后需要进行堆内调整 i 为剩余结点数 每次调整均需要从 0 开始
            self.heapify(arr, i, 0)
        return arr
    def buildHeap(self, arr: [int], n):
        # 建堆函数只在排序开始后执行一次
        last_node = n - 1
        parent = (last_node + 1) // 2
        for i in range(parent, -1, -1):
            self.heapify(arr, n, i)
    def heapify(self, arr, n, i):
        if i >= n:
            return
        c1 = 2 * i + 1
        c2 = 2 * i + 2
        max = i
        max = c1 if c1 < n and arr[c1] > arr[max] else max
        max = c2 if c2 < n and arr[c2] > arr[max] else max
        if max != i:
            # 交换完成后需要判断是否打乱堆内结构 进行递归 递归范围是max的子结点
            arr[max], arr[i] = arr[i], arr[max]
            self.heapify(arr, n, max)

if __name__ == '__main__':
    arr = [10, 2, 3, 5, 9, 1, 4, 7, 6, 0, 8]
    n = len(arr)
    solution = Solution()
    print(solution.HeapSort(arr, n))
