from data import loan_requests 
from admin.admin_login import admin_login

def view_lone_requests():
        
    for loans in loan_requests:
        print(f"Id: {loans['id']} , Usernames: {loans['username']}:, Loan amount:{loans['amount']}rs, Status: {loans['status']}")
    print()

