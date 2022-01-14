# at a array, every number which the left number is smaller then the number, 
# and sum that, we called it Small Sum.
# [1 ,3, 4, 2, 5]
def process(arr: [int], left: int, right: int):
    if left == right:
        return 0
    mid = left + ((right - left) >> 1)
    return process(arr, left, mid) + process(arr, mid + 1, right) + merge(arr, left, mid, right)


def merge(arr: [int], start, mid, end):
    left = start  # pointer of left array
    right = mid + 1  # pointer of right array
    res = []
    smallSum = 0
    while left <= mid and right <= end:
        # it must carry the number of right array when the arr[right] is equal to arr[left]
        if arr[left] < arr[right]:
            smallSum = smallSum + arr[left] * (end - right + 1)
            res.append(arr[left])
            left += 1
        else:
            res.append(arr[right])
            right += 1
    while left <= mid:
        res.append(arr[left])
        left += 1
    while right <= end:
        res.append(arr[right])
        right += 1
    # save the number into the original array, if not every recursion will give the last result up.
    for i in range(len(res)):
        arr[start + i] = res[i]
    return smallSum


if __name__ == '__main__':
    arr = [1, 3, 4, 2, 5]
    print(process(arr, 0, len(arr) - 1))
