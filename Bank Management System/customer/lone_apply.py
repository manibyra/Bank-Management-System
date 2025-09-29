from utils.find_customer import find_customer
from data import loan_requests , customers

def lone_apply(user_entered, pin_entered):
    customer = find_customer(user_entered, pin_entered)
    amount = int(input("\nEnter lone amount: "))
    if customer in customers:
        loan_requests.append({"id": customer["id"], "username": customer["username"], "amount": amount, "status": "Pending"})
        print(f"Loan request for {amount}rs submitted.\n")
