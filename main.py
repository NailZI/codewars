
def array_diff(a, b):
    while b[0] in a:
        a.remove(b[0])
    return a


if __name__ == "__main__":
    # array_diff([1, 2], [1]) == [2]
    # array_diff([1, 2, 2, 2, 3], [2]) == [1, 3]
    print(array_diff([1, 2], [1]))
    print(array_diff([1, 2, 2, 2, 3], [2]))