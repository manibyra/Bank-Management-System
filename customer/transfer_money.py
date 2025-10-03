from utils.find_customer import find_customer
from data import customers

def transfer_money(user_entered, pin_entered):
    sender = find_customer(user_entered, pin_entered)
    receiver_username = input("Enter receiver username: ")
    amount = int(input("Enter the amount you want to transfer: "))
    receiver = None
    for rec_check in customers:
        if rec_check['username'].lower() == receiver_username.lower():
            receiver = rec_check
            break
    
    if not receiver:
        print("Receiver not found.\n")
        return
    
    if sender['balance'] >= amount:
        receiver['balance'] += amount
        sender['balance'] -= amount
        print(f"Transaction Successful your current balance is: {sender['balance']}rs \n")
       
    else:
        print("\nLow balance")
        return