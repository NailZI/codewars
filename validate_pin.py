# Name of file
# import
def validate_pin(pin):
    #return true or false
    return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)


if __name__ == "__main__":
    print(validate_pin('12l6'))
