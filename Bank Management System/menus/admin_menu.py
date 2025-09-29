#admin_menu
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from admin.update_lones import update_lones
from admin.view_all_accounts import view_all_accounts
from admin.view_lone_requests import view_lone_requests
from admin.admin_login import admin_login

def admin_menu():
    admin_user_entered = input("Enter admin username: ")
    admin_pass_entered = input("Enter admin password: ")
    admin = admin_login(admin_user_entered, admin_pass_entered)
    if admin:
        while True:
            print("Enter 1 - view all accounts")
            print("Enter 2 - view lone requests")
            print("Enter 3 - update_lones")
            print("Enter 'Exit' to quite from admin menu\n")

            admin_choice = input("Enter your choice: ")

            if admin_choice == "1":
                view_all_accounts()
                            
            elif admin_choice == "2":
                view_lone_requests()

            elif admin_choice == "3":
                update_lones()
            elif admin_choice.lower() == "exit":
                print("Exiting from admin menu\n")
                return
            else: 
                print("Enter vaild choice ") 


