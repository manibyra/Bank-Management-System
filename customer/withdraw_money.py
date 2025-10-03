from utils.find_customer import find_customer

def withdraw_money(user_entered, pin_entered):
    amount = int(input("Enter the amount to withdraw: "))
    customer = find_customer(user_entered, pin_entered)
    if customer:
        customer['balance'] -= amount
        print(f"Amount withdrawed is {amount} new balance is {customer['balance']}rs\n")
    # else:
    #     print("Invalid credentials.\n")
