# Name of file
# import
def get_sum(a,b):
    #good luck!
    # return sum(range(min(a, b), max(a, b) + 1))
    sum = 0
    if a < b:
        start, stop = a, b
    else:
        start, stop = b, a
    for i in range(start, stop+1):
        sum += i
    return sum


if __name__ == "__main__":
    print(get_sum(5, 1))
