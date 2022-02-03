def duplicate_encode(word):
    #your code here

    if __name__ == "__main__":
        # "din"      =>  "((("
        # "recede"   =>  "()()()"
        # "Success"  =>  ")())())"
        # "(( @"     =>  "))(("
        print(duplicate_encode("din"))
        print(duplicate_encode("recede"))
        print(duplicate_encode("Success"))
        print(duplicate_encode("(( @"))
