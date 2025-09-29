# utils/find_customer.py
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from data import customers

def find_customer(user_entered, pin_entered):
    for customer in customers:         
        if customer['username'].lower() ==user_entered.lower() and customer['pin'] == pin_entered:
            return customer
    # print("Invalid credentials.\n")

