# find the odd number of occurrences.
# 1) Only one number has an odd number of occurrences.
def FindOddNumber_1(arr: [int]) -> int:
    eor = 0
    for i in arr:
        eor ^= i
    return eor

# 2) Two numbers has an odd number of occurrences.
def FindOddNumber_2(arr: [int]) -> int:
    eor = 0
    eors = 0
    for i in arr:
        eor ^= i
    rightOne = eor & (~eor + 1) # take the right_one 1
    for j in arr:
        if j & rightOne == 0:
            eors ^= j
    eorss = eor ^ eors
    return eors, eorss


if __name__ == '__main__':
    arr = [1, 1, 5, 1, 3, 5, 4, 3, 4, 5, 1, 3]
    print(FindOddNumber_2(arr))