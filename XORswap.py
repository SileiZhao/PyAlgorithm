# how to swap two number with xor?
def swap(a: int, b: int) -> int:
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


if __name__ == '__main__':
    a = 12
    b = 29
    print(swap(a, b))