
def password_encoder(password):
    encoded_password = ''.join(str((int(digit) + 3))[-1] for digit in password)
    return encoded_password


def decode(encoded_num):
    decoded_num = ''
    for digit in str(encoded_num):
        decoded_digit = (int(digit) - 3) % 10
        decoded_num += str(decoded_digit)
    return decoded_num


def main():
    while True:
        print("menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        try:
            menu_option = int(input("Please enter an option: "))
        except ValueError:
            print("Invalid input")
            continue

        if menu_option == 1:
            password = (input("Please enter your password to encode:  "))
            if len(password) == 8 and password.isdigit():
                encoded_password = password_encoder(password)
                print(f"Your password has been encoded and stored!")
            else:
                print("Invalid input.")
            print("")

        elif menu_option == 2:
            if len(encoded_password) == 8 and encoded_password.isdigit():
                original_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {password}.")
            else:
                print("Invalid input.")
            print()
        elif menu_option == 3:
            break

if __name__ == '__main__':
    main()