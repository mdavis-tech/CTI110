# P3LAB_DavisMisti.py
# Author: Misti Davis
# Date: 03/15/2026
# Description: This program accepts a monetary value and calculates
# the most efficient number of dollars, quarters, dimes, nickels,
# and pennies needed to make that amount.

# Get input
money = float(input("Enter the amount of money as a float: $"))

# Convert to cents
cents = int(money * 100)

# If no money entered
if cents == 0:
    print("No change")

else:
    dollars = cents // 100
    cents -= dollars * 100

    quarters = cents // 25
    cents -= quarters * 25

    dimes = cents // 10
    cents -= dimes * 10

    nickels = cents // 5
    cents -= nickels * 5

    pennies = cents

    if dollars > 0:
        if dollars == 1:
            print("1 Dollar")
        else:
            print(f"{dollars} Dollars")

    if quarters > 0:
        if quarters == 1:
            print("1 Quarter")
        else:
            print(f"{quarters} Quarters")

    if dimes > 0:
        if dimes == 1:
            print("1 Dime")
        else:
            print(f"{dimes} Dimes")

    if nickels > 0:
        if nickels == 1:
            print("1 Nickel")
        else:
            print(f"{nickels} Nickels")

    if pennies > 0:
        if pennies == 1:
            print("1 Penny")
        else:
            print(f"{pennies} Pennies")