# Mini Bank System

accounts = {}

def create_account():
    username = input("Enter your name: ")
    if username in accounts:
        print("Account already exists!")
        return
    
    password = input("Set your password: ")
    balance = 0
    accounts[username] = {"password": password, "balance": balance}
    print("✅ Account created successfully!")

def login():
    username = input("Enter your name: ")
    password = input("Enter your password: ")

    if username in accounts and accounts[username]["password"] == password:
        print(f"✅ Welcome {username}!")
        return username
    else:
        print("❌ Invalid login!")
        return None

def deposit(user):
    amount = float(input("Enter amount to deposit: "))
    accounts[user]["balance"] += amount
    print("💰 Amount deposited successfully!")

def withdraw(user):
    amount = float(input("Enter amount to withdraw: "))
    if amount > accounts[user]["balance"]:
        print("❌ Insufficient balance!")
    else:
        accounts[user]["balance"] -= amount
        print("💸 Withdrawal successful!")

def check_balance(user):
    print(f"💼 Your balance is: {accounts[user]['balance']}")

def main():
    while True:
        print("\n====== 🏦 MINI BANK ======")
        print("1. Open Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\n--- Banking Menu ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")

                    opt = input("Enter option: ")

                    if opt == "1":
                        deposit(user)
                    elif opt == "2":
                        withdraw(user)
                    elif opt == "3":
                        check_balance(user)
                    elif opt == "4":
                        print("👋 Logged out!")
                        break
                    else:
                        print("Invalid option!")

        elif choice == "3":
            print("Thank you for using Mini Bank!")
            break
        else:
            print("Invalid choice!")

# Run program
main()