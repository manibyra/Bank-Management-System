#customer_menu
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.find_customer import find_customer
from customer.check_balance import check_balance
from customer.deposit_money import deposit_money
from customer.lone_apply  import lone_apply
from customer.lone_status import lone_status
from customer.check_balance import check_balance
from customer.withdraw_money import withdraw_money
from customer.transfer_money import transfer_money


def customer_menu():
    user_entered = input("Enter username: ")
    pin_entered = int(input("Enter pin: "))
    customer = find_customer(user_entered, pin_entered)
    if not customer:
        print("Invalid username or PIN. Exiting menu.")
        return
    
    while True:

        print("\n===== Customer Menu =====")
        print("Enter 1. Check Balance")
        print("Enter 2. Deposit Money")
        print("Enter 3. Withdraw Money")
        print("Enter 4. Transfer Money")
        print("Enter 5. Apply for Loan")
        print("Enter 6. View Loan Status")
        print("Enter 'Exit' to exit the Customer Menu\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(user_entered, pin_entered)
        elif choice == "2":
            deposit_money(user_entered, pin_entered)
        elif choice == "3":
            withdraw_money(user_entered, pin_entered)
        elif choice == "4":
            transfer_money(user_entered, pin_entered)
        elif choice == "5":
            lone_apply(user_entered, pin_entered)
        elif choice == "6":
            lone_status(user_entered, pin_entered)
        elif choice.lower() == "exit":
            print("Exiting Customer Menu\n")
            break
        else:
            print("Enter valid choice.\n")

