
def admin_login(admin_user_entered,admin_pass_entered):
    username = "admin"
    password = "admin"

    if username == admin_user_entered and password ==admin_pass_entered :
        return True
    else: 
        print("Invalid credentials.\n")

