from menus.customer_menu import customer_menu
from menus.admin_menu import admin_menu

def main_menu():
    while True:
        print("\n===== Bank Management System =====")
        print("Enter 1. to Customer Menu")
        print("Enter 2. to Admin Menu")
        print("Type 'Exit' to quit the Bank system\n")
        user_choice = input("Enter Your choice: ")
        
        if user_choice == "1":
            customer_menu()
        elif user_choice== "2":
            admin_menu()
        elif user_choice.lower() == "exit":
            print("Exiting the Bank system. Goodbye!")
            return
        else:
            print("Enter vaild Credits")
        
main_menu()

