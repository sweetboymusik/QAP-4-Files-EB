# Program to calculate insurace policy info
# Written for One Stop Insurance Company
# Dates written: November 17, 2023 - November 24, 2023
# Author: Elliott Butt

# import libraries
import datetime as dt

# define constants
NEXT_POLICY_NUM = 1944
BASIC_PREMIUM_RATE = 869.00
ADD_CAR_DISCOUNT_RATE = 0.25
LIABILITY_OPT_RATE = 130.00
GLASS_OPT_RATE = 86.00
LOAN_OPT_RATE = 58.00
HST_RATE = 0.15
PROCESS_FEE = 39.99
DATE_FORMAT = "%Y-%m-%d"
PAY_PERIOD = 8
COMPANY_NAME = "One Stop Insurance Company"
COMPANY_STREET = "123 Fake Street"
COMPANY_ADD = "City of Townsville, NL A1B 2C3"
COMPANY_PHONE = "709-123-4567"

# define lists (constants continued)
PROV_LIST = ["AB", "BC", "MB", "NB", "NL", "NS",
             "NT", "NV", "ON", "PE", "QC", "SK", "YK"]
PAY_OPT_LIST = ["Full", "Monthly", "Down Pay"]
PREV_CLAIM_DATES = []
PREV_CLAIM_COSTS = []

# welcome message
print()
print("Welcome to One Stop Insurance Company's insurance policy software. Please follow the instructions on the screen.")
print()


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


def add_prev_claim():
    while True:
        try:
            prev_cost = float(input("Enter cost of previous claim: "))
        except:
            print("Previous cost must be a valid number. Please re-enter.")
        else:
            if prev_cost <= 0:
                print("Previous must be greater than 0. Please re-enter.")
            else:
                break
    while True:
        try:
            prev_date = dt.datetime.strptime(
                input("Enter previous claim date (YYYY-MM-DD): "), DATE_FORMAT).date()
        except:
            print("Invalid date. Date must follow the following format: YYYY-MM-DD (including hyphens). Please re-enter.")
        else:
            break

    PREV_CLAIM_COSTS.append(prev_cost)
    PREV_CLAIM_DATES.append(prev_date)


def calc_extra_costs():
    extra_costs = 0

    if liability_opt == "Y":
        extra_costs += LIABILITY_OPT_RATE

    if glass_opt == "Y":
        extra_costs += GLASS_OPT_RATE

    if loan_opt == "Y":
        extra_costs += LOAN_OPT_RATE * num_cars

    return extra_costs


def calc_payment(pay_type, down_payment, total):
    payment = 0

    if pay_type == "Full":
        payment = total
    elif pay_type == "Monthly":
        payment = (PROCESS_FEE + total_cost) / PAY_PERIOD
    elif pay_type == "Down Pay":
        payment = (PROCESS_FEE + (total_cost - down_payment)) / PAY_PERIOD

    return payment


def format_dollar_amt(val):
    format1 = f"${val:,.2f}"
    format2 = f"{format1:>10s}"

    return format2


def format_center(str):
    formatted = f"{str:^36s}"

    return formatted


def format_phone_number(num):
    pt1 = num[0:3]
    pt2 = num[3:6]
    pt3 = num[6:10]
    formatted = f"{pt1}-{pt2}-{pt3}"

    return formatted


def print_prev_claims(amounts, dates):
    print(f"Claim #      Claim Date       Amount")
    print("-" * 36)

    for i in range(0, len(dates)):
        print(
            f"   {i + 1}.        {dates[i]}   {format_dollar_amt(amounts[i])}")


