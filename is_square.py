# Name of file
# import
def is_square(n):
    # return n > -1 and math.sqrt(n) % 1 == 0
    if n >= 0:
        num = n ** 0.5
        if num == int(num):
            return True
    return False # fix me

if __name__ == "__main__":
    print(is_square(-1))
