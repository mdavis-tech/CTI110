# Misti Davis
# April 20, 2026
# P5LAB - Self Checkout Change Dispenser
# This program simulates a self-checkout machine. It generates a random total owed,
# accepts user payment, calculates change, and displays the breakdown of coins.

import random

# Function to calculate and display change
def disperse_change(change):
    # Convert to cents to avoid float issues
    cents = int(round(change * 100))

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    print("\nChange to be given:")
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")


def main():
    # Generate random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${total_owed}")

    # Get user payment
    cash = float(input("How much cash will you put in the self-checkout?: $"))

    # Validate input
    while cash < total_owed:
        print("Not enough money. Please enter an amount equal to or greater than the total owed.")
        cash = float(input("Enter amount of cash: $"))

    # Calculate change
    change = round(cash - total_owed, 2)
    print(f"Change owed: ${change}")

    # Call function
    disperse_change(change)


# Call main function
main()
