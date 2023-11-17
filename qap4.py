# Program to calculate insurace policy info
# Written for One Stop Insurance Compay
# Dates written: November 17, 2023 -
# Author: Elliott Butt

next_policy_num = 1944
basic_premium = 869.00
add_car_discount = 0.25
liability_cov = 130.00
glass_cov = 86.00
loan_coverage = 58.00
HST_RATE = 0.15
PROCESS_FEE = 39.99

PROV_LIST = ["AB", "BC", "MB", "NB", "NL", "NS",
             "NT", "NV", "ON", "PE", "QC", "SK", "YK"]
PAY_OPT_LIST = ["F", "M", "D"]


# define functions
def check_postal_code(code):
    correct = False

    for i, char in enumerate(code):
        if (i + 1) % 2 != 0:
            if char.isalpha():
                correct = True
            else:
                correct = False
                break
        elif (i + 1) % 2 == 0:
            if char.isdigit():
                correct = True
            else:
                correct = False
                break

    return correct


# inputs and validations

while True:
    cust_first_name = input("Enter customer first name: ").title()

    if cust_first_name == "":
        print("First name cannot be empty. Please re-enter.")
    else:
        break

while True:
    cust_last_name = input("Enter customer last name: ").title()

    if cust_last_name == "":
        print("Last name cannot be empty. Please re-enter.")
    else:
        break

while True:
    cust_street_add = input("Enter customer street address: ").title()

    if cust_street_add == "":
        print("Street address cannot be empty. Please re-enter.")
    else:
        break

while True:
    cust_city_add = input("Enter customer city address: ").title()

    if cust_city_add == "":
        print("City address cannot be empty. Please re-enter.")
    else:
        break

while True:
    cust_prov_add = input("Enter customer province (XX): ").upper()

    if cust_prov_add == "":
        print("Province cannot be empty. Please re-enter.")
    elif len(cust_prov_add) != 2:
        print("Province must be two characters in length. Please re-enter.")
    elif cust_prov_add not in PROV_LIST:
        print("Not a valid province code. Please re-enter.")
    else:
        break

while True:
    cust_postal_add = input("Enter customer postal code (X#X#X#): ").upper()

    if cust_postal_add == "":
        print("City address cannot be empty. Please re-enter.")
    elif len(cust_postal_add) != 6:
        print("Postal code must be six characters in length and follow the folling format: X#X#X#. Please re-enter.")
    else:
        if check_postal_code(cust_postal_add) == False:
            print(
                "Postal code must follow the folling format: X#X#X#. Please re-enter.")
        else:
            break

while True:
    cust_phone_num = input(
        "Enter customer ten-digit phone number (##########): ")

    if cust_phone_num == "":
        print("Phone number cannot be empty. Please re-enter.")
    elif len(cust_phone_num) != 10:
        print(cust_phone_num)
        print("Phone number must be ten characters in length and follow the following format: (###-###-####). Please re-enter.")
    else:
        break

while True:
    try:
        num_cars = int(input("Enter number of cars being insured: "))
    except:
        print("Cars to be unsured must be a valid integer number. Please re-enter.")
    else:
        if num_cars < 1:
            print("Number of cars cannot be less than 1. Please re-enter.")
        else:
            break

while True:
    liability_opt = input(
        "Would you like optional extra liability coverage up to $1,000,000? (Y/N): ").upper()

    if liability_opt == "":
        print("Optional extra liability coverage cannot be empty. Please re-enter.")
    elif liability_opt != "Y" and liability_opt != "N":
        print("Must answer 'Y' for yes or 'N' for no. Please re-enter")
    else:
        break

while True:
    glass_opt = input(
        "Would you like optional glass coverage? (Y/N): ").upper()

    if glass_opt == "":
        print("Optional glass coverage cannot be empty. Please re-enter.")
    elif glass_opt != "Y" and glass_opt != "N":
        print("Must answer 'Y' for yes or 'N' for no. Please re-enter")
    else:
        break

while True:
    loan_opt = input(
        "Would you like an optional loaner car? (Y/N): ").upper()

    if loan_opt == "":
        print("Optional loaner car cannot be empty. Please re-enter.")
    elif loan_opt != "Y" and loan_opt != "N":
        print("Must answer 'Y' for yes or  'N' for no. Please re-enter")
    else:
        break

while True:
    pay_opt = input(
        "Enter desired payment option ('F' for full, 'M' for monthly, or 'D' for down pay): ").upper()

    if pay_opt == "":
        print("Optional loaner car cannot be empty. Please re-enter.")
    elif pay_opt not in PAY_OPT_LIST:
        print("Payment option must be 'F', 'M', or 'D'. Please re-enter")
    else:
        break

while True:
    if pay_opt != "D":
        dp_amount = 0.00
        break

    try:
        dp_amount = float(input("Enter down payment amount: "))
    except:
        print("Down payment must be a valid number. Please re-enter.")
    else:
        if dp_amount <= 0:
            print("Down payment amount cannot be 0 (or less). Please re-enter.")
        else:
            break