# main program loop
while True:

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
        cust_postal_add = input(
            "Enter customer postal code (X#X#X#): ").upper()

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
            print("Must answer 'Y' for yes or 'N' for no. Please re-enter")
        else:
            break

    while True:
        pay_opt = input(
            "Enter desired payment option (Full, Monthly, or Down Pay): ").title()

        if pay_opt == "":
            print("Optional loaner car cannot be empty. Please re-enter.")
        elif pay_opt not in PAY_OPT_LIST:
            print(
                "Payment option must be 'Full', 'Monthly', or 'Down Pay'. Please re-enter")
        else:
            break

    while True:
        if pay_opt != "Down Pay":
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

    while True:
        claim_opt = input(
            "Enter a previous claim? (Y to add, press Enter to finish): ").upper()

        if claim_opt != "Y" and claim_opt != "":
            print("Must answer 'Y' to add or press Enter to finish. Please re-enter.")
        else:
            if claim_opt == "Y":
                add_prev_claim()
            else:
                break

    # calculations
    insurance_premiums = BASIC_PREMIUM_RATE
    if num_cars > 1:
        insurance_premiums += (BASIC_PREMIUM_RATE *
                               ADD_CAR_DISCOUNT_RATE) * (num_cars - 1)

    extra_costs = calc_extra_costs()

    total_insurance_premium = insurance_premiums + extra_costs
    taxes = total_insurance_premium * HST_RATE
    total_cost = total_insurance_premium + taxes

    monthly_payment = calc_payment(pay_opt, dp_amount, total_cost)

    inv_date = dt.date.today()
    pay_date = dt.date(inv_date.year, inv_date.month + 1, 1)

    # output
    print()
    print(format_center(COMPANY_NAME))
    print(format_center(COMPANY_STREET))
    print(format_center(COMPANY_ADD))
    print(format_center(COMPANY_PHONE))
    print()
    print(f"Policy #: {NEXT_POLICY_NUM}")
    print(f"Inv Date: {str(inv_date.strftime('%B %d, %Y')):>10s}")

    print("-" * 36)

    print(f"{format_center('Customer Info')}")
    print()
    print(f"Name:     {(cust_first_name + ' ' + cust_last_name):<20s}")
    print(f"Phone #:  {format_phone_number(cust_phone_num):<12s}")
    print(f"Address:  {cust_street_add:<20s}")
    print(
        f"          {(cust_city_add + ', ' + cust_prov_add + ' ' + cust_postal_add[0:3] + ' ' + cust_postal_add[3:6]):<20s}")

    print("-" * 36)

    print(f"{format_center('Details')}")
    print()
    print(f"Number of cars:                   {num_cars:>2d}")
    print(
        f"Liability Option:                {'YES' if liability_opt == 'Y' else 'NO':>3s}")
    print(
        f"Glass Option:                    {'YES' if glass_opt == 'Y' else 'NO':>3s}")
    print(
        f"Loan Option:                     {'YES' if loan_opt == 'Y' else 'NO':>3s}")
    print(f"Payment Option:             {pay_opt:>8s}")

    print("-" * 36)

    print(f"{format_center('Totals')}")
    print()
    print(f"Insurance Premiums:       {format_dollar_amt(insurance_premiums)}")
    print(f"Extra Costs:              {format_dollar_amt(extra_costs)}")
    print(
        f"Sub-Total:                {format_dollar_amt(total_insurance_premium)}")
    print(f"HST:                      {format_dollar_amt(taxes)}")
    print(f"{' ' * 25}{'-' * 11}")
    print(f"Total:                    {format_dollar_amt(total_cost)}")
    print()
    if pay_opt == "Down Pay":
        print(f"Down Payment:            -{format_dollar_amt(dp_amount)}")
    print(
        f"Monthly Payment:          {'N/A' if monthly_payment == 0 else str(format_dollar_amt(monthly_payment)):>10s}")
    print(
        f"First Payment Date:       {'N/A' if monthly_payment == 0  else str(pay_date):>10s}")

    print("-" * 36)

    print(f"{format_center('Previous Claims')}")
    print()
    print_prev_claims(PREV_CLAIM_COSTS, PREV_CLAIM_DATES)

    print()

    # increment policy number / reset previous claims
    NEXT_POLICY_NUM += 1
    PREV_CLAIM_COSTS = []
    PREV_CLAIM_DATES = []

    # prompt to continue
    while True:
        cont = input(
            "Would you like to enter another policy? (Y/N): ").upper()

        if cont == "" or (cont != "Y" and cont != "N"):
            print("Must enter 'Y' or 'N'. Please re-enter.")
        else:
            break

    if cont == "N":
        print("Thank you for using our program. Have a great day!")
        break
