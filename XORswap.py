# how to swap two number with xor?
# but, it does not work if i and j is a same position at a array,
# or i and j is the same address at the memory.
def swap(a: int, b: int) -> int:
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


if __name__ == '__main__':
    a = 12
    b = 29
    print(swap(a, b))