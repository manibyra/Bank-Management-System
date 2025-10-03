from utils.find_customer import find_customer

def deposit_money(user_entered, pin_entered):
    amount = int(input("\nEnter the amount to Deposit: "))
    customer = find_customer(user_entered, pin_entered)
    if customer:
        customer['balance'] += amount
        print(f"Amount deposited {amount}rs. New balance is {customer['balance']}rs\n")
    # else:
    #     print("Invalid credentials.\n")
