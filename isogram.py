def is_isogram(string):
    #your code here
    res = True
    string = string.lower()
    for let in string:
        if string.find(let) != string.rfind(let):
            res = False
    return res

if __name__ == "__main__":
        # "Dermatoglyphics" --> true
        # "aba" --> false
        # "moOse" --> false (ignore letter case)
    print(is_isogram("Dermatoglyphics"))
    print(is_isogram("aba"))
    print(is_isogram("moOse"))