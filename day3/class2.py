balance = 10000

pin = input("input your pin: ")

if pin == "1234":
    print("Welcome!")
    print("1. check balance")
    print("2. Withdraw money")
    print("3. Deposit money")
    print("4. Exit")

    option = input("choose an option: ")

    if option == "1":
        print(f"your balance is n{balance}")

    elif option =="2":
        amount = int(input("how much do you wanna withdraw: "))

        if balance < amount:
            print("insufficient funds")

        else:
            balance -= amount
            print(f"withdrawal succesful. new balance = N{balance}")

    elif option == "3":
        amount =  int(input("how much do you wanna deposit: "))
        balance += amount
        print(f" your new balance is N{balance}")

    elif option == "4":
        print("thank you for using our ATM")

    else:
        print("invalid option")

else:
    print("incorrect pin")