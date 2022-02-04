def solution(string, ending):
    # your code here...
    result = True
    len_end = len(ending)
    if len_end:
        for i in range(1, len_end+1):
            if ending[i*(-1)] == string [i*(-1)]:
                result = True
            else:
                result = False
    return result

if __name__ == "__main__":
    print(solution('abcde', 'abc'))