from data import loan_requests

def update_lones():
    while True:
        username_entered= input("Enter username of Lone person to Approve/Reject the loan \nor type 'Exit' to quit: ")
        
        if username_entered.lower() == "exit":
            print("Exiting the Loan updates \n")
            break
        
        loan = None 
        for request in loan_requests:
            if request["username"].lower() == username_entered.lower():
                loan = request
                break
        if not loan:
            print(f"No loan is Found for user {username_entered}\n")
            continue
         
        print("\nEnter a - Approve The Loan")
        print("Enter b - Reject The Loan")
        print("Enter 0 (Zero) - To Pause\n")
        status_update = input("Your choice: ")

        if status_update == "a":
            loan['status'] = 'Approved'
            print(f"Loan amount of {loan['amount']}rs Approved for {username_entered}\n")
        elif status_update == "b":
            loan['status'] = 'Rejected'
            print(f"Loan amount of {loan['amount']}rs Rejected for {username_entered}\n")
        elif status_update == "0":
            print(f"No changes made for {username_entered}\n")
        else:
            print("Enter vaild choice \n")