def digitize(n):
    lis = []
    for i in str(n):
        lis.append(int(i))
    return lis

if __name__ == "__main__":
    print(digitize(8675309))