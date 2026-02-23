balance = 10000.0
print("\n1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")
choice = input("\nEnter choice (1-3): ")
if choice == '1':
    print(f"\nYour current balance is: {balance:,.2f}")
elif choice == '2':
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    print(f"New balance: {balance:,.2f}")
elif choice == '3':
    amount = float(input("Enter amount to withdraw: "))
    if balance <500:    
        print(f" You must maintain a minimum balance of 500.")
        print(f"Maximum you can withdraw: {balance - 500:,.2f}")
    else:
        balance -= amount
        print(f" New balance: {balance:,.2f}")
else:
    print("Invalid choice")
