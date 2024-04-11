#molly crossman

def encode(password):
    x = ''
    for i in range(len(password)):
        b = str(int(password[i]) + 3)
        x += b
    return x

def decode(encode_password):
    pass


def main():
    while True:
        print('''Menu
-------------
1. Encode
2. Decode
3. Quit''')
        print()

        x = int(input("Please enter an option: "))

        if x == 1:
            password = str(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
            encode_password = encode(password)
            print()
            continue

        if x == 2:
            y = decode(encode_password)
            print("The encoded password is,",encode_password,", and the original password is",y,'.')
            continue


        else:
            break



if __name__ == "__main__":
    main()