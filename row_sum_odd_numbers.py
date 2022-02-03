def row_sum_odd_numbers(n):
    #your code here
    sum = 0
    max_num = (n+1) * n - 1
    min_num = (n-1) * n + 1
    for i in range(min_num, max_num+1, 2):
        sum += i
        print(i, sum)
    print(min_num, max_num, sum)

row_sum_odd_numbers(10)