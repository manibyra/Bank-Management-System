from utils.find_customer import find_customer

def check_balance(user_entered, pin_entered):
    customer = find_customer(user_entered, pin_entered)
    if customer:
        print(f"\nYour current balance is {customer['balance']}rs")
    # else:
    #     print("Invalid credentials.\n")
