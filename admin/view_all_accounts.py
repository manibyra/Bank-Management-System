from admin.admin_login import admin_login
from data import customers

def view_all_accounts():
    
    print("--- Accounts ---")
    for cust in customers:
        print(f"ID: {cust['id']}, Name: {cust['name']}, Username: {cust['username']}, Balance: {cust['balance']}rs")
    print()
