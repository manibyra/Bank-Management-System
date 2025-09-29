from data import loan_requests 
from utils.find_customer import find_customer

def lone_status(user_entered, pin_entered):
    customer = find_customer(user_entered, pin_entered)
    loan = None
    for loan_user in loan_requests:
        if loan_user['username'].lower() == customer['username'].lower():
            loan = loan_user
            break
    if loan:
        print(f"Lone Amount: {loan_user['amount']}rs, Status: {loan_user['status']}\n")
        return
    else:
        print("No loan requests found\n")
        return
