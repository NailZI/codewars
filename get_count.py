def get_count(sentence):
    num = 0
    vowels = ("a", "e", "i", "o", "u")
    for let in vowels:
        num += sentence.count(let)
    return num

if __name__ == "__main__":
    print(get_count("hgftr"))