exitCommand = "n"
while exitCommand != "y":
    password = input("Password: ")
    passwordLength = len(password)
    while passwordLength < 6 or passwordLength > 15:
        if passwordLength < 6:
            print("Password must be at least 6 characters long")
        else:
            print("Password can not exceed 15 characters")
        password = input("Password: ")
        passwordLength = len(password)
    for i in range(0, passwordLength, 1):
        print("*", end="")
    print()
    exitCommand = input("Exit? (y/n): ")