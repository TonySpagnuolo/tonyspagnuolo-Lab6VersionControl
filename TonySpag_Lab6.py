
def password_encoder(password):
    encoded_password = ''.join(str((int(digit) + 3)) for digit in password)
    return encoded_password




def mian():
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
                print("Your password has been stored!")
            else:
                print("Invalid input.")
            print("")


        elif menu_option == 2:
            print("The encoded password is ")
            pass

        elif menu_option == 3:
            break
if __name__ == '__main__':
    mian()