def options():
    return input(f"{user} would you like to withraw of deposit money?: ")

def deposit():
    print("----------------------")
    return(int(input(f"how much money would you like to deposit into your bank account {user}: ")))

def withraw():
    print("----------------------")
    return(int(input(f"how much money would you like to withraw into your bank account {user}: ")))



def password():
    return int(input(f"insert your password {user}: "))

print("----------------------------------")
print("   ")
print("Welcome to banana republic bank")
print("   ")
user = input("Write your username to continue: ")
print("   ")
print("----------------------------------")
roman_balance = 500
xavier_balance = 200
#Usernames avalible and amount of money
match user:                                                                                     
    case "roman":
        pin = 1234
        if password() == pin:
            print(f"welcome {user}")
            option = options()
            if option == "deposit":
                moneydeposit = deposit()
                print(f"you've deposit the amount of {moneydeposit} now your balance is:", moneydeposit + roman_balance)
            elif option == "withraw":
                moneywithraw = withraw()
                print(f"you've withdrew the amount of {moneywithraw} now your balance is:", roman_balance - moneywithraw)
        else:
            print("pin incorrecto")
